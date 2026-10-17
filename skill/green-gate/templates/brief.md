# <ID>: <one-line goal>

Branch `<work|cloud>/<name>`. Worklog `docs/worklog/<branch-with-dashes>.md`. Rules: `DIRECTOR.md` (green-gate).
<If this replaces a stopped engineer: paste its post-mortem here, first.>

## Why
<Two or three lines: the problem, who hit it, what good looks like.>

## Files (the manifest)
- **Edit:** `path/a.js` (~line 120 `fnName`), `test/a.test.js`
- **Read first:** `path/b.js` (`otherFn` ~300), `docs/INTENT.md` rule N
- **Do not touch:** `path/c.js` (another engineer is in it), `deploy/`

## Do
1. <Concrete step, with file:line pointers.>
2. <...>

## Lessons to read
<ids from the LESSONS.md index: L-MAP-04, L-PLANS-11, or "none">

## Traps (risky packages only)
<Two or three ways the tests could pass without the work being right; the handoff says how each was avoided.>

## Tests
- **Targeted (green first):** `node --test test/a.test.js` — cases: <list>
- **Full suite (before done):** `npm test`, fail 0
- **Gates (if any):** <harness phases, replay>; ports `<range>` only

## Done
The handoff block (`templates/handoff.md`). Cap: three fix attempts at the same failing test, or three rounds sent back, then stop with a post-mortem (`ENGINEER.md` rule 9).
