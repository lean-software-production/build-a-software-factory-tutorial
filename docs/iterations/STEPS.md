# Steps

Every step in the iterations' feature files, as one vocabulary. A
student's step definitions carry over from one iteration to the next, so
a step's words change only when what it means changes. From 005, the
named factory execution is a **run**; its steps use that noun consistently
through every later iteration. Starting or resuming it is an invocation
of the same run, not a new run. When an iteration needs a new step, add
it here first. `bin/step-drift` checks every step
against this list, and shows what each iteration adds and drops.

`{string}` is a quoted value, `{word}` a single word. The range says which
iterations use the phrase; "001+" means from 001 on.

Steps say what the machines do, never how a test makes them do it. "The
validator is never satisfied" is the student's to make true, usually with
a small program chosen as the validator's harness: a test double. No
feature mentions one.

No step waits a set time. A machine an example needs to see at work stays
part-way through until a step says it finishes, or the run finishes, and a step that waits for something waits for it to happen, not for
a while.

This file is for authors of the course. `fetch-iteration` does not copy
it to students.

## Given

### The factory, the target and the seed

- `a seed describing a game of Tetris` — 001–004. A seed file outside the target, selected with `--seed`.
- `no seed is chosen` — 001–004. Omit the seed argument.
- `a seed describing Tetris on a board 8 columns wide, started with {string}` — 001+, `@real-agent`.
- `a copy of the factory` — 001+. The factory copied into a new folder of its own, with no runs or targets.
- `a new target` — 001–004. A plain folder in the test repository, selected by an explicit target argument.
- `the target folder does not exist` — 001–004. The explicitly selected output path does not exist yet.
- `the target is outside any Git repository` — 001+. Select a folder with no repository among its ancestors. From 005 place the selected line's folder, machines included, there before invoking the run; this setup must not initialize Git.
- `the factory has staged and unstaged changes` — 001+. Unrelated changes outside the target, including both staged and unstaged edits to the same file.
- `no target is chosen` — 001+. Omit the target argument. From 005 any invocation of a run, first or later: the target is never remembered, because the run is kept in it.
- `a new target, with a seed describing a game of {word}` — 005+. A fresh target folder and selected seed in the same test repository as the factory copy. Never initialize a nested repository here; shared-repository behavior must remain covered.
- `the seed has been deleted` — 001+. The selected seed file (the current run's seed from 005).

### Runs and lines

- `the line has the three big brains` — 006+. reviewer_1 to reviewer_3 and the synthesiser, each a machine in the line's `machines/` (the line under test, or the current run's line), configured alike but for their models.
- `the target has an assembly line {string} on which the doer's work is validated` — 005+. The line in `assembly-line.feature`'s Background, as `.assembly-lines/<name>/assembly-line.dot` in the latest target, with its own planner, doer and validator in its `machines/`.
- `the target has an assembly line {string} on which the doer goes straight to the planner` — 005+. The same line, without the validator, with its own planner and doer.
- `the {string} line has been copied into the target` — 005+. Its folder, machines included but no runs, from the target that has it into the latest.
- `a run named {string}, on the {string} line, with that seed and target` — 005+. The latest target and its seed; the line is one of that target's. The first run named is the current one.
- `the {string} run has been started` — 005+. It has run once, with all its settings.
- `this assembly line` — 004+. The graph that follows, as the line under test: its `assembly-line.dot`, in the factory's `assembly-lines/` in 004, in the latest target's `.assembly-lines/` from 005.
- `the validator has been taken out, so the doer goes straight to the planner` — 004+. The line under test.
- `the validator has been taken out of the {string} line, so the doer goes straight to the planner` — 005+.
- `the three big brains has replaced the validator on the {string} line` — 006+. The line has the three big brains; on it the doer's edge to the validator becomes an unlabelled edge to each reviewer, each reviewer has an unlabelled edge to the synthesiser, and the validator's edges become the synthesiser's.
- `{string} is misspelt {string} throughout the assembly line` — 004+.
- `{string} is misspelt {string} throughout the {string} line` — 005+.
- `the edge from {word} to {word} has been taken out` — 004+.
- `the edges from {word} are labelled {string} and {string}` — 004+. Its two labelled edges, in place of `satisfied` and `not satisfied`.

### Machines and their harnesses

001 has one agent, "the agent". From 002 the planner, the doer and the
validator are machines, named by those words; from 006, so are the
three big brains' reviewers and synthesiser.

What a machine does, in the examples that say. A result has the fields
the line routes on: `complete` for the planner, `satisfied` and
`findings` for a validator or synthesiser, whatever the machine was asked.

- `the agent plans the tasks alpha and beta, and does one task a pass` — 001. With no plan, writes one: `alpha`, then `beta`, and its result says the plan is not complete. Otherwise does the first task not done, marks it done, and says whether the plan is now complete.
- `the {word} plans the tasks alpha and beta` — 002+. The planner. With no plan, writes one: `alpha`, then `beta`. With a plan, marks done every task whose work is committed. Its result says whether the plan is complete.
- `the {word} does the next task in the plan` — 002+. The doer. Does the first task not done, and never touches the plan.
- `the {word} keeps its plan in prose` — 001+. A plan no factory could parse; plays any part: writes the plan, builds whichever of `alpha` and `beta` is not committed yet, and says the plan is complete once both are.
- `the {word} writes a file called SENTINEL` — 001+. And nothing else.
- `the {word} is always satisfied` — 002+. A validator or the synthesiser.
- `every reviewer is always satisfied` — 006+.
- `no reviewer finishes until all three have begun` — 006+. A factory that runs them one after another never finishes the run.
- `the {word} is never satisfied` — 002+. With a finding.
- `the {word} is not satisfied the first time` — 002+. With the finding `not satisfied the first time`; satisfied every time after.
- `every reviewer is not satisfied, with a finding of its own: "report 1", "report 2" or "report 3"` — 006+. Numbered in the order they report.
- `the second reviewer is not satisfied, with the finding {string}` — 006+. reviewer_2 only.
- `the second reviewer answers in prose, with no result` — 006+. reviewer_2 only.
- `the second reviewer cannot be run` — 006+. reviewer_2's harness is a path where no program exists.
- `the {word} answers in prose, with no result` — 001+. Having done its work: the agent or doer writes a file called `UNREADABLE`.
- `the {word} says {string} before its result` — 001+. A line of prose, then its result.
- `the doer says {string}, then {string}` — 007+. Generates the first line; the second only once the attempt carries on to its end.
- `the reviewers' lens is {word}` — 006+. Written in each reviewer's `AGENTS.md`.
- `the reviewers run on Anthropic, Google and OpenAI models` — 007+. reviewer_1 to reviewer_3's configurations name those providers.
- `the {word} cannot be run` — 001+. Its harness is a path where no program exists.
- `no harness is chosen` — 001–002. pi, for every machine.
- `no harness is chosen for the {word}` — 003+. pi, for that machine.
- `the agent is pi` — 001, `@real-agent`.
- `every machine runs pi` — 002+, `@real-agent`.
- `the validator's lens is {word}` — 002+. From 003, written in the validator's `AGENTS.md`.
- `the {word}'s AGENTS.md says {string}` — 003+. That machine's instructions: the `AGENTS.md` in its folder, `machines/<name>/` in the factory in 003, and in its line's `machines/` from 004 (the current run's line from 005): the configuration its harness runs on.
- `on the {string} line, the {word}'s AGENTS.md says {string}` — 005+. The same, for the machine on that line.
- `the folder above the target has an AGENTS.md saying {string}` — 003+, `@real-agent`. The folder that holds the target, inside the test repository.
- `the {word} has its own login` — 003+. A copy of a login in its folder, as its harness keeps it. From 003 every machine has one unless a step says it has none.
- `the {word} has no login` — 003+. None in its folder.
- `there is an API key for the {word}'s provider` — 003+. In the environment the factory runs in.
- `there is no API key for the {word}'s provider` — 003+.

### Limits

- `the factory allows at most three attempts per pass` — 002–003.
- `the factory allows at most three attempts at a task` — 004+. The orchestrator's limit; the line only routes.

### The plan

Plans in steps are in whatever format the student's machines keep. The
tasks are `first`, `second` and `third`, and a task's work is a file with
its name. In 001–004, plans supplied by Given steps are committed as the
starting state before the invocation baseline is captured.

- `no plan` — 001+.
- `a plan with three tasks, none of them done` — 001+.
- `a plan whose first task is done` — 001+.
- `a plan in which every task is done` — 001+.
- `a plan for each run with three tasks of its own, none of them done` — 005+. Each run's tasks are named after the run.
- `a plan with one task, not done` — 006+.

### The running factory

From 007 the factory is a daemon. These steps start a run and leave it
running, rather than running it to the end.

- `the factory has run the {string} run` — 008+. To the end.
- `the {string} run is running, with the doer part-way through an attempt` — 007+. Started, and the doer has begun an attempt it does not finish until a step says so.
- `the {string} run is running, with the doer part-way through an attempt, having said {string}` — 007+. And the doer has generated that line.
- `the {string} run is running, with every reviewer part-way through` — 007+. All three have begun, and none finishes until a step says so.
- `I am watching the {string} run` — 007+. Following it, from another command, as it goes.
- `I am watching the {string} run as it runs` — 007+. Started, and followed.
- `I have stopped the {string} run` — 007+.

## When

- `the factory builds the target {string} to completion` — 001–004. Select that folder on the command line; run to completion (`--all` through 002, the assembly line from 004). Relative paths are from the caller's working directory; absolute paths are also accepted.

- `the factory builds the same target using its absolute path` — 001–004. Repeat the previous target-building command to completion, replacing only its target argument with the absolute path to that same folder.

- `the factory runs one pass` — 001–003.
- `the factory runs to completion` — 001–003.
- `the factory runs` — 004.
- `the factory runs the {string} run` — 005+. With all its settings: naming them again is fine.
- `the factory runs the {string} run, given only its name and target` — 005+.
- `the factory runs the {string} run on the {string} line` — 005+. Its target, and a line other than its own.
- `the factory reads the assembly line` — 004+. Checks the line under test without running it.
- `the doer's first attempt at a task is untestable` — 002+, `@real-agent`.
- `the doer finishes its attempt` — 008+.
- `the reviewers finish` — 008+.
- `I start the {string} run` — 007+. The command returns while the run is running; the doer does not finish its first attempt until a step says so.
- `the {string} run has run to the end` — 007+. Waits until it has.
- `I stop the {string} run` — 007+.
- `I stop the factory` — 007+.
- `I watch the {string} run` — 007+. What the watch command shows now.
- `I read the {string} run's record` — 007+.
- `I say {string} to the {word}` — 008+.
- `I say {string} to {word}` — 008+. A machine by name, such as reviewer_2.

## Then

### The plan

- `the committed plan matches the plan on disk` — 001–004. Compare the plan in HEAD with the target's plan file; no parsing by the factory is required.
- `the target has no uncommitted changes` — 001–004. Check tracked and untracked non-ignored files inside the selected target. Unrelated changes elsewhere must remain untouched.
- `there are no new work commits` — 001+. Plan-only commits are allowed, and from 005 commits of the run's folder.
- `there is a plan` — 001+.
- `there is no plan` — 001+.
- `the plan shows the first task as done` — 001+.
- `the plan shows the first two tasks as done` — 001+.
- `the plan shows the other two as not done` — 001+.
- `the plan shows every task as done` — 001+.
- `the plan shows every task as not done` — 001+.
- `the plan still has those three tasks` — 001+.
- `the plan has the tasks {string} and {string}, and no others` — 001+.
- `the plan is .factory/plan.md in the target` — 001–004.
- `there is no plan in the factory's folder` — 001+.
- `the plan is plan.md in the {string} line's runs folder, under {word}` — 005+. `.assembly-lines/<line>/runs/<run>/plan.md` in the target.
- `each run has its own plan` — 005+.
- `every task in the plan comes from the seed` — 001+, `@real-agent`.
- `that task has a subtask for the finding` — 002+, `@real-agent`.
- `the plan has no new task` — 002+, `@real-agent`.

### Commits and work

These are about the selected target (the current run's target from 005).
Count commits with a pathspec for the selected target. A work commit
changes product files; a plan-only commit does not count as a work commit.
Plans are part of target history throughout: through 004 in the target's
`.factory/`, and from 005 in the run's folder, `.assembly-lines/<line>/runs/<run>/`,
which the factory commits in commits of its own. Neither kind is a work
commit. Other targets may share the same repository. Each invocation captures
a new baseline before running: commit counts are relative to that invocation,
not to scenario setup. For a daemon, capture the baseline before starting
the run and compare after it finishes.

- `there is one new work commit` — 001+.
- `there are two new work commits` — 001+.
- `there are three new work commits` — 001+.
- `the run's folder has been committed in commits of its own` — 005+. Every new commit that touches the run's folder touches nothing outside it, and there is at least one.
- `the run's folder has no uncommitted changes` — 005+. Tracked and untracked files under the run's folder, after the invocation ends.
- `there are no new commits` — 001–004. From 005 an invocation always commits its run's folder: see `there are no new work commits`.
- `it contains the work for the {word} task` — 001+. The newest work commit holds that task's product files and no other task's product files. In 001–004 it may also include the plan.
- `its only product file is SENTINEL` — 001–004. Inspect the latest work commit: apart from the plan, its only changed file is SENTINEL.
- `it contains SENTINEL and nothing else` — 005+.
- `each new work commit contains the work for one task` — 004+.
- `no new commit contains the work for the first task` — 004+.
- `the work for alpha and beta has been committed` — 001+.
- `each target holds only its own run's work` — 005+.
- `Tetris has been built in the target` — 001+, `@real-agent`.
- `{string} in the target starts Tetris` — 001+, `@real-agent`.
- `its board is 8 columns wide` — 001+, `@real-agent`.
- `the target's CODEWORD file says {string}` — 003+, `@real-agent`.
- `the {word}'s login is ignored by Git` — 003+. `git check-ignore` reports it, wherever the machine's folder is.

### The factory

- `the target is a Git repository` — 001+. Git was initialized for a target outside any existing repository.
- `the factory's own files and unrelated uncommitted changes are as they were` — 001+. Snapshot the factory copy's source files and all pre-existing unrelated staged and unstaged changes before each invocation. Compare file contents, index entries and path-limited history using the actual source paths in that copy, not a prescribed folder name. Exclude the run's own runtime state, which is expected to change. The repository's global history may gain target-only commits.
- `the target uses the containing repository` — 001+. The target has no nested `.git`; its Git root is the existing test repository.
- `it reports that a target is required` — 001+.
- `the targets {string} and {string} each have their own completed plan and committed work` — 001–004. Each has alpha and beta and a completed plan, all committed. Commits for each target contain only its work and plan. Inspect history limited to that target's paths.
- `the target {string} is unchanged` — 001–004. Snapshot all known targets before each invocation; compare this target's files, plan and path-limited Git history with that snapshot.

- `the factory has stopped` — 001+.
- `the factory refuses` — 005+.
- `it accepts it` — 004+. The line under test.
- `it refuses it` — 004+.
- `it reports that there is no seed` — 001+.
- `it reports that it could not run the {word}` — 001+. The agent in 001; a machine from 002.
- `it reports that it could not read the {word}'s result` — 001+. Its answer was not a result.
- `it reports that the result of {word} has no field {string}` — 004+. A label on the line names a field the machine's result lacks.
- `it reports that the pass hit its limit` — 002–003.
- `it reports that a task hit its limit` — 004+.
- `it reports that it has no machine called {string}` — 004+.
- `it reports that the branches from {word} do not meet` — 006+. A fan out whose branches do not each lead, by one unlabelled edge, to the same machine.
- `it reports that it could not read reviewer_2's result` — 006+.
- `it reports that it could not run reviewer_2` — 006+.
- `it reports that finish cannot be reached from {word}` — 004+. Among the machines it names.
- `it says the {string} run already has a line` — 005+.
- `it reports that the {word} cannot sign in` — 003+.

### Fan out

- `every reviewer has been called once` — 006+.
- `every reviewer was given the same prompt` — 006+.
- `every reviewer was asked for a result` — 006+.
- `every reviewer was given the work for the {word} task` — 006+.
- `every reviewer was given {string}` — 006+.
- `the synthesiser was given {string}, {string} and {string}` — 006+.
- `the reviewers' findings are about {word}` — 006+, `@real-agent`.

### The daemon, watching and the record

What watching and the record show is the student's to lay out; the
steps only need each line of generated text to say which machine it came
from, and the tokens in and out per machine.

- `the command has returned while the {string} run is running` — 007+.
- `the factory is running` — 007+.
- `the factory is not running` — 007+.
- `the {string} run is running` — 007+.
- `the {string} run is not running` — 007+.
- `what I am watching shows that the {string} run was stopped` — 007+.
- `I see {string} from the doer` — 007+. Waits a little for it.
- `I do not see {string}` — 007+.
- `I see {string} from reviewer_1, reviewer_2 and reviewer_3` — 007+.
- `it shows reviewer_1, reviewer_2 and reviewer_3 as running` — 007+.
- `I see what the planner generated` — 007+.
- `it shows what every machine generated` — 007+.
- `it shows what every machine spent` — 007+.
- `the record is in the run's folder in the target, and committed` — 007+. Under `.assembly-lines/<line>/runs/<run>/`, with no uncommitted changes once the run has ended.
- `it shows tokens in and tokens out for the {word}` — 007+.
- `it shows a total for each of Anthropic, Google and OpenAI` — 007+.
- `it shows a total for the whole run` — 007+.
- `what I watched showed the doer's tokens go up` — 007+.
- `what I watched showed the run's total go up` — 007+.

### Steering

A machine "heard" a message when its generated text shows it did, at the
point it heard it.

- `it says that the doer is what is running` — 008+.
- `it says that nothing is running` — 008+.
- `the doer heard {string} before it said {string}` — 008+.
- `{word} heard {string}` — 008+.
- `neither reviewer_1 nor reviewer_3 heard it` — 008+.
- `the doer heard {string} once` — 008+.
- `the {word} did not hear {string}` — 008+.
- `it shows that the doer was told {string}` — 008+.

### Agents

Counted over the latest run.

- `no agent has been called` — 001+.
- `the agent has been called once` — 001.
- `pi has been called` — 001+.
- `pi has not been called` — 001+.
- `the chosen agent has been called` — 001.
- `the {word}'s chosen harness has been called` — 002+.
- `the {word} has been called once` — 002+. planner, doer, validator or synthesiser.
- `the {word} has been called twice` — 002+.
- `the {word} has been called three times` — 002+.
- `the {word} has been called four times` — 002+.
- `the {word} has not been called` — 002+.
- `the planner was called before the doer` — 004+.
- `the validator was called for the {string} run` — 005+.
- `the validator was not called for the {string} run` — 005+.

What a machine (or 001's agent) was given:

- `the {word} was asked for a result with the field {string}` — 001+.
- `the {word} was asked for a result with the fields {string} and {string}` — 002+.

- `the {word} was pointed at the plan and at the seed` — 001+.
- `the {word} signed in with its own login` — 003+.
- `the {word} signed in with the API key` — 003+.
- `the {word} was pointed at the run's folder` — 005+. `.assembly-lines/<line>/runs/<run>/` in the target, for whatever the machine keeps.
- `the {word} was given the work for the {word} task` — 002+.
- `it was not given the work for the {word} task` — 002+.
- `the {word} was given {string}` — 002+.
- `it was not given {string}` — 003+. The machine the step before names.
- `the {word} was given the validator's findings` — 002+. The findings in the validator's result.
- `the doer was given the synthesiser's findings` — 006+.
- `the validator has changed neither the plan nor the work` — 002+, `@real-agent`.
- `the validator's findings are about {word}` — 002+, `@real-agent`.
