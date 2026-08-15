# Project Objective

## What this project is

**Flet Testing** is a virtual pet application (Tamagotchi/Pou-style) built as a *functional sandbox* for learning **Python + Flet** with serious engineering practices. It is neither a toy nor a one-shot tutorial: it is a real GUI application, exercised by a real test suite, organized like a real project.

## Target audience

- Developers learning Flet who want to go beyond "Hello, world" demos.
- Developers who want to practice test-first development and clean architecture in a GUI context.
- AI-assisted development: this repo is designed to be worked on with AI agents under explicit, documented rules.

## Educational purpose

The point is NOT to build the best virtual pet in the world. The point is to practice:

- Separating UI from logic so the app stays testable.
- Writing a test *before* the code that makes it pass.
- Persisting state and resetting it, as a real product would.
- Evolving a codebase feature by feature, with a definition of done for every change.

## Key capabilities

- **Working GUI** — real buttons and actions the user can click.
- **Test shielding** — every action/feature is covered by one or more tests, written test-first.
- **Persistent state** — pet state survives across sessions.
- **State reset** — the user can wipe state back to a fresh pet.
- **Multiple profiles** — independent pets, each with its own stored state.

## Non-goals (honest and short)

- **Production deployment.** No packaging, releases, or real-world distribution.
- **Polish.** No complex animations, sound engineering, or marketing-grade visuals.
- **Monetization.** No store, purchases, or ads, ever.
- **Feature breadth.** Features are added for learning value, not completeness.

## Success criteria

The project succeeds as a *learning vehicle* when:

1. Every committed feature follows the documented evolution cycle (see `docs/evolution.md`).
2. Every feature has its tests written first, and they stay green.
3. Ruff is clean and format-clean at all times.
4. State, profiles, and reset all work, and all are tested.
5. A new developer — or a new AI session — can read the docs and continue the work without asking questions.
