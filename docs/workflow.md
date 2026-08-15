# Workflow

How we work on this project: commands, commits, testing culture, quality gates, and the definition of done.

## Command cheat-sheet

All commands run from the project root with `uv run`.

```powershell
uv run flet run src/main.py     # run the app (dev mode, hot reload)
uv run ruff check .             # lint
uv run ruff format --check .    # format check
uv run pytest                   # tests
```

## Commits

- Conventional commits (e.g., `feat:`, `fix:`, `test:`, `docs:`, `refactor:`).
- English commit messages.
- No AI attribution lines (no "Co-Authored-By" or similar).

## Testing culture: test-first

Tests are part of the **definition of done**, not an afterthought.

- For every feature: write a failing test first, watch it fail, implement until it passes, then refactor.
- Prefer testing the state/logic layer without the UI (see `docs/organization.md`). Unit tests for logic are fast, deterministic, and the primary safety net.
- UI wiring stays thin; anything that genuinely needs a real Flet test is added where it earns its keep.

## Quality gates

A feature is not done until all of these pass:

1. `uv run ruff check .` — no lint errors.
2. `uv run ruff format --check .` — code is formatted.
3. `uv run pytest` — all tests pass.

## Definition of Done

- [ ] Feature went through the four-step evolution cycle (`docs/evolution.md`).
- [ ] Tests written first: they existed as failing tests for the missing behavior and pass now.
- [ ] The behavior is covered by at least one test.
- [ ] Quality gates pass: ruff check, ruff format --check, pytest.
- [ ] Code follows the organization rules (`docs/organization.md`).
- [ ] Committed with a conventional, English, no-AI-attribution message.

## Branch / PR policy

Simple on purpose:

- `main` is the stable branch and the source of truth.
- Work happens on short-lived feature branches: `feat/<short-name>`.
- Open a Pull Request for any meaningful change; the branch is deleted after merge.
- Keep branches small so reviews (human or AI) stay focused.

No ceremony beyond that. This is a learning project, not a corporation.
