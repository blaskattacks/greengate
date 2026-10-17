# green-gate

A portable rule set and Claude Code skill for running a software project with one persistent **Director** session
and fresh **engineer** agents (Claude Code subagents, cloud sessions, or other tools). Built on YardSister
(2026-10). Project-agnostic: each project adds its own commands, ports and gates.

The loop: one package, one fresh engineer, one branch. The Director writes the brief and its acceptance tests. The
engineer writes those tests first and watches them fail, builds in small green steps, answers the design checks, and
hands back commits plus a handoff block. The Director verifies in a fresh tree and merges, or sends the failure back
to the same engineer. Three failed attempts and the engineer stops with a post-mortem; the Director fixes the brief
before starting a fresh one.

## What is here

| Path | What |
|---|---|
| `green-gate/SKILL.md` | The skill: which file to read, set up a project, issue, gate, after a stop, deploys |
| `green-gate/references/ENGINEER.md` | The engineer's rules: one page, 16 rules (all an engineer reads) |
| `green-gate/references/DIRECTOR.md` | The Director's rules: 25, in six groups |
| `green-gate/assets/templates/` | brief, handoff, worklog, board, lessons, engineer prompt, CLAUDE.md snippet |
| `green-gate/assets/githooks/pre-push` | The guard: engineers can't push protected branches or force-push |
| `green-gate/scripts/setup_project.py` | Copies the rules into a project's `docs/agents/`, creates lessons/board/worklog |
| `green-gate/scripts/check_handoff.py` | Checks an engineer's handoff block is complete before gating |

## Use it

- **As a skill on this PC:** copy the `green-gate/` folder to `~/.claude/skills/green-gate/` (or install the
  packaged `green-gate.zip`). Then in any project: "set up green-gate here".
- **In a project's repo** (cloud sessions only see the repo): `python green-gate/scripts/setup_project.py <repo>
  --dry-run`, then without `--dry-run`; paste the CLAUDE.md snippet; commit.

## Changing the rules

Change them here first, then `setup_project.py <repo> --update` in each project. Keep edits rare and batched: the
rules sit at the front of every session's context, and each edit restarts its cache.
