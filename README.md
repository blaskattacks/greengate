# director-worker

A portable rule set for running a software project with one persistent **Director** session and fresh **worker**
agents (Claude Code subagents, cloud sessions, or other tools), built on YardSister (2026-10). Project-agnostic: the
project adds its own commands, ports and gates.

The core loop (the "green gate"): one package, one fresh worker, one branch. The worker tests and fixes its own work
(targeted tests first, then the full suite) and hands back commits plus a handoff block. The Director gates it and
accepts it or sends it back to the same worker. Three tries and the worker stops with a post-mortem; the Director
checks the brief before starting a fresh one.

## What is here

| Path | What |
|---|---|
| `skill/director-worker/SKILL.md` | The Claude Code skill: the Director's steps (set up, issue, gate, after a stop) |
| `skill/director-worker/RULES.md` | The rules, 23 of them, in six groups |
| `skill/director-worker/templates/` | brief, handoff, worklog, board, lessons, worker prompt, CLAUDE.md snippet |

## Use it

- **As a skill, in every project on this PC:** copy `skill/director-worker` to `~/.claude/skills/director-worker`.
  Then in any project: "set up director-worker here".
- **In a project's repo** (needed for cloud sessions, which only see the repo): copy `RULES.md` and `templates/`
  to `docs/agents/`, and paste `templates/claude-md-snippet.md` into the project's `CLAUDE.md`.

## Changing the rules

Change them here first, then copy into each project. Keep edits rare and batched: the rules sit at the front of
every session's context, and each edit restarts its cache.
