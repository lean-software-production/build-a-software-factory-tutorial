# Homework 5a — Machine configuration

Read `FACTORY.md`, then the feature files in `features/`. Together they
are the whole spec of the factory at this point, not just the new parts.

Since homework 4 every machine has had a folder of its own,
`.assembly-lines/.machines/<name>/`, holding "its configuration". No
homework has said what goes in it, and your machines' prompts probably
still live in your factory's code. In homework 3 the route came out of
your code and into a line the factory reads. This homework does the same
for the machines: what a machine is for, and how it does its job, comes
out into its folder.

A machine's folder holds two things:

- **`AGENTS.md`** — the machine's instructions: what it is for, how it
  does its job, and anything it should bring to the work, such as the
  validator's lens. `AGENTS.md` is a convention most coding agents
  already read, so the same file serves whichever harness runs the
  machine.
- **The rest of its configuration** — the harness that runs it (`pi`,
  unless it names another) and whatever that harness needs: its model,
  and from homework 6 its provider. The file's name and format are your
  choice.

The factory gives each machine its own `AGENTS.md`, and no other
machine's. Change a machine's `AGENTS.md`, and the machine changes, with
no change to your code.

## What a target looks like

The format of the configuration file is yours; `machine.json` is only an
example:

```text
tetris/tetris-003/
  .assembly-lines/
    careful.dot
    quick.dot
    .machines/
      planner/
        AGENTS.md
        machine.json      {"harness": "pi", "model": "<a model>"}
      doer/
        AGENTS.md
        machine.json
      validator/
        AGENTS.md
        machine.json
      reviewer_1/
        AGENTS.md         the same in all three reviewers
        machine.json      {"harness": "pi", "model": "<an Anthropic model>"}
      reviewer_2/
        AGENTS.md
        machine.json      {"harness": "pi", "model": "<a Google model>"}
      reviewer_3/
        AGENTS.md
        machine.json      {"harness": "pi", "model": "<an OpenAI model>"}
      synthesiser/
        AGENTS.md
        machine.json
```

The three big brains' reviewers are configured alike apart from their
models: the same `AGENTS.md`, and a different model each.

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
`AGENTS.md`, and the reviewers' lens in each reviewer's.

## Watch for

Your machines run in the target, and the target sits inside your capstone
repository. Coding agents look for `AGENTS.md` (and `CLAUDE.md`) in the
folder they run in and the folders above it. So a machine can pick up
your repository's own `AGENTS.md`, the one that coaches you, and it will
not find its own, which is in `.assembly-lines/.machines/<name>/`, not
above the target.

So the factory has to hand each machine its `AGENTS.md`. How is up to
you: in the prompt, which works with any harness, or through a flag the
harness has, such as pi's `--append-system-prompt`. pi's
`--no-context-files` stops it reading the `AGENTS.md` files around the
target.

## Once your suite passes

- Move every machine's prompt out of your factory's code and into its
  `AGENTS.md`. Search your factory's source for your validator's lens:
  it should not be there.
- Change your validator's lens by editing only its `AGENTS.md`, and
  build a generation in a fresh target. Did the findings follow?
