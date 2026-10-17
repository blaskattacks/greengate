# <ID>: <one-line goal>

Branch `<work|cloud>/<name>`. Worklog `docs/worklog/<branch-with-dashes>.md`. Rules: `RULES.md` (director-worker).
<If this replaces a stopped worker: paste its post-mortem here, first.>

## Why
<Two or three lines: the problem, who hit it, what good looks like.>

## Files (the manifest)
- **Edit:** `path/a.js` (~line 120 `fnName`), `test/a.test.js`
- **Read first:** `path/b.js` (`otherFn` ~300), `docs/INTENT.md` rule N
- **Do not touch:** `path/c.js` (another worker is in it), `deploy/`

## Do
1. <Concrete step, with file:line pointers.>
2. <...>

## Tests
- **Targeted (green first):** `node --test test/a.test.js` — cases: <list>
- **Full suite (before done):** `npm test`, fail 0
- **Gates (if any):** <harness phases, replay>; ports `<range>` only

## Done
The handoff block (`templates/handoff.md`). Cap: three tries at a red targeted test, then stop with a post-mortem.
