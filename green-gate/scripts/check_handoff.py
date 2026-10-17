#!/usr/bin/env python3
"""Check an engineer's handoff block before gating it.

Usage:
    check_handoff.py <worklog.md>

Finds the "### Done:" (or "### Stopped:") block and checks that it has every line the template asks for:
files, commands, output with counts, the six design checks answered, side effects, not done, rounds; a stopped
block also needs its post-mortem. Exit 0 when complete; 1 with the list of what is missing.
"""

import re
import sys
from pathlib import Path

LINES = ['Files changed', 'Commands', 'Output', 'Design checks', 'Side effects', 'Not done', 'Rounds']
CHECKS = ['Wrong client', 'Old client, old data', 'Change mid-run', 'The edges', 'What ships', 'Traps']
POST = ['Blocked by', 'Clashed with', 'Tried']


def value(block, label):
    """The text after '- Label:' (a note in brackets after the label is allowed, e.g. 'Files changed (Round 2):').
    When the line itself is empty, the indented lines under it are the value."""
    m = re.search(r'^(\s*)-\s*(?:\*\*)?' + re.escape(label) + r'(?:\*\*)?(?:\s*\([^)]*\))?\s*:(?:\*\*)?[ \t]*(.*)$',
                  block, re.M)
    if m is None:
        return None
    if m.group(2).strip():
        return m.group(2).strip()
    indent, under = len(m.group(1)), []
    for line in block[m.end():].splitlines()[1:]:
        if not line.strip():
            continue
        if len(line) - len(line.lstrip()) <= indent:
            break
        under.append(line.strip())
    return ' '.join(under)


def answered(v):
    return v is not None and v != '' and not v.startswith('<')  # a template placeholder starts with <; a value may hold <path>


def check(text):
    m = re.search(r'^###\s+(Done|Stopped):.*?(?=^#{1,3}\s(?!Post-mortem)|\Z)', text, re.M | re.S)
    if not m:
        return ['no "### Done:" or "### Stopped:" block']
    block, kind = m.group(0), m.group(1)
    missing = []
    for label in LINES:
        v = value(block, label)
        if v is None:
            missing.append(f'line "{label}"')
        elif label != 'Design checks' and not answered(v):
            missing.append(f'"{label}" not filled in')
    out = value(block, 'Output') or ''
    if not re.search(r'\d', out) or 'fail' not in out.lower():
        missing.append('"Output" needs counts, including fail')
    rounds = value(block, 'Rounds') or ''
    if not re.match(r'^\d+', rounds):
        missing.append('"Rounds" needs a number')
    for c in CHECKS:
        if not answered(value(block, c)):
            missing.append(f'design check "{c}" not answered (n/a is an answer)')
    if kind == 'Stopped':
        pm = re.search(r'^###\s+Post-mortem(.*?)(?=^#{1,3}\s|\Z)', text, re.M | re.S)
        body = pm.group(1) if pm else ''
        for p in POST:
            if p.lower() not in body.lower():
                missing.append(f'post-mortem "{p}"')
    return missing


def main(argv):
    if len(argv) != 1:
        print(__doc__)
        return 2
    path = Path(argv[0])
    if not path.exists():
        print(f'No such file: {path}')
        return 1
    missing = check(path.read_text(encoding='utf-8'))
    if missing:
        print(f'{path}: the handoff is not complete:')
        for x in missing:
            print(f'  - {x}')
        return 1
    print(f'{path}: the handoff is complete.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
