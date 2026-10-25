# Agent instructions

This repo holds the course's iterations (`docs/iterations/`). Students
don't work here: they work in their copy of
[my-factory-starter](https://github.com/lean-software-production/my-factory-starter),
whose `fetch-iteration` skill downloads each iteration from this repo's
`main` branch on GitHub.

The feature files are the students' test suite, and their step
definitions carry over between iterations. When you change a feature,
use the steps in `docs/iterations/STEPS.md` (add a new one there first)
and run `bin/step-drift` to check that each iteration's steps differ
from the last only where the meaning changed. A step says what a machine
does, never how a check makes it so: students write their own test
doubles ([ADR 0002](docs/adr/0002-students-write-their-own-test-doubles.md)),
and no feature names one.
