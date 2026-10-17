#!/usr/bin/env python3
"""Set up the green-gate rules in a project repository.

Usage:
    setup_project.py <project-root> [--update] [--install-hook] [--dry-run]

Copies the skill's rules and templates into <project-root>/docs/agents/, creates docs/LESSONS.md,
docs/cloud/BOARD.md and docs/worklog/ when missing, and puts the pre-push guard at .githooks/pre-push.

  --update        overwrite docs/agents/ and .githooks/pre-push with the skill's current copies
                  (the project's LESSONS.md, BOARD.md and worklogs are never overwritten)
  --install-hook  also run `git config core.hooksPath .githooks` in the project
  --dry-run       say what would happen, change nothing

Nothing is ever removed. Prints the next steps (the CLAUDE.md snippet, the lesson ids).
"""

import shutil
import subprocess
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent


def main(argv):
    args = [a for a in argv if not a.startswith('--')]
    flags = {a for a in argv if a.startswith('--')}
    unknown = flags - {'--update', '--install-hook', '--dry-run'}
    if len(args) != 1 or unknown:
        print(__doc__)
        return 2
    root = Path(args[0]).resolve()
    if not (root / '.git').exists():
        print(f'Not a git repository: {root}')
        return 1
    update, dry = '--update' in flags, '--dry-run' in flags
    done = []

    def put(src, dst, overwrite, lf=False):
        if dst.exists() and not overwrite:
            done.append(f'kept     {dst.relative_to(root)} (exists)')
            return
        done.append(f'{"update" if dst.exists() else "create"}   {dst.relative_to(root)}')
        if dry:
            return
        dst.parent.mkdir(parents=True, exist_ok=True)
        if lf:
            dst.write_bytes(src.read_bytes().replace(b'\r\n', b'\n'))
        else:
            shutil.copyfile(src, dst)

    agents = root / 'docs' / 'agents'
    put(SKILL / 'references' / 'ENGINEER.md', agents / 'ENGINEER.md', update)
    put(SKILL / 'references' / 'DIRECTOR.md', agents / 'DIRECTOR.md', update)
    for t in sorted((SKILL / 'assets' / 'templates').glob('*.md')):
        put(t, agents / 'templates' / t.name, update)
    put(SKILL / 'assets' / 'githooks' / 'pre-push', root / '.githooks' / 'pre-push', update, lf=True)

    templates = SKILL / 'assets' / 'templates'
    put(templates / 'lessons.md', root / 'docs' / 'LESSONS.md', False)
    put(templates / 'board.md', root / 'docs' / 'cloud' / 'BOARD.md', False)
    keep = root / 'docs' / 'worklog' / '.gitkeep'
    if not (root / 'docs' / 'worklog').exists():
        done.append('create   docs/worklog/')
        if not dry:
            keep.parent.mkdir(parents=True, exist_ok=True)
            keep.write_text('')

    if '--install-hook' in flags:
        done.append('run      git config core.hooksPath .githooks')
        if not dry:
            subprocess.run(['git', '-C', str(root), 'config', 'core.hooksPath', '.githooks'], check=True)

    print('\n'.join(done))
    print('\nNext:')
    print('1. Paste docs/agents/templates/claude-md-snippet.md at the top of CLAUDE.md; fill in its project lines.')
    print('2. If LESSONS.md already had entries, give each an id L-<AREA>-NN and add the index (templates/lessons.md).')
    if '--install-hook' not in flags:
        print('3. Install the guard: git config core.hooksPath .githooks (or rerun with --install-hook).')
    print('4. Commit on a branch, gate it, merge. Push your own merges with GREEN_GATE_DIRECTOR=1.')
    print('5. Turn on branch protection for main where the host allows: cloud sessions never run local hooks.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
