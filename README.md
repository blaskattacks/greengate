# green-gate

A portable rule set for running a software project with one persistent **Director** session and fresh **engineer**
agents (Claude Code subagents, cloud sessions, or other tools), built on YardSister (2026-10). Project-agnostic: the
project adds its own commands, ports and gates.

The core loop (the "green gate"): one package, one fresh engineer, one branch. The engineer tests and fixes its own work
(targeted tests first, then the full suite) and hands back commits plus a handoff block. The Director gates it and
accepts it or sends it back to the same engineer. Three tries and the engineer stops with a post-mortem; the Director
checks the brief before starting a fresh one.

## What is here

| Path | What |
|---|---|
| `skill/green-gate/SKILL.md` | The Claude Code skill: the Director's steps (set up, issue, gate, after a stop) |
| `skill/green-gate/DIRECTOR.md` | The rules, 23 of them, in six groups |
| `skill/green-gate/templates/` | brief, handoff, worklog, board, lessons, engineer prompt, CLAUDE.md snippet |

## Use it

- **As a skill, in every project on this PC:** copy `skill/green-gate` to `~/.claude/skills/green-gate`.
  Then in any project: "set up green-gate here".
- **In a project's repo** (needed for cloud sessions, which only see the repo): copy `DIRECTOR.md` and `templates/`
  to `docs/agents/`, and paste `templates/claude-md-snippet.md` into the project's `CLAUDE.md`.

## Changing the rules

Change them here first, then copy into each project. Keep edits rare and batched: the rules sit at the front of
every session's context, and each edit restarts its cache.
