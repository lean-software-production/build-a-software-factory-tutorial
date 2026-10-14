Feature: Machines

  No machine's work is written by the factory. The planner, the doer and
  the validator are machines on the line. Each has a name and a folder of
  its own on its line, .assembly-lines/<line>/machines/<name>/ in the
  target; two lines can each have a doer, configured differently. The
  folder holds the machine's AGENTS.md, its instructions: what the
  machine is for and how it does its job. It also holds the rest of its
  configuration: the harness that runs it, a coding agent such as pi by
  default or another named there, and whatever that harness needs, such
  as its model. A machine could as well be ordinary code. Whatever runs
  it, a machine answers with a result: JSON describing the job it did.

  Most examples say what each machine does in them: the planner plans
  the tasks alpha and beta, say, and the validator is never satisfied.
  That shows what the factory gives a machine and what it does with the
  result. Examples tagged @real-agent run a real agent.

  Background:
    Given a copy of the factory
    And a new target, with a seed describing a game of Tetris
    And the target has an assembly line "careful" on which the doer's work is validated
    And a run named "tetris", on the "careful" line, with that seed and target
    And the planner plans the tasks alpha and beta
    And the doer does the next task in the plan
    And the validator is always satisfied

  Rule: A machine runs pi unless its configuration names another harness

    Example: The validator's configuration names no harness
      Given a plan with three tasks, none of them done
      And no harness is chosen for the validator
      When the factory runs the "tetris" run
      Then pi has been called
      And the doer's chosen harness has been called

  Rule: A machine whose harness cannot be run does no work

    Example: The doer cannot be run
      Given a plan with three tasks, none of them done
      And the doer cannot be run
      When the factory runs the "tetris" run
      Then it reports that it could not run the doer
      And there are no new work commits

  Rule: The plan is what the planner wrote

    Example: A planner that plans two tasks
      Given no plan
      When the factory runs the "tetris" run
      Then the plan has the tasks "alpha" and "beta", and no others

  Rule: The target holds what the doer wrote

    Example: A doer that writes a file for each task
      Given a plan with three tasks, none of them done
      When the factory runs the "tetris" run
      Then there are three new work commits
      And each new work commit contains the work for one task

  Rule: A machine is given its own instructions

    The factory gives each machine the AGENTS.md in its folder, whatever
    harness runs it, and no other machine's. Instructions live with the
    machine, not in the factory: change a machine's AGENTS.md and the
    machine changes, with no change to the factory.

    Example: The doer's instructions
      Given a plan with three tasks, none of them done
      And the doer's AGENTS.md says "write the smallest code that does the task"
      When the factory runs the "tetris" run
      Then the doer was given "write the smallest code that does the task"

    Example: Each machine is given only its own
      Given a plan with three tasks, none of them done
      And the doer's AGENTS.md says "write the smallest code that does the task"
      And the validator's AGENTS.md says "be strict about error handling"
      When the factory runs the "tetris" run
      Then the validator was given "be strict about error handling"
      And it was not given "write the smallest code that does the task"

  Rule: Each line has its own machines

    A machine belongs to the line whose machines/ holds it. Two lines in
    a target can each have a doer, and a run is given the machines of the
    line it runs.

    Example: Two lines, two doers
      Given the target has an assembly line "quick" on which the doer goes straight to the planner
      And a run named "quick", on the "quick" line, with that seed and target
      And a plan for each run with three tasks of its own, none of them done
      And on the "careful" line, the doer's AGENTS.md says "take your time"
      And on the "quick" line, the doer's AGENTS.md says "be quick"
      When the factory runs the "quick" run
      Then the doer was given "be quick"
      And it was not given "take your time"

  Rule: The doer is pointed at the plan and the seed

    The factory cannot hand the doer a task: it never reads the plan. It
    tells the doer where the plan and the seed are, and the doer does the
    rest.

    Example: What the doer is given
      Given a plan with three tasks, none of them done
      When the factory runs the "tetris" run
      Then the doer was pointed at the plan and at the seed

  Rule: Each machine is pointed at the run's folder

    A machine can keep what it makes for the run — notes, artifacts,
    logs — in the run's folder, beside the plan. The factory tells each
    machine where it is.

    Example: What the validator is given
      Given a plan with three tasks, none of them done
      When the factory runs the "tetris" run
      Then the validator was pointed at the run's folder

  Rule: Validation is what the validator decided

    Example: A validator that is never satisfied
      Given a plan with three tasks, none of them done
      And the factory allows at most three attempts at a task
      And the validator is never satisfied
      When the factory runs the "tetris" run
      Then the doer has been called three times
      And there are no new work commits

  Rule: Each machine is asked for the fields its edges route on

    The factory tells each machine what its result must say: the field
    each edge leaving it names. The validator is also asked why it is
    not satisfied, in "findings", which go back to the doer. Nothing but
    that question makes a machine answer with a result.

    Example: What the planner is asked for
      Given a plan with three tasks, none of them done
      When the factory runs the "tetris" run
      Then the planner was asked for a result with the field "complete"

    Example: What the validator is asked for
      Given a plan with three tasks, none of them done
      When the factory runs the "tetris" run
      Then the validator was asked for a result with the fields "satisfied" and "findings"

    Example: Edges that name another field
      Given a plan with three tasks, none of them done
      And the edges from validator are labelled "approved" and "not approved"
      When the factory runs the "tetris" run
      Then the validator was asked for a result with the fields "approved" and "findings"

  Rule: A result is the last line of the answer that is JSON

    A machine may say anything before its result. The factory reads only
    the last line of the answer that parses as JSON.

    Example: The validator talks before its result
      Given a plan with three tasks, none of them done
      And the validator says "looks good to me" before its result
      When the factory runs the "tetris" run
      Then there are three new work commits

  Rule: What gets built follows the seed

    A factory that had Tetris tucked away inside it would pass every
    example that asks for Tetris. It would not pass this one.

    @real-agent
    Example: A Tetris with different details
      Given every machine runs pi
      And a seed describing Tetris on a board 8 columns wide, started with "npm run play"
      When the factory runs the "tetris" run
      Then "npm run play" in the target starts Tetris
      And its board is 8 columns wide
