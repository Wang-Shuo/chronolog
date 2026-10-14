"""Deploy only a merged PR commit with approval of its final reviewed head."""
import argparse
import json
import os
from pathlib import Path
import subprocess


def approved_merge(pr: dict, reviews: list[dict], commit: str, base: str) -> bool:
    if not pr.get('merged_at') or pr.get('merge_commit_sha')!=commit or pr['base']['ref']!=base:
        return False
    latest={}
    for r in sorted(reviews,key=lambda x:x.get('submitted_at') or ''):
        if r['state'] in {'APPROVED','CHANGES_REQUESTED','DISMISSED'}:
            latest[r['user']['login']]=r
    if any(r['state']=='CHANGES_REQUESTED' for r in latest.values()):return False
    return any(r['state']=='APPROVED' and r.get('commit_id')==pr['head']['sha'] and
        r['user'].get('type')!='Bot' and r['user']['login']!=pr['user']['login'] for r in latest.values())


def api(path: str) -> object:
    return json.loads(subprocess.check_output(['gh','api',path],text=True))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--commit',required=True);p.add_argument('--base',required=True)
    p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    repo=os.environ['GITHUB_REPOSITORY']
    pulls=api(f'repos/{repo}/commits/{a.commit}/pulls?per_page=100')
    accepted=[]
    for item in pulls:
        pr=api(f'repos/{repo}/pulls/{item["number"]}')
        # GitHub CLI paginates this array without dropping older dismissals.
        reviews=json.loads(subprocess.check_output(['gh','api','--paginate','--slurp',
            f'repos/{repo}/pulls/{item["number"]}/reviews?per_page=100'],text=True))
        flat=[r for page in reviews for r in page]
        if approved_merge(pr,flat,a.commit,a.base):accepted.append(pr['html_url'])
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps({'commit':a.commit,'approved_merged_prs':accepted,
        'status':'passed' if accepted else 'failed'},indent=2)+'\n')
    if not accepted:raise SystemExit('Deployment requires a merged PR and human approval on its final head; direct pushes are not deployed.')

if __name__=='__main__':main()
