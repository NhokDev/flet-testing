# Flet Testing

A **virtual pet** app (Tamagotchi/Pou-style) built as a functional sandbox for learning **Python + Flet** with serious engineering practices: test-first development, persistent state, multiple profiles, and state reset — all inside a documented workflow.

## Quick start

Requirements: `uv` (it manages Python, the virtual environment, and dependencies).

```powershell
uv sync
uv run flet run src/main.py
```

## Commands

```powershell
uv run flet run src/main.py     # run the app
uv run ruff check .             # lint
uv run ruff format --check .    # format check
uv run pytest                   # tests
```

## Documentation

- [`docs/objective.md`](docs/objective.md) — what this project is, and what it is not.
- [`docs/workflow.md`](docs/workflow.md) — commands, commits, testing culture, quality gates, definition of done.
- [`docs/organization.md`](docs/organization.md) — structure, UI/logic separation, persistence.
- [`docs/evolution.md`](docs/evolution.md) — the four-step feature evolution cycle.
