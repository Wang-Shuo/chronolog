"""Collect evidence from seven real daily GitHub scheduled runs, never offline replays."""
import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import subprocess


def assess(runs: list[dict], reports: dict[int, dict], now: datetime) -> dict:
    if len(runs)!=7 or len({r['databaseId'] for r in runs})!=7:
        raise ValueError('seven distinct real scheduled runs are required')
    days=[]
    for run in runs:
        if run['event']!='schedule' or run['status']!='completed':
            raise ValueError('only completed GitHub schedule events qualify')
        created=datetime.fromisoformat(run['createdAt'].replace('Z','+00:00'))
        days.append(created.date())
        report=reports[run['databaseId']]
        if report.get('input_kind')!='live':
            raise ValueError('offline replay cannot satisfy continuous operations acceptance')
        if report.get('status') not in {'no-change','candidate-applied','failed'}:
            raise ValueError('scheduled run lacks a terminal generation report')
        if {s['product'] for s in report.get('sources',[])}!={'chatgpt','claude-code','cursor'}:
            raise ValueError('run evidence must account for each requested source')
        if any(s.get('status') not in {'success','failed','not-attempted'} for s in report['sources']):
            raise ValueError('source status is missing')
        if run['conclusion']=='success' and report['status']=='failed':
            raise ValueError('GitHub success masks a failed run report')
    days=sorted(days)
    if len(set(days))!=7 or any(b-a!=timedelta(days=1) for a,b in zip(days,days[1:])):
        raise ValueError('the seven runs must cover consecutive daily schedules')
    newest=max(datetime.fromisoformat(r['createdAt'].replace('Z','+00:00')) for r in runs)
    if now-newest>timedelta(hours=36):raise ValueError('latest scheduled execution is stale')
    return {'status':'passed','scheduled_runs':7,'from':str(days[0]),'through':str(days[-1]),
            'run_ids':[r['databaseId'] for r in runs],
            'conclusions':{str(r['databaseId']):r['conclusion'] for r in runs}}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',required=True)
    p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists():p.error('output must be a new evidence directory')
    a.output.mkdir(parents=True)
    runs=json.loads(subprocess.check_output(['gh','run','list','--repo',a.repo,'--workflow','generate.yml',
        '--event','schedule','--limit','7','--json','databaseId,event,status,conclusion,createdAt,url,headSha'],text=True))
    reports={}
    for run in runs:
        current=json.loads(subprocess.check_output(['gh','api',
            f'repos/{a.repo}/actions/runs/{run["databaseId"]}'],text=True))
        if (current['id']!=run['databaseId'] or current['event']!='schedule'
                or current['status']!='completed' or current['head_sha']!=run['headSha']
                or current['conclusion']!=run['conclusion']):
            raise ValueError('scheduled run changed while collecting evidence; rerun after it completes')
        attempt=current['run_attempt']
        if not isinstance(attempt,int) or isinstance(attempt,bool) or attempt<1:
            raise ValueError('GitHub run attempt must be a positive integer')
        run['selectedAttempt']=attempt
        run['artifactName']=f'generation-{run["databaseId"]}-{attempt}'
        dest=a.output/str(run['databaseId'])
        subprocess.run(['gh','run','download',str(run['databaseId']),'--repo',a.repo,
            '--name',run['artifactName'],'--dir',str(dest)],check=True)
        found=list(dest.rglob('quality.json'))
        if len(found)!=1:raise ValueError('selected run attempt must contain exactly one quality report')
        reports[run['databaseId']]=json.loads(found[0].read_text())
    result=assess(runs,reports,datetime.now(timezone.utc))
    (a.output/'scheduled-runs.json').write_text(json.dumps({'runs':runs,'assessment':result},indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
