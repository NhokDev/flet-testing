# Feature Evolution Cycle

How a feature goes from idea to accepted. This cycle is deliberately SIMPLE — four steps, no heavyweight ceremony.

## The four steps

### 1. Proposal (user)

The user describes the feature or intent in a sentence or two. No format required.

### 2. Specification (agent)

The agent turns the proposal into a concrete spec:

- **Requirements** — what must work.
- **Scenarios** — the main user flows.
- **Edge cases** — what could break (empty name, missing file, invalid input...).
- **Acceptance criteria** — how we know it is done.

The spec must be clear enough to test against.

### 3. Coding via TDD (agent)

The agent implements the feature test-first:

1. Write a failing test for the new behavior.
2. Run it — watch it fail for the right reason.
3. Implement until it passes.
4. Refactor, keeping tests green.

The code stays inside the rules of `docs/organization.md` and passes the quality gates of `docs/workflow.md`.

### 4. Verification (user)

The USER reviews and verifies the result — runs the app, reads the code, asks questions. Nothing is done until the user says so.

## Why this cycle is intentionally simple

Heavyweight SDD (full proposal → spec → tasks → design → apply → verify → archive chains) exists to protect large, multi-agent, production workflows. This project is a personal learning sandbox; that overhead would crush it. These four steps teach the same fundamentals — spec first, test first, verify before accepting — without the ceremony. The agent does the heavy lifting; the user keeps control as the final reviewer.

## The rule

**Every new feature MUST follow these four steps.** Skipping steps — code without a spec, code without tests, code without user verification — is a process violation, not a shortcut.
