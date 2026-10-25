# Iterations

| Iteration | Spec |
|---|---|
| 001 | [Basic unvalidated loop](001-basic-unvalidated-loop/README.md) |
| 002 | [Checking the work](002-checking-the-work/README.md) |
| 003 | [Machine configuration](003-machine-configuration/README.md) |
| 004 | [The assembly line](004-assembly-line/README.md) |
| 005 | [Runs and targets](005-runs-and-targets/README.md) |
| 006 | [Fan out](006-fan-out/README.md) |
| 007 | [Watching](007-watching/README.md) |
| 008 | [Steering](008-steering/README.md) |

Your progress is kept in your starter repo (`factory/ITERATION`),
not here. `fetch-iteration` works through these in order.

## Spec structure

Each iteration folder holds the whole spec at that point, not just what's new:

- `README.md` — the homework framing: what's changing, what to watch for, and the CLI commands you should end up with. An optional `## Once your suite passes` section holds tasks to do after the acceptance suite passes. The starter's coaching and implementation skills offer to work through that section before marking the iteration Done; keep the heading exact. Course-specific tasks and report requirements belong in that section, not in the skills.
- `FACTORY.md` — a short summary of the factory at this point. The features win where they disagree.
- `spec.md` — the seed: the project the factory builds (when there is one).
- `features/*.feature` — the acceptance criteria, in Gherkin. They are also your factory's test suite.

[`STEPS.md`](STEPS.md) lists every step the features use. It is for
the course's authors, and `bin/step-drift` checks the features against it.

## Ground rules

These hold for every homework.

- The behaviour in `features/` is the spec. How you build it — language,
  shape, libraries — is up to you.
- The feature files are your factory's test suite. Pick a language with a
  Gherkin runner (cucumber-js, behave, godog, Cucumber for Ruby or the
  JVM, …), write the step definitions, and build the factory until the
  suite passes. Examples tagged `@real-agent` need a real agent and are
  left out of the everyday run; every other example runs with test
  doubles, which you write (homework 1 explains). A step keeps its words from one homework to the next unless
  its meaning changes, so your step definitions carry over, and what
  fails after a fetch is what is new.
- Your factory drives a real coding agent, and the agent does the work:
  the plans, the code and the verdicts. The plan belongs to the agents:
  the factory never reads it. Each machine answers with a result — a
  line of JSON describing the job it did — and the factory routes on
  the result's fields, never on the words. `pi` is the default; any coding
  agent will do. The factory writes none of the work itself and fakes
  none of it — `agent.feature`, and from homework 2 `machine.feature`, is
  how that is checked.
