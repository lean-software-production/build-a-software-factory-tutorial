# Lines own their machines and runs

Date: 2026-10-14

## Status

accepted

## Context

From homework 4 (now 5) a target held its lines in `.assembly-lines/` and
their machines in `.assembly-lines/.machines/`: a hidden folder inside a
hidden folder, with every line in the target sharing one doer. Runs lived
in the factory, in `factory/runs/<name>/`, out of Git, so a generation's
plan and record were not kept with what it built. And until 005a no
iteration said what a machine's folder holds, so machines' prompts stayed
in the students' factory code.

## Decision

A machine is configured by a folder of its own: its `AGENTS.md`, its
instructions, and the rest of its configuration, naming its harness and
whatever that harness needs. This is iteration 003, before assembly
lines, so every later iteration builds on it.

From 004 a line is a folder named for it, holding `assembly-line.dot` and
its own `machines/`. From 005 lines live in the target, and each line's
folder also holds its runs:

    <target>/.assembly-lines/<line>/
      assembly-line.dot
      machines/<machine>/AGENTS.md, and its configuration
      runs/<run>/plan.md, and whatever the machines keep for the run

Machines belong to their line: two lines can each have a doer. A run is
found by its target and its name, so every invocation names its target,
and the factory keeps nothing of a run. The factory commits a run's
folder in commits of its own, never with the work, and an invocation
leaves nothing in it uncommitted. From 007 the run's record, what the
machines generated and spent, goes there too.

## Consequences

- A target is self-contained: its product, the lines that build it, their
  machines, and the history of every run, all in Git. Copying a line's
  folder copies its machines with it.
- Machines are duplicated across lines that want the same one; that is
  the price of a line being changeable on its own.
- Every command takes `--target`, including watch, stop and say.
- "There are no new commits" stops holding from 005, since every
  invocation commits its run's folder; the features say "no new work
  commits" instead.
- The renumbering this came with (a new 003) breaks a cohort's
  `ITERATION` files, so it ships between cohorts.
