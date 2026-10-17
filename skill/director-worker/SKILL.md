---
name: director-worker
description: Run a project as a Director with fresh worker agents (the green gate). Use when issuing a package of work to a subagent or cloud session, gating a worker's "done", sending a failure back, handling a worker that hit its cap, or setting these rules up in a new project.
---

# Director and workers

The rules are in `RULES.md` beside this file; the templates in `templates/`. Read `RULES.md` once per session.

## Set up a project (once)
1. Copy `RULES.md` and `templates/` into the project as `docs/agents/` (cloud sessions can only read the repo).
2. Paste `templates/claude-md-snippet.md` at the top of the project's `CLAUDE.md` and fill in its project lines.
3. Create `docs/LESSONS.md`, `docs/cloud/BOARD.md`, `docs/worklog/` from the templates; an `INTENT.md` if missing.
4. Open a PR; the owner merges.

## Issue a package
1. Make the branch and worktree yourself; check nobody has the branch.
2. Write the brief from `templates/brief.md`: the file manifest (edit / read first / do not touch), the targeted
   tests, the gates, ports. Paste a stopped worker's post-mortem at its top.
3. Start a **fresh** worker with `templates/worker-prompt.md`, in the background. One package per worker.

## Gate a "done"
1. Read the handoff block. Missing or without counts → send it back for one.
2. In your own tree: `git diff --stat`, the diff against the brief, the full suite, the gates. Never re-read whole files.
3. Pass → accept (PR ready to merge), close the worker, next package. Fail → send the log and findings to the
   **same** worker (SendMessage), "Round N". Count rounds.

## A worker stops (cap: three tries or three rounds)
1. Read its post-mortem and raw output. Ask first: was the brief wrong (wrong file, wrong assumption, missing
   dependency)? Fix the brief.
2. Start a fresh worker with the corrected brief and the post-mortem at its top; a debugging specialist when the
   brief was right.
3. If it was hard, add a `LESSONS.md` entry.
