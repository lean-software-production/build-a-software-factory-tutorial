# Build a Software Factory tutorial

A hands-on course for building an agentic software factory. Work through the
iterations in order, one homework at a time. They take you from the first
agent loop to a factory you can watch and steer.

## Get started

1. Fork or clone
   [my-factory-starter](https://github.com/lean-software-production/my-factory-starter).
   That is where you work. You don't need to clone this repo.
2. Open your favourite coding agent harness (Claude Code, Codex, Pi,
   etc) at the root of your starter repository. Your factory source
   lives in `factory/` from the first homework on.
3. Say "fetch iteration" to pull the first homework into `factory/spec/`, then
   "coach me". Setup creates the `bin/factory` launcher; once you build
   homework 1, run it from the root with `--seed` and `--target` to select
   what to build and where.

## Where things live

- [Iterations](docs/iterations/README.md) — the homeworks, one folder each.
- [Architecture decisions](docs/adr/README.md) — the ADR ledger.
- [Lexicon](docs/lexicon.yaml) — the vocabulary we use.
- [Reference](docs/reference/README.md) — outside material we borrow from.
