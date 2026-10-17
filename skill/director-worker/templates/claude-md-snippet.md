<!-- Paste at the top of the project's CLAUDE.md, then fill in the project lines. -->

> **Workers and cloud sessions: never push to `main` or a release branch, never merge. Open a PR, mark your row on
> `docs/cloud/BOARD.md`, stop.** Rules: `docs/agents/RULES.md` (director-worker).

## Working as a worker
- You test your own work: the brief's targeted tests until green, then `<full test command>`, then its gates. Fix
  failures while the code is fresh.
- Say done with the handoff block (`docs/agents/templates/handoff.md`). If the Director sends it back, fix it on the
  same branch. Three tries at a red test and you stop with a post-mortem.
- Stay in the brief's file manifest. Never read a file over ~1,000 lines whole; search and read ranges.
- Push after every commit; never force-push. Keep `docs/worklog/<branch>.md`.

## This project
- Full tests: `<command>`. One file: `<command>`.
- Ports workers may use: `<ranges>`; never `<reserved>`.
- Stand-ins for outside services: `<env vars>`.
