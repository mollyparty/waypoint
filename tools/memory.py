"""Waypoint memory checks. Version-Timestamp: 2026-09-05 18:00:00 UTC-4."""
import argparse
import hashlib
import html
import json
import os
from pathlib import Path
import re
import socket
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
CHECKPOINT = 'vault/01-Project/CURRENT-WORK.json'
BASELINE = 'graphify-out/source-baseline.json'


def run(*args):
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, timeout=90)


def git(*args):
    result = run('git', *args)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result.stdout.strip()


def stamp():
    return datetime.now(timezone.utc).isoformat()


def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def save(path, value):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + '.tmp')
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    temporary.replace(target)


def sources():
    paths = [p for p in ROOT.rglob('*.md') if '.git' not in p.parts
             and 'graphify-out' not in p.parts and '.obsidian' not in p.parts
             and '_templates' not in p.parts]
    paths += [ROOT / 'catalog/features.json', ROOT / CHECKPOINT, ROOT / 'graphify-out/graph.json']
    return {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes().replace(b'\r\n', b'\n')).hexdigest()
            for p in sorted(paths) if p.is_file()}


def check():
    errors, warnings = [], []
    checkpoint = read(CHECKPOINT)
    for field in ('Version-Timestamp', 'objective', 'phase', 'status', 'next_action', 'evidence', 'pending_decisions'):
        if field not in checkpoint or checkpoint[field] in ('', None):
            errors.append('Checkpoint missing ' + field)
    for path in checkpoint.get('evidence', []):
        if not (ROOT / path).is_file():
            errors.append('Missing checkpoint evidence: ' + path)
    graph = read('graphify-out/graph.json')
    ids = [n['id'] for n in graph['nodes']]
    if len(ids) != len(set(ids)):
        errors.append('Duplicate graph node identifiers')
    ids = set(ids)
    for edge in graph['links']:
        if edge['source'] not in ids or edge['target'] not in ids:
            errors.append('Dangling graph edge: ' + str(edge))
    missing = sorted({n.get('source_file') for n in graph['nodes'] if n.get('source_file')
                      and not (ROOT / n['source_file']).is_file()})
    warnings.extend('Legacy graph source missing: ' + path for path in missing)
    warnings.append('Legacy semantic claims require source verification; hashes measure drift only.')
    actual = sources()
    if (ROOT / BASELINE).exists():
        previous = read(BASELINE)['sources']
        drift = sorted(p for p in actual.keys() | previous.keys() if actual.get(p) != previous.get(p))
        if drift:
            errors.append('Sources changed since graph review baseline: ' + ', '.join(drift))
    else:
        errors.append('Graph source baseline missing')
    result = run(sys.executable, 'catalog/build.py', '--check')
    if result.returncode:
        errors.append('Catalog: ' + result.stderr.strip())
    return {'Version-Timestamp': stamp(), 'errors': errors, 'warnings': warnings,
            'checkpoint': checkpoint, 'graph': {'nodes': len(ids), 'links': len(graph['links'])}}


def staged():
    files = git('diff', '--cached', '--name-only', '-z').split('\0')
    files = [p for p in files if p]
    if not files:
        raise RuntimeError('No staged files')
    forbidden = [p for p in files if any(part == '.env' or part.startswith('.env.')
                 or part in ('.vercel', 'credentials.json') or part.endswith('.pem') for part in Path(p).parts)]
    if forbidden:
        raise RuntimeError('Sensitive paths staged: ' + ', '.join(forbidden))
    if not any(p.startswith('vault/03-Sessions/') and p.endswith('.md') for p in files):
        raise RuntimeError('Stage a session checkpoint with this meaningful unit of work')
    for required in (CHECKPOINT, 'vault/00-START-HERE.md'):
        if required not in files:
            raise RuntimeError('Stage the updated checkpoint: ' + required)
    # Prevent checks against working files that differ from the staged versions.
    dirty = set(git('diff', '--name-only', '-z').split('\0'))
    if dirty.intersection(files):
        raise RuntimeError('Staged files have further unstaged edits: ' + ', '.join(sorted(dirty.intersection(files))))
    checked_paths = set(sources()) | {'catalog/build.py', 'blueprint/index.html', 'tools/memory.py', BASELINE}
    if dirty.intersection(checked_paths):
        raise RuntimeError('Validation inputs have unstaged changes: ' + ', '.join(sorted(dirty.intersection(checked_paths))))
    git('diff', '--cached', '--check')
    state = check()
    if state['errors']:
        raise RuntimeError('\n'.join(state['errors']))
    print('Staged checkpoint checks passed')


def report(remote=False):
    state = check()
    state['branch'] = git('branch', '--show-current')
    state['head'] = git('rev-parse', 'HEAD')
    state['working_changes'] = git('status', '--short')
    state['remote_verification'] = 'Not checked. Run report --remote for live verification.'
    if remote:
        remote_line = git('ls-remote', 'origin', 'refs/heads/' + state['branch'])
        remote_sha = remote_line.split()[0] if remote_line else None
        state['remote_verification'] = 'Verified: remote matches HEAD' if remote_sha == state['head'] else 'Remote differs from local HEAD'
    save('memory/status.json', state)
    esc = html.escape
    items = ''.join('<li>' + esc(s) + '</li>' for s in state['errors'] + state['warnings'])
    content = f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Waypoint memory health</title><style>body{{font:18px/1.65 system-ui;max-width:850px;margin:40px auto;padding:24px;background:#f5f7fa;color:#172b3a}}section{{background:white;border:1px solid #bccbd5;border-radius:12px;padding:24px;margin:20px 0}}h1,h2{{line-height:1.2}}code{{overflow-wrap:anywhere}}a{{color:#075b9a}}</style>
<a href="index.html">Memory workflow</a><h1>Waypoint memory health</h1><p>Snapshot: {esc(state['Version-Timestamp'])}. Refresh with <code>python tools/memory.py report --remote</code>.</p>
<section><h2>Where we are</h2><p>{esc(state['checkpoint']['phase'])}</p><p><strong>Next:</strong> {esc(state['checkpoint']['next_action'])}</p></section>
<section><h2>Backup status</h2><p>{esc(state['remote_verification'])}</p><code>{esc(state['head'])}</code><p>{'Local changes remain outside the commit.' if state['working_changes'] else 'Working tree clean.'}</p></section>
<section><h2>Memory checks</h2><p>{len(state['errors'])} errors. {state['graph']['nodes']} nodes, {state['graph']['links']} links.</p><ul>{items}</ul></section></html>'''
    (ROOT / 'memory/status.html').write_text(content, encoding='utf-8')
    print(json.dumps(state, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['check', 'baseline', 'staged', 'install', 'publish', 'report'])
    parser.add_argument('--message')
    parser.add_argument('--remote', action='store_true')
    parser.add_argument('--tool', default='unknown', help='Actual calling IDE/tool for commit attribution')
    parser.add_argument('--tool-version', default='unknown')
    args = parser.parse_args()
    if args.action == 'baseline':
        save(BASELINE, {'Version-Timestamp': stamp(), 'meaning': 'Source drift baseline; not semantic certification', 'sources': sources()})
        print('Recorded source baseline. Semantic review remains the orchestrator responsibility.')
    elif args.action == 'install':
        previous = run('git', 'config', '--local', '--get', 'core.hooksPath')
        print('Previous hooksPath: ' + (previous.stdout.strip() or '(unset)'))
        git('config', '--local', 'core.hooksPath', '.githooks')
        for hook in (ROOT / '.githooks').iterdir():
            hook.chmod(hook.stat().st_mode | 0o111)
        print('Installed tracked hooks. Existing .git/hooks files preserved.')
    elif args.action == 'staged':
        staged()
    elif args.action == 'publish':
        if not args.message or not re.match(r'^(feat|fix|docs|chore|test|refactor|build|ci)(\([^)]+\))?: .+', args.message):
            raise RuntimeError('Supply --message with a Conventional Commit summary')
        branch = git('branch', '--show-current')
        if not branch:
            raise RuntimeError('Detached HEAD: select a work branch first')
        staged()
        if any('\n' in value or '\r' in value for value in (args.tool, args.tool_version)):
            raise RuntimeError('Tool attribution must be single-line')
        footer = f'Agent-Attribution: computer={socket.gethostname()}; tool={args.tool}; version={args.tool_version}; timestamp={stamp()}'
        print(git('commit', '-m', args.message, '-m', footer))
        print(git('push', '-u', 'origin', branch))
        head = git('rev-parse', 'HEAD')
        remote = git('ls-remote', 'origin', 'refs/heads/' + branch).split()
        if not remote or remote[0] != head:
            raise RuntimeError('Remote commit does not match HEAD after push')
        print('Verified pushed checkpoint: ' + head)
    elif args.action == 'report':
        report(args.remote)
    else:
        state = check()
        print(json.dumps(state, indent=2))
        return bool(state['errors'])
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.TimeoutExpired) as exc:
        print('Memory workflow failed: ' + str(exc), file=sys.stderr)
        sys.exit(1)
