# Steps

Every step in the iterations' feature files, as one vocabulary. A
student's step definitions carry over from one iteration to the next, so
a step's words change only when what it means changes. From 004, the
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

- `a seed describing a game of Tetris` — 001–003. A seed file outside the target, selected with `--seed`.
- `no seed is chosen` — 001–003. Omit the seed argument.
- `a seed describing Tetris on a board 8 columns wide, started with {string}` — 001+, `@real-agent`.
- `a copy of the factory` — 001+. The factory copied into a new folder of its own, with no runs or targets.
- `a new target` — 001–003. A plain folder in the test repository, selected by an explicit target argument.
- `the target folder does not exist` — 001–003. The explicitly selected output path does not exist yet.
- `the target is outside any Git repository` — 001+. Select a folder with no repository among its ancestors. From 004 place the selected line and machines there before invoking the run; this setup must not initialize Git.
- `the factory has staged and unstaged changes` — 001+. Unrelated changes outside the target, including both staged and unstaged edits to the same file.
- `no target is chosen` — 001+. Omit the target argument. From 004 this is the first invocation of a run with no saved configuration, not a resumed run.
- `a new target, with a seed describing a game of {word}` — 004+. A fresh target folder and selected seed in the same test repository as the factory copy. Never initialize a nested repository here; shared-repository behavior must remain covered.
- `the seed has been deleted` — 001+. The selected seed file (the current run's seed from 004).

### Runs and lines

- `the target has the machines planner, doer and validator` — 004+. Their configurations, in the latest target's `.assembly-lines/.machines/`.
  From 005a each has its own login, unless a step says it has none.
- `the target has the three big brains` — 005+. reviewer_1 to reviewer_3 and the synthesiser, each a machine of the latest target's, configured alike but for their models.
- `the target has an assembly line {string} on which the doer's work is validated` — 004+. The line in `assembly-line.feature`'s Background, in the latest target's `.assembly-lines/`.
- `the target has an assembly line {string} on which the doer goes straight to the planner` — 004+. The same line, without the validator.
- `the {string} line has been copied into the target` — 004+. From the target that has it, into the latest.
- `a run named {string}, on the {string} line, with that seed and target` — 004+. The latest target and its seed; the line is one of that target's. The first run named is the current one.
- `the {string} run has been started` — 004+. It has run once, with all its settings.
- `this assembly line` — 003+. The graph that follows, as the line under test: in the factory's folder through 003, in the latest target from 004.
- `the validator has been taken out, so the doer goes straight to the planner` — 003.
- `the validator has been taken out of the {string} line, so the doer goes straight to the planner` — 004+.
- `the three big brains has replaced the validator on the {string} line` — 005+. The target has the three big brains; on that line the doer's edge to the validator becomes an unlabelled edge to each reviewer, each reviewer has an unlabelled edge to the synthesiser, and the validator's edges become the synthesiser's.
- `{string} is misspelt {string} throughout the assembly line` — 003+.
- `{string} is misspelt {string} throughout the {string} line` — 004+.
- `the edge from {word} to {word} has been taken out` — 003+.
- `the edges from {word} are labelled {string} and {string}` — 003+. Its two labelled edges, in place of `satisfied` and `not satisfied`.

### Machines and their harnesses

001 has one agent, "the agent". From 002 the planner, the doer and the
validator are machines, named by those words; from 005, so are the
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
- `every reviewer is always satisfied` — 005+.
- `no reviewer finishes until all three have begun` — 005+. A factory that runs them one after another never finishes the run.
- `the {word} is never satisfied` — 002+. With a finding.
- `the {word} is not satisfied the first time` — 002+. With the finding `not satisfied the first time`; satisfied every time after.
- `every reviewer is not satisfied, with a finding of its own: "report 1", "report 2" or "report 3"` — 005+. Numbered in the order they report.
- `the second reviewer is not satisfied, with the finding {string}` — 005+. reviewer_2 only.
- `the second reviewer answers in prose, with no result` — 005+. reviewer_2 only.
- `the second reviewer cannot be run` — 005+. reviewer_2's harness is a path where no program exists.
- `the {word} answers in prose, with no result` — 001+. Having done its work: the agent or doer writes a file called `UNREADABLE`.
- `the {word} says {string} before its result` — 001+. A line of prose, then its result.
- `the doer says {string}, then {string}` — 006+. Generates the first line; the second only once the attempt carries on to its end.
- `the reviewers' lens is {word}` — 005+. From 005a, written in each reviewer's `AGENTS.md`.
- `the reviewers run on Anthropic, Google and OpenAI models` — 006+. reviewer_1 to reviewer_3's configurations name those providers.
- `the {word} cannot be run` — 001+. Its harness is a path where no program exists.
- `no harness is chosen` — 001–002. pi, for every machine.
- `no harness is chosen for the {word}` — 003+. pi, for that machine.
- `the agent is pi` — 001, `@real-agent`.
- `every machine runs pi` — 002+, `@real-agent`.
- `the validator's lens is {word}` — 002+. From 005a, written in the validator's `AGENTS.md`.
- `the {word}'s AGENTS.md says {string}` — 005a+. That machine's instructions: the `AGENTS.md` in its folder in the latest target's `.assembly-lines/.machines/`, the configuration its harness runs on.
- `the folder above the target has an AGENTS.md saying {string}` — 005a+, `@real-agent`. The folder that holds the target, inside the test repository.
- `the {word} has its own login` — 005a+. A copy of a login in its folder, as its harness keeps it.
- `the {word} has no login` — 005a+. None in its folder.
- `there is an API key for the {word}'s provider` — 005a+. In the environment the factory runs in.
- `there is no API key for the {word}'s provider` — 005a+.

### Limits

- `the factory allows at most three attempts per pass` — 002.
- `the factory allows at most three attempts at a task` — 003+. The orchestrator's limit; the line only routes.

### The plan

Plans in steps are in whatever format the student's machines keep. The
tasks are `first`, `second` and `third`, and a task's work is a file with
its name. In 001–003, plans supplied by Given steps are committed as the
starting state before the invocation baseline is captured.

- `no plan` — 001+.
- `a plan with three tasks, none of them done` — 001+.
- `a plan whose first task is done` — 001+.
- `a plan in which every task is done` — 001+.
- `a plan for each run with three tasks of its own, none of them done` — 004+. Each run's tasks are named after the run.
- `a plan with one task, not done` — 005+.

### The running factory

From 006 the factory is a daemon. These steps start a run and leave it
running, rather than running it to the end.

- `the factory has run the {string} run` — 007+. To the end.
- `the {string} run is running, with the doer part-way through an attempt` — 006+. Started, and the doer has begun an attempt it does not finish until a step says so.
- `the {string} run is running, with the doer part-way through an attempt, having said {string}` — 006+. And the doer has generated that line.
- `the {string} run is running, with every reviewer part-way through` — 006+. All three have begun, and none finishes until a step says so.
- `I am watching the {string} run` — 006+. Following it, from another command, as it goes.
- `I am watching the {string} run as it runs` — 006+. Started, and followed.
- `I have stopped the {string} run` — 006+.

## When

- `the factory builds the target {string} to completion` — 001–003. Select that folder on the command line; run to completion (`--all` through 002, the assembly line from 003). Relative paths are from the caller's working directory; absolute paths are also accepted.

- `the factory builds the same target using its absolute path` — 001–003. Repeat the previous target-building command to completion, replacing only its target argument with the absolute path to that same folder.

- `the factory runs one pass` — 001–002.
- `the factory runs to completion` — 001–002.
- `the factory runs` — 003.
- `the factory runs the {string} run` — 004+. With all its settings: naming them again is fine.
- `the factory runs the {string} run, given only its name` — 004+.
- `the factory runs the {string} run with that target` — 004+. The latest target, in place of its own.
- `the factory reads the assembly line` — 003+. Checks the line under test without running it.
- `the doer's first attempt at a task is untestable` — 002+, `@real-agent`.
- `the doer finishes its attempt` — 007+.
- `the reviewers finish` — 007+.
- `I start the {string} run` — 006+. The command returns while the run is running; the doer does not finish its first attempt until a step says so.
- `the {string} run has run to the end` — 006+. Waits until it has.
- `I stop the {string} run` — 006+.
- `I stop the factory` — 006+.
- `I watch the {string} run` — 006+. What the watch command shows now.
- `I read the {string} run's record` — 006+.
- `I say {string} to the {word}` — 007+.
- `I say {string} to {word}` — 007+. A machine by name, such as reviewer_2.

## Then

### The plan

- `the committed plan matches the plan on disk` — 001–003. Compare the plan in HEAD with the target's plan file; no parsing by the factory is required.
- `the target has no uncommitted changes` — 001–003. Check tracked and untracked non-ignored files inside the selected target. Unrelated changes elsewhere must remain untouched.
- `there are no new work commits` — 001–003. Plan-only commits are allowed.
- `there is a plan` — 001+.
- `there is no plan` — 001+.
- `the plan shows the first task as done` — 001+.
- `the plan shows the first two tasks as done` — 001+.
- `the plan shows the other two as not done` — 001+.
- `the plan shows every task as done` — 001+.
- `the plan shows every task as not done` — 001+.
- `the plan still has those three tasks` — 001+.
- `the plan has the tasks {string} and {string}, and no others` — 001+.
- `the plan is .factory/plan.md in the target` — 001–003.
- `there is no plan in the factory's folder` — 001–003.
- `the plan is plan.md in the factory's runs folder, under tetris` — 004+.
- `there is no plan in the target` — 004+.
- `each run has its own plan` — 004+.
- `every task in the plan comes from the seed` — 001+, `@real-agent`.
- `that task has a subtask for the finding` — 002+, `@real-agent`.
- `the plan has no new task` — 002+, `@real-agent`.

### Commits and work

These are about the selected target (the current run's target from 004).
Count commits with a pathspec for the selected target. A work commit
changes product files; a plan-only commit does not count as a work commit.
Plans are part of target history through 003; from 004 they live outside
the target. Other targets may share the same repository. Each invocation captures
a new baseline before running: commit counts are relative to that invocation,
not to scenario setup. For a daemon, capture the baseline before starting
the run and compare after it finishes.

- `there is one new work commit` — 001+.
- `there are two new work commits` — 001+.
- `there are three new work commits` — 001+.
- `there are no new commits` — 001+.
- `it contains the work for the {word} task` — 001+. The newest work commit holds that task's product files and no other task's product files. In 001–003 it may also include the plan.
- `its only product file is SENTINEL` — 001–003. Inspect the latest work commit: apart from the plan, its only changed file is SENTINEL.
- `it contains SENTINEL and nothing else` — 004+.
- `each new work commit contains the work for one task` — 003+.
- `no new commit contains the work for the first task` — 003+.
- `the work for alpha and beta has been committed` — 001+.
- `each target holds only its own run's work` — 004+.
- `Tetris has been built in the target` — 001+, `@real-agent`.
- `{string} in the target starts Tetris` — 001+, `@real-agent`.
- `its board is 8 columns wide` — 001+, `@real-agent`.
- `the target's CODEWORD file says {string}` — 005a+, `@real-agent`.
- `the {word}'s login is ignored by Git` — 005a+. `git check-ignore` reports it, wherever the machine's folder is.

### The factory

- `the target is a Git repository` — 001+. Git was initialized for a target outside any existing repository.
- `the factory's own files and unrelated uncommitted changes are as they were` — 001+. Snapshot the factory copy's source files and all pre-existing unrelated staged and unstaged changes before each invocation. Compare file contents, index entries and path-limited history using the actual source paths in that copy, not a prescribed folder name. Exclude the run's own runtime state, which is expected to change. The repository's global history may gain target-only commits.
- `the target uses the containing repository` — 001+. The target has no nested `.git`; its Git root is the existing test repository.
- `it reports that a target is required` — 001+.
- `the targets {string} and {string} each have their own completed plan and committed work` — 001–003. Each has alpha and beta and a completed plan, all committed. Commits for each target contain only its work and plan. Inspect history limited to that target's paths.
- `the target {string} is unchanged` — 001–003. Snapshot all known targets before each invocation; compare this target's files, plan and path-limited Git history with that snapshot.

- `the factory has stopped` — 001+.
- `the factory refuses` — 004+.
- `it accepts it` — 003+. The line under test.
- `it refuses it` — 003+.
- `it reports that there is no seed` — 001+.
- `it reports that it could not run the {word}` — 001+. The agent in 001; a machine from 002.
- `it reports that it could not read the {word}'s result` — 001+. Its answer was not a result.
- `it reports that the result of {word} has no field {string}` — 003+. A label on the line names a field the machine's result lacks.
- `it reports that the pass hit its limit` — 002.
- `it reports that a task hit its limit` — 003+.
- `it reports that it has no machine called {string}` — 003+.
- `it reports that the branches from {word} do not meet` — 005+. A fan out whose branches do not each lead, by one unlabelled edge, to the same machine.
- `it reports that it could not read reviewer_2's result` — 005+.
- `it reports that it could not run reviewer_2` — 005+.
- `it reports that finish cannot be reached from {word}` — 003+. Among the machines it names.
- `it says the {string} run already has a target` — 004+.
- `it reports that the {word} cannot sign in` — 005a+.

### Fan out

- `every reviewer has been called once` — 005+.
- `every reviewer was given the same prompt` — 005+.
- `every reviewer was asked for a result` — 005+.
- `every reviewer was given the work for the {word} task` — 005+.
- `every reviewer was given {string}` — 005+.
- `the synthesiser was given {string}, {string} and {string}` — 005+.
- `the reviewers' findings are about {word}` — 005+, `@real-agent`.

### The daemon, watching and the record

What watching and the record show is the student's to lay out; the
steps only need each line of generated text to say which machine it came
from, and the tokens in and out per machine.

- `the command has returned while the {string} run is running` — 006+.
- `the factory is running` — 006+.
- `the factory is not running` — 006+.
- `the {string} run is running` — 006+.
- `the {string} run is not running` — 006+.
- `what I am watching shows that the {string} run was stopped` — 006+.
- `I see {string} from the doer` — 006+. Waits a little for it.
- `I do not see {string}` — 006+.
- `I see {string} from reviewer_1, reviewer_2 and reviewer_3` — 006+.
- `it shows reviewer_1, reviewer_2 and reviewer_3 as running` — 006+.
- `I see what the planner generated` — 006+.
- `it shows what every machine generated` — 006+.
- `it shows what every machine spent` — 006+.
- `the record is in the run's folder in the factory, not in the target` — 006+.
- `it shows tokens in and tokens out for the {word}` — 006+.
- `it shows a total for each of Anthropic, Google and OpenAI` — 006+.
- `it shows a total for the whole run` — 006+.
- `what I watched showed the doer's tokens go up` — 006+.
- `what I watched showed the run's total go up` — 006+.

### Steering

A machine "heard" a message when its generated text shows it did, at the
point it heard it.

- `it says that the doer is what is running` — 007+.
- `it says that nothing is running` — 007+.
- `the doer heard {string} before it said {string}` — 007+.
- `{word} heard {string}` — 007+.
- `neither reviewer_1 nor reviewer_3 heard it` — 007+.
- `the doer heard {string} once` — 007+.
- `the {word} did not hear {string}` — 007+.
- `it shows that the doer was told {string}` — 007+.

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
- `the planner was called before the doer` — 003+.
- `the validator was called for the {string} run` — 004+.
- `the validator was not called for the {string} run` — 004+.

What a machine (or 001's agent) was given:

- `the {word} was asked for a result with the field {string}` — 001+.
- `the {word} was asked for a result with the fields {string} and {string}` — 002+.

- `the {word} was pointed at the plan and at the seed` — 001+.
- `the {word} signed in with its own login` — 005a+.
- `the {word} signed in with the API key` — 005a+.
- `the {word} was given the work for the {word} task` — 002+.
- `it was not given the work for the {word} task` — 002+.
- `the {word} was given {string}` — 002+.
- `it was not given {string}` — 005+. The machine the step before names: the synthesiser in 005, any machine from 005a.
- `the {word} was given the validator's findings` — 002+. The findings in the validator's result.
- `the doer was given the synthesiser's findings` — 005+.
- `the validator has changed neither the plan nor the work` — 002+, `@real-agent`.
- `the validator's findings are about {word}` — 002+, `@real-agent`.
