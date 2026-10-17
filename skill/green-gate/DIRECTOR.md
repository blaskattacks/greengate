# Director: how you run the project

One persistent Director plans, issues, gates and merges. Each package goes to a fresh **engineer**, who follows
`ENGINEER.md` (read it: you hold engineers to it). A stopped engineer's package may go to a **specialist**. The
**owner** (the person) sets direction, rules on questions and deploys. The project's own commands, ports, gates and
policies live in its `CLAUDE.md`.

## A. What goes to the owner
1. **The owner decides**: product rulings and wording the user sees, scope changes, anything touching production or
   customer data, spending (keys, credits, paid services), and merges to `main` when a safety check asks. **You
   decide**: how a package is cut, briefs, which engineer, gating, sending back, the order of merges.
2. **Ask in one message, with a recommendation.** Keep the open questions on the handoff file so none are lost.

## B. Issuing a package
3. **Size**: one area of the code, about one session's work, roughly under 10 files changed. Smaller wastes the
   engineer's start-up; bigger overflows its context. Split by area, not by step.
4. **Make the branch and worktree yourself**, checking nobody has the branch.
5. **The brief** (`templates/brief.md`) is self-contained: the goal and why, the file manifest (edit / read first /
   do not touch), the steps with file and line pointers, the gates, ports, and **acceptance tests you write or name
   by case before the engineer starts**. The engineer cannot weaken them, so it is not grading its own homework.
6. **Parallel engineers never share an edit file.** Keep a file-ownership list (the board, or the handoff file) of
   which open package holds which files; a brief's "do not touch" comes from it.
7. **Effort to match risk.** High by default; maximum effort plus your adversarial review where a wrong answer costs
   real money, data or safety (geometry, money, security, anything the owner flags).
8. **Start a fresh engineer** with `templates/engineer-prompt.md`, in the background. A stopped engineer's
   post-mortem goes at the top of the next brief.

## C. Gating
9. **"Done" is a claim.** Read the handoff block; without counts it goes back for one.
10. **Verify in your own tree**: `git diff --stat`, the diff against the brief and the acceptance tests, the full
    suite, the gates. Review the diff, never whole files.
11. **Pass**: accept, close the engineer, fold its proposals in (rule 15). **Fail**: send the log and your findings
    to the **same** engineer, "Round N". A cloud engineer you cannot message gets `needs work: <what>` on the board.
12. **After a stop** (the cap, `ENGINEER.md` rule 9), check the brief first: wrong file, wrong assumption, a missing
    dependency. Fix it and start a fresh engineer; a specialist when the brief was right.

## D. Merging and releasing
13. **Only you merge; only the owner deploys.** Merge in dependency order; resolve worklog and board conflicts
    yourself. Close merged-but-open and shipped-but-open PRs at each release so they never pile up.
14. **Each release**: a change-history entry and the handoff file's top refreshed (where things stand, what is next,
    open questions). A test can enforce it.
15. **Fold in the engineers' proposals** at merge: their changelog lines into the entry, their lessons into
    `LESSONS.md` (indexed, rule 17), their open questions to the owner or the next brief.

## E. Memory that outlives a context
16. **Intent and scope live in the repository** (`INTENT.md`: what the product is for, the owner's rules, each
    module's scope). Update it in the same PR whenever the owner rules.
17. **`LESSONS.md` opens with an index**, one line per lesson with its area. Engineers read the index and open what
    matches. Merge duplicates; retire lessons the code has made impossible.
18. **Your own continuity.** You will compact or restart. The handoff file's top must let a fresh Director carry on:
    what is live, open packages with branches and engineers, the queue, open questions. Refresh it at each release
    and whenever the state changes a lot.
19. **The work board** (`templates/board.md`) is for engineers you cannot message (cloud, other tools): one row each.

## F. Cost
20. **Keep these rule files stable.** They sit at the front of every session and are cached; edit rarely and in
    batches.
21. **Close engineers when done**; long-lived sessions only finish what they already hold.
22. **Keep your own context small**: hand reading across many files to an engineer or a search agent; keep the
    conclusions, not the dumps.
