### Done: <package> (<branch>)
- Files changed: `src/lib/x.js`, `test/x.test.js`
- Commands: `npm test` (and the acceptance tests, phases or replay run)
- Output: 2410 tests, 2404 pass, 0 fail, 6 skipped
- Red first: each acceptance test and where it failed before the code (a run log or a commit), or n/a with why
- Design checks:
  - Wrong client: <one line, or n/a>
  - Old client, old data: <one line, or n/a>
  - Change mid-run: <one line, or n/a>
  - The edges: <one line, or n/a>
  - What ships: <one line, or n/a>
  - Traps: <how each listed trap was avoided, or none listed>
- Side effects: what the next package must know (a new export, a field, a changed message), or none
- Not done: what could not be run or finished, or nothing
- Rounds: 1

<!-- Stopped at the cap: replace "Done" with "Stopped" and add
### Post-mortem
Blocked by: <one sentence>. Clashed with: <one sentence>. Tried: <one sentence>.
Raw failing output: <log path>. -->
