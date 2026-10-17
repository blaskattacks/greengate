---
name: green-gate
description: This skill should be used when running a software project as a Director that hands packages of work to fresh engineer agents (subagents, cloud sessions, other tools) and gates their work before merging. It covers setting the rules up in a project, writing a brief, issuing a package, gating an engineer's "done" (fresh-tree verify, design-check review), sending failures back to the same engineer, handling an engineer that hit its three-attempt cap, and merging. It also applies when acting as an engineer under these rules.
---

# Green gate

One persistent **Director** plans, issues, gates and merges. Each package goes to a fresh **engineer** that builds
it, tests and fixes its own work, and hands back commits plus a handoff block. The Director verifies in a fresh tree
and either merges or sends the failure back to the same engineer. Three failed attempts and the engineer stops with a
post-mortem; the Director fixes the brief before starting a fresh one. The owner (the person) rules on questions
and asks for deploys.

## Which file to read

- **Acting as the Director:** read `references/DIRECTOR.md` once per session (25 rules). Hold engineers to
  `references/ENGINEER.md`.
- **Acting as an engineer:** read only `references/ENGINEER.md` (one page), the brief, the `LESSONS.md` index and
  the lesson ids the brief names. Do not load `DIRECTOR.md`.
- In a project already set up, the same files live at `docs/agents/`; prefer the project's copies.

## Set up a project (once)

1. Run `scripts/setup_project.py <project-root> --dry-run`, check the list, then run it without `--dry-run`
   (add `--install-hook` to set `core.hooksPath`). It copies the rules and templates to `docs/agents/`, creates
   `docs/LESSONS.md`, `docs/cloud/BOARD.md` and `docs/worklog/` when missing, and puts the pre-push guard at
   `.githooks/pre-push`. It never overwrites the project's own lessons, board or worklogs.
2. Paste `docs/agents/templates/claude-md-snippet.md` at the top of the project's `CLAUDE.md`; fill in the project
   lines (test commands, ports, stand-ins, what ships, the quarantine folder).
3. Give existing lessons ids (`L-<AREA>-NN`) and an index (`assets/templates/lessons.md`).
4. Commit on a branch, gate it, merge, push with `GREEN_GATE_DIRECTOR=1`. Suggest branch protection for `main` to
   the owner where the host allows it: cloud sessions never run local hooks.

To refresh a project after the rules change, rerun the script with `--update`.

## Issue a package

1. Cut it to one area, about one session's work, under ~10 files. Make the branch and worktree; check nobody has the
   branch and no open package holds the files.
2. Write the brief from `assets/templates/brief.md`: the manifest, the pattern to follow, the lesson ids, the
   acceptance tests (written or named by case now), the gates and ports. For a risky package (money, data, safety,
   privacy, geometry, anything the owner flags): "plan first" and two or three traps.
3. Check the brief: grep every file, function and line pointer it names; ask of each acceptance test whether it could
   fail.
4. Start a fresh engineer in the background with `assets/templates/engineer-prompt.md`. Answer its plan or questions
   promptly.

## Gate a "done"

1. Run `scripts/check_handoff.py <worklog>`. Incomplete → send it back for the missing lines.
2. Make a fresh worktree at the PR's commit merged onto `main`; empty data, own ports. Never clean an existing tree.
3. Run `git diff --stat`, the acceptance tests, the full suite, the gates. Review the diff through the design-check
   lenses (wrong client, old client and old data, change mid-run, the edges, what ships, the traps) plus
   regressions. For a risky package, hand the review to a fresh read-only reviewer agent with those lenses.
4. Pass → merge with `--no-ff`, push `main` (`GREEN_GATE_DIRECTOR=1`), fold the worklog's proposals into the
   changelog, `LESSONS.md` and the open questions, close the engineer, record the rounds. Fail → send the log and
   findings to the **same** engineer as "Round N".

## An engineer stops

1. Read its post-mortem and raw output. Ask first whether the brief was wrong (file, assumption, dependency); fix it.
2. Start a fresh engineer with the corrected brief and the post-mortem at its top; a debugging specialist when the
   brief was right.
3. Add a `LESSONS.md` entry with a new id and an index line when it was hard.

## Deploys

Deploy production only when the owner asks; one request covers one deploy.
