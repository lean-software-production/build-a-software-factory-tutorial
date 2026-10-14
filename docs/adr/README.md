# Architecture Decision Records

Decisions about how this tutorial is built, recorded so we can see what we
decided, when, and why. Each record follows [adr_template.md](adr_template.md).

## Adding one

1. Copy `adr_template.md` to `NNNN-short-title.md` (next number).
2. Fill in the title, date, status, context, decision, and consequences.
3. Add a row to the ledger below.

`adrgen` (see `adrgen.config.yml`) automates steps 1 and 3.

## Ledger

| ADR | Title | Status |
|---|---|---|
| [0001](0001-use-adrs.md) | use ADRs | accepted |
| [0002](0002-students-write-their-own-test-doubles.md) | students write their own test doubles | accepted |
| [0003](0003-fan-out-is-edges-on-the-line.md) | fan out is edges on the line | accepted |
| [0004](0004-lines-own-their-machines-and-runs.md) | lines own their machines and runs | accepted |

## Not in here

These records are decisions about how the course is built. What a
student's factory must do is specified as Gherkin in each iteration's
`features/`, and how they must build it is in the Rules section of that
iteration's `README.md`.
