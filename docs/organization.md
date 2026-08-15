# Project Organization

## Current structure

```text
flet-testing/
├── src/
│   ├── assets/
│   │   ├── images/
│   │   └── sounds/
│   └── main.py          # entry point: builds the Flet page, wires events
├── tests/
│   └── test_main.py
├── docs/                # this documentation set
├── .python-version
├── pyproject.toml
├── uv.lock
├── AGENTS.md
└── README.md
```

## The architectural principle: UI separate from logic

This is the single most important rule of the project.

**Keep the Flet UI thin.** The Flet page only wires events to actions. All state, rules, and persistence live in a logic layer that does NOT import Flet, so every behavior can be unit-tested with plain pytest — fast, deterministic, no UI required.

Proposed shape (evolves as features land):

```text
src/
├── main.py            # entry point: builds the Flet page, wires events
├── state/             # pet state + actions (pure logic, no flet imports)
│   ├── pet.py         # pet model: hunger, happiness, energy, etc.
│   └── actions.py     # feed(), play(), tick() ... pure functions over state
├── storage/           # persistence: local JSON store, profiles, reset
└── ui/                # optional, only if the page outgrows main.py
```

Rule of thumb: if a function touches `ft.*`, it lives in the UI layer; if it changes state, it lives in the logic layer and gets a test.

## Persistence

- **Where state lives:** a local JSON file (e.g., `.data/store.json`), loaded at startup and saved on every meaningful action.
- **Profiles:** stored state is keyed by profile. Each profile is an independent pet; `default` is the first profile.
- **Reset:** reset clears the active profile's data (or the whole store, by explicit design choice) back to a fresh pet — and that behavior is tested.
- **Structure:** storage functions belong to the logic layer; `main.py` only calls them and renders the result.

## Feature → file mapping convention

- A feature touches the logic layer first (state/actions plus tests), then the UI.
- One feature = one focused change: its spec, its tests, its code, its commit.
- Tests live in `tests/`, mirroring the source layout (e.g., `tests/state/test_pet.py`).
- Names are explicit: `feed`, `play`, `reset_profile` — say what they do.
