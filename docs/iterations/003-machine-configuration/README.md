# Homework 3 — Machine configuration

Read `FACTORY.md`, then the feature files in `features/`. Together they
are the whole spec of the factory at this point, not just the new parts.

The factory does the same work it did for homework 2. What changes is
where each machine's instructions live. Until now your planner's, doer's
and validator's prompts were in your factory's code, and one harness ran
all three, chosen for the run. This homework moves each machine out of
your code and into a folder of its own, in your factory's folder:
`machines/<name>/`.

A machine's folder holds two things:

- **`AGENTS.md`** — the machine's instructions: what it is for, how it
  does its job, and anything it should bring to the work, such as the
  validator's lens. `AGENTS.md` is a convention most coding agents
  already read, so the same file serves whichever harness runs the
  machine.
- **The rest of its configuration** — the harness that runs it (`pi`,
  unless it names another) and whatever that harness needs, such as its
  model. The file's name and format are your choice.

The factory gives each machine its own `AGENTS.md`, and no other
machine's. Change a machine's `AGENTS.md`, and the machine changes, with
no change to your code.

## What your factory's folder looks like

The format of the configuration file is yours; `machine.json` is only an
example:

```text
factory/
  machines/
    planner/
      AGENTS.md
      machine.json      {"harness": "pi", "model": "<a model>"}
    doer/
      AGENTS.md
      machine.json      {"harness": "pi", "model": "<a model>"}
    validator/
      AGENTS.md
      machine.json      {"harness": "pi", "model": "<another model>"}
```

A validator's `AGENTS.md` might read:

```markdown
# Validator

You check the doer's work on one task of a plan. You never change the
plan or the work: you only report.

Look at the work through one lens: testability. Can each part of the
code be checked on its own, without the rest of the game running?

If the work holds up, you are satisfied. If not, say why in your
findings, one finding per problem, each specific enough for the doer to
act on.
```

The lens you picked in homework 2 belongs here now, in the validator's
`AGENTS.md`.

The factory still tells each machine what it tells it today: where the
plan and the seed are, the work to check, the validator's findings, and
the fields its result must have. What the machine *is* comes from its
folder.

## Watch for

Your machines run in the target, and the target sits inside your capstone
repository. Coding agents look for `AGENTS.md` (and `CLAUDE.md`) in the
folder they run in and the folders above it. So a machine can pick up
your repository's own `AGENTS.md`, the one that coaches you, and it will
not find its own, which is in `factory/machines/<name>/`, not above the
target.

So the factory has to hand each machine its `AGENTS.md`. How is up to
you: in the prompt, which works with any harness, or through a flag the
harness has, such as pi's `--append-system-prompt`. pi's
`--no-context-files` stops it reading the `AGENTS.md` files around the
target.

## Once your suite passes

- Move every machine's prompt out of your factory's code and into its
  `AGENTS.md`. Search your factory's source for your validator's lens:
  it should not be there.
- Build a generation in a fresh target:

  ```sh
  bin/factory --seed tetris/spec.md --target tetris/tetris-003 --all
  npm --prefix tetris/tetris-003 start
  ```

- Change your validator's lens by editing only its `AGENTS.md`, and
  build another generation, in `tetris/tetris-003-<lens>`. Did the
  findings follow?

### Bonus round: a model per machine

In homework 1's bonus round you chose one model for the whole run. Now
each machine names its own. Give the validator a different model from
the doer's, or a different provider's, and build another generation.
Does a second pair of eyes from another model find things the first
missed?
