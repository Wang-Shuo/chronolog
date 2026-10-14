"""Maintain one review branch; preserve open-PR edits and use an exact push lease."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import subprocess

BRANCH = 'codex/chronolog-updates'
VAULT = ['Products','Releases','Changes','Themes','Alerts','_review','index.md']


def cmd(root: Path, *args: str) -> str:
    return subprocess.check_output(args,cwd=root,text=True).strip()


def prepare(root: Path, base: str, state_path: Path) -> dict:
    cmd(root,'git','check-ref-format','--branch',base)
    if cmd(root,'git','status','--porcelain'):
        raise ValueError('prepare requires a clean disposable CI checkout')
    cmd(root,'git','fetch','origin',base)
    prs=json.loads(cmd(root,'gh','pr','list','--state','open','--head',BRANCH,'--base',base,
                       '--json','number,url'))
    if len(prs)>1:
        raise ValueError('multiple open rolling PRs; reconcile them before generation')
    remote=cmd(root,'git','ls-remote','--heads','origin','refs/heads/'+BRANCH)
    sha=remote.split()[0] if remote else ''
    if prs:
        if not sha:raise ValueError('open rolling PR has no remote branch')
        cmd(root,'git','fetch','origin',BRANCH)
        cmd(root,'git','switch','-C',BRANCH,'origin/'+BRANCH)
        # Conflicts stop here, preserving remote content and the evidence artifact.
        cmd(root,'git','merge','--no-edit','origin/'+base)
    else:
        cmd(root,'git','switch','-C',BRANCH,'origin/'+base)
    state={'base':base,'branch':BRANCH,'expected_remote_head':sha,'pr':prs[0] if prs else None}
    state_path.parent.mkdir(parents=True,exist_ok=True)
    state_path.write_text(json.dumps(state,indent=2)+'\n')
    return state


def publish(root: Path, state: dict, report_dir: Path) -> dict:
    report=json.loads((report_dir/'quality.json').read_text())
    if report['status'] not in {'candidate-applied','no-change'}:
        raise ValueError('generation did not pass all gates')
    if cmd(root,'git','branch','--show-current')!=BRANCH:
        raise ValueError('must publish from the managed review branch')
    if report['status']=='no-change':
        return {'status':'no-change','pr':state['pr']}
    paths=[p for p in VAULT if (root/p).exists()]
    cmd(root,'git','add','--',*paths)
    staged=cmd(root,'git','diff','--cached','--name-only').splitlines()
    if any(p.split('/')[0] not in VAULT for p in staged):
        raise ValueError('unexpected staged file outside generated Vault scope')
    if not staged:return {'status':'no-change','pr':state['pr']}
    cmd(root,'git','commit','-m',f"chore: refresh ChronoLog sources ({report['run_id']})")
    cmd(root,'git','push',f"--force-with-lease=refs/heads/{BRANCH}:{state['expected_remote_head']}",
        'origin',f'HEAD:refs/heads/{BRANCH}')
    body=report_dir/'pr-body.md'
    body.write_text((report_dir/'quality.md').read_text()+
        f"\nRun evidence: {os.environ.get('GITHUB_SERVER_URL','https://github.com')}/{os.environ['GITHUB_REPOSITORY']}/actions/runs/{os.environ['GITHUB_RUN_ID']}\n")
    title='chore: review ChronoLog source updates'
    if state['pr']:
        cmd(root,'gh','pr','edit',str(state['pr']['number']),'--title',title,'--body-file',str(body))
        url=state['pr']['url']
    else:
        url=cmd(root,'gh','pr','create','--base',state['base'],'--head',BRANCH,'--title',title,'--body-file',str(body))
    return {'status':'review-required','url':url,'head':cmd(root,'git','rev-parse','HEAD')}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('action',choices=['prepare','publish'])
    p.add_argument('--root',type=Path,default=Path.cwd());p.add_argument('--base',default='main')
    p.add_argument('--state',type=Path,required=True);p.add_argument('--report',type=Path)
    a=p.parse_args()
    if a.action=='prepare':result=prepare(a.root,a.base,a.state)
    else:
        if not a.report:p.error('publish requires --report')
        try:
            result=publish(a.root,json.loads(a.state.read_text()),a.report)
        except Exception as exc:
            (a.report/'rolling-pr.json').write_text(json.dumps({'status':'failed','error':str(exc)},indent=2)+'\n')
            raise
        (a.report/'rolling-pr.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
