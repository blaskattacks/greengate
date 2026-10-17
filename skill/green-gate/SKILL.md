---
name: green-gate
description: Run a project as a Director with fresh engineer agents (the green gate). Use when issuing a package of work to a subagent or cloud session, gating an engineer's "done", sending a failure back, handling an engineer that hit its cap, or setting these rules up in a new project.
---

# Director and engineers

The rules are in `DIRECTOR.md` beside this file; the templates in `templates/`. Read `DIRECTOR.md` once per session; engineers read only `ENGINEER.md`.

## Set up a project (once)
1. Copy `DIRECTOR.md`, `ENGINEER.md` and `templates/` into the project as `docs/agents/` (cloud sessions can only
   read the repo).
2. Paste `templates/claude-md-snippet.md` at the top of the project's `CLAUDE.md` and fill in its project lines.
3. Create `docs/LESSONS.md`, `docs/cloud/BOARD.md`, `docs/worklog/` from the templates; an `INTENT.md` if missing.
4. Install the guard: copy `templates/githooks/pre-push` to `.githooks/pre-push` (LF line endings), commit it,
   run `git config core.hooksPath .githooks`. Push your own merges with `GREEN_GATE_DIRECTOR=1`. Turn on GitHub
   branch protection for `main` where the plan allows: cloud sessions never run local hooks.
5. Give existing lessons ids and an index (`templates/lessons.md`).
6. Commit on a branch, gate it, merge and push it yourself (`DIRECTOR.md` rule 13).

## Issue a package
1. Make the branch and worktree yourself; check nobody has the branch.
2. Write the brief from `templates/brief.md`: the file manifest (edit / read first / do not touch), the targeted
   tests, the gates, ports. Write or name the **acceptance tests** before it starts; name the lesson ids to read;
   for a risky package list two or three **traps**. Paste a stopped engineer's post-mortem at its top.
3. Start a **fresh** engineer with `templates/engineer-prompt.md`, in the background. One package per engineer.

## Gate a "done"
1. Read the handoff block. Missing or without counts → send it back for one.
2. In a **fresh worktree at the PR's exact commit** (merged onto main), empty data, your own ports: `git diff --stat`,
   the diff against the brief and its traps, the acceptance tests, the full suite, the gates. Never re-read whole
   files; never clean an existing tree.
3. Pass → merge and push main yourself (`GREEN_GATE_DIRECTOR=1`), fold in the worklog's proposals (changelog,
   lessons, questions), close the engineer, next package. Fail → send the log and findings to the
   **same** engineer (SendMessage), "Round N". Count rounds.

## An engineer stops (cap: three tries or three rounds)
1. Read its post-mortem and raw output. Ask first: was the brief wrong (wrong file, wrong assumption, missing
   dependency)? Fix the brief.
2. Start a fresh engineer with the corrected brief and the post-mortem at its top; a debugging specialist when the
   brief was right.
3. If it was hard, add a `LESSONS.md` entry with a new id and an index line.
