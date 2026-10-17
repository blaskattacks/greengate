### Done: <package> (<branch>)
- Files changed: `src/lib/x.js`, `test/x.test.js`
- Command: `npm test` (and any targeted tests, phases or replay run)
- Output: 2410 tests, 2404 pass, 0 fail, 6 skipped
- Side effects: what the next package must know (a new export, a field, a changed message), or "none"
- Traps avoided: how, for each trap the brief listed, or "none listed"
- Not done: what could not be run or finished, or "nothing"

<!-- If stopped at the cap, replace "Done" with "Stopped" and add:
### Post-mortem
Blocked by: <one sentence>. Clashed with: <one sentence>. Tried: <one sentence>.
Raw failing output: below, or the log path. -->
