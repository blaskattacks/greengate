# <ID>: <one-line goal>

Branch `<work|cloud>/<name>`. Worklog `docs/worklog/<branch-with-dashes>.md`. Rules: `docs/agents/ENGINEER.md`.
Risk: <normal | risky: plan first>.
<If this replaces a stopped engineer: its post-mortem here, first.>

## Why
<Two or three lines: the problem, who hit it, what good looks like.>

## Files (the manifest)
- **Edit:** `path/a.js` (~line 120 `fnName`), `test/a.test.js`
- **Read first:** `path/b.js` (`otherFn` ~300), `docs/INTENT.md` rule N
- **Do not touch:** `path/c.js` (another engineer holds it), `deploy/`
- **Pattern to follow:** <an existing feature of the same shape: "the way `/evidence` is added in server.js ~4100">

## Lessons to read
<ids from the LESSONS.md index, or none>

## Do
1. <Concrete step, with file:line pointers.>
2. <...>

## Acceptance tests (written or named before the engineer starts; never weakened)
- `test/a.test.js`: <case>; <case>; <case at the edge>
- Old data: <a record from before this change>

## Traps (risky packages)
- <A way the tests could pass without the work being right.>

## Gates
- Full suite: `<command>`, fail 0. Slower gates: <phases, replay>. Ports `<range>` only.

## Done
The handoff block (`docs/agents/templates/handoff.md`). Cap: `ENGINEER.md` rule 15.
