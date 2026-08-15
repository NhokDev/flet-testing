# AGENTS.md

Operative rules for AI sessions working in this repo. Full details live in `docs/`. Read `docs/evolution.md`, `docs/workflow.md`, and `docs/organization.md` before significant work.

## Commands (Windows/PowerShell, `uv run`)

```powershell
uv run flet run src/main.py     # run the app
uv run ruff check .             # lint
uv run ruff format --check .    # format check
uv run pytest                   # tests
```

## Rules

1. EVERY new feature MUST follow the cycle in `docs/evolution.md`: proposal (user) → specification (agent) → coding via TDD (agent) → verification (user). Do not skip steps.
2. TDD is mandatory: write the failing test first, then implement, then refactor. Tests are part of the definition of done, not an afterthought.
3. Separate UI from logic: the Flet page only wires events; state, actions, and persistence live in a logic layer that never imports `flet`, so it stays unit-testable (see `docs/organization.md`).
4. Quality gates before anything is done: ruff check clean, ruff format --check clean, all tests pass.
5. Commits: conventional commits, English messages, no AI attribution lines.
6. Docs are English, neutral-professional register. Update them when a rule or the structure changes.

## Layout at a glance

`src/main.py` entry point · `src/assets/` images + sounds · `tests/` pytest suite · `docs/` this documentation set.
