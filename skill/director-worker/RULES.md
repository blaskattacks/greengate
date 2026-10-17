# Director and workers: the rules

One persistent **Director** session coordinates. Each package of work goes to a fresh **worker**. The **owner** (the
person) sets direction, rules on questions, and deploys. These rules are project-agnostic; a project adds its own
commands, ports and gates in its `CLAUDE.md` (see `templates/claude-md-snippet.md`).

Short version: *one package, one fresh worker, one branch. The worker tests and fixes its own work and hands back a
diff with a handoff block. The Director gates it, then accepts it or sends it back to the same worker. Three tries and
the worker stops with a post-mortem.*

## A. Issuing work

1. **One package, one fresh worker, one branch, one PR.** A fresh worker carries no history, so it costs less and
   cannot be confused by old context. The Director makes the branch or worktree first and names it in the brief.
2. **The brief is self-contained** (`templates/brief.md`): the goal, the **file manifest** (files it edits, files to
   read first, files it must not touch), the **targeted tests**, the gates, the branch, any ports or resources it
   may use, and these rules by reference. A worker should not need the Director's conversation to start.
3. **Read narrow.** Never read a file over about 1,000 lines whole: search it and read the ranges you need. Reading a
   small file outside the manifest is fine; **editing** outside the manifest is not: say so in the handoff and let
   the Director decide. *Context spent swallowing a file the task didn't need is context lost for reasoning.*
4. **Effort to match the risk.** High effort by default; maximum effort, plus an adversarial review by the Director,
   for packages where a wrong answer is expensive (data, geometry, money, security).

## B. The worker's loop (the "green gate")

5. **The worker tests its own work.** Targeted tests first (the ones the brief names, e.g. one test file), until
   green; then the full suite; then any slower gates the brief names. It fixes failures while the code is still in
   its context. *A fix by the worker that wrote it is cheap; a fresh agent spends its first hour rebuilding that
   context.*
6. **No review passes, audits or unasked refactors by workers.** The tests and gates are the worker's review. Review
   belongs to the Director.
7. **Commit small, push after every commit.** A machine can be wiped; a branch on the remote survives. Never
   force-push.
8. **Keep a worklog** on the branch (`templates/worklog.md`): Asked, Did, Measured, What broke, Left. It merges with
   the work, so the notes survive the worker.

## C. Handoff and the gate

9. **"Done" is a handoff block** (`templates/handoff.md`), at the top of the worklog and in the worker's last message:
   files changed, the command run, the output with counts, side effects for the next package, what is not done.
   Changes live as **commits on the branch**: the worker never pastes whole files back, and the Director reviews the
   diff (`git diff --stat`, then the diff), never re-reads whole files.
10. **The Director is the gatekeeper.** "Done" is a claim. The Director reruns the gates in its own tree, reviews the
    diff against the brief, then either accepts it and closes the worker, or sends the failing log and its findings
    back to **the same worker**, which fixes it on the same branch (a "Round 2" heading in the worklog). A worker
    never closes, merges or releases its own work.
11. **The cap.** Three tries at a targeted test that stays red, or three rounds sent back, and the worker stops. It
    writes a **post-mortem** (three sentences: what blocked it, what clashed, what it tried) and the raw failing
    output into its worklog, pushes, reports, and ends. It does not refactor its way out.
12. **After a stop, check the brief first.** A stuck worker is often a wrong brief. The Director corrects the brief,
    puts the post-mortem at its top, and starts a fresh worker (a debugging specialist when the brief was right).

## D. Merging and releasing

13. **Only the Director merges**, and only the owner deploys to production. Workers and cloud sessions never push to
    the main or release branches and never merge: they open a PR, mark the board, and stop.
14. **Every release** adds a change-history entry and refreshes the handoff file's top (where the project stands,
    what is next). A test can enforce it.

## E. Memory that outlives a context

15. **Intent and scope live in the repository** (`INTENT.md`: what the product is for, the owner's rules, each
    module's scope) so a small context does not lose the plot.
16. **Lessons.** After anything hard, an entry in `LESSONS.md` (`templates/lessons.md`): what was hard, how it was
    fixed, what to do better next time. Workers read it before they start.
17. **A work board** (`templates/board.md`) for sessions the Director cannot message directly (cloud, other tools):
    one row per package, `claimed / done: ready / needs work / stuck`. Finishing and marking the row is the alert.

## F. Safety and cost

18. **Never delete; quarantine.** Move what is marked for deletion to a dated holding folder.
19. **Secrets stay unseen.** Never print env files or keys; never store or repeat a key the owner pastes; use
    short-lived keys for quick checks. Tests never call paid or outside services: they use stand-ins.
20. **Customer data stays local** unless the owner rules otherwise for a named service and purpose.
21. **Limits go to the owner at once.** A worker that hits a usage or rate limit reports it; no silent switch to a
    different model.
22. **Keep the shared rules stable.** The rules file sits at the front of every session's context and is cached;
    edit it rarely and in batches, not a line at a time.
23. **Close workers when done.** Long-lived sessions only finish what they already hold; new work goes to a fresh
    worker.
