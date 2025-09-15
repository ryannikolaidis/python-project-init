# Contributing Guide

> **Goal:** Make this repo instantly grok‑able for both humans and agentic coding agents. All public code must be well‑documented, important interfaces clearly flagged, and every script must print rich, copy‑pasteable usage help.

---

## Philosophy

* **Clarity over cleverness.** Prefer explicit, boring solutions with great docs.
* **Interfaces first.** The repo's "public surface" is easy to find, annotated, and documented.
* **Single source of truth for running the stack.** No hidden Docker invocations or surprise side‑effects.

---

## Documentation Standards (required)

1. **Module/API docs:** Every public function, class, or module has a docstring/header comment with:

   * What it does, inputs/outputs, error cases, example usage.
2. **Examples:** Provide a minimal example for each public entrypoint.
3. **Type hints:** Use language‑native typing (e.g., TypeScript types/JSDoc, Python type hints, Go types) for public APIs.
4. **Doc coverage:** Public APIs without docs cannot merge (CI enforces).

---

## Important Interfaces (how to flag them)

Mark interfaces in code using a lightweight, grep‑able annotation **and** add a short page under `/docs/interfaces/`.

### Inline annotation (choose the style for your language)

**Generic block:**

```
/*
@interface: NameOfInterface
@purpose: What this interface is for
@stability: experimental|stable
@inputs: ...
@outputs: ...
@owner: team-or-handle
*/
```

**Python:**

```python
# @interface NameOfInterface | stability:stable | owner:@individual
# inputs: ... | outputs: ...
class NameOfInterface:
    ...
```

**TypeScript/JS (TSDoc):**

```ts
/**
 * @interface NameOfInterface
 * @stability stable
 * @owner @individual
 * @inputs ...
 * @outputs ...
 */
export interface NameOfInterface { /* ... */ }
```

**Bash header for CLI interface files:**

```bash
# @interface NameOfCLI | stability:experimental | owner:@team
# inputs: env vars, flags | outputs: stdout JSON
```

### Interface page stub (`/docs/interfaces/<name>.md`)

```
# <NameOfInterface>
- **Stability:** stable | experimental
- **Owner:** @team
- **Location:** path/to/file
- **Summary:** one paragraph
- **Inputs/Outputs:**
- **Examples:** code samples
- **Change log:** human‑written notes for breaking changes
```

> **Tip:** Add a simple `INTERFACES.md` index that links every interface page.

---

## Script Standards (super detailed `--help` output)

All executables in `/scripts` must:

* Be runnable directly (`chmod +x`) and shebang‑correct.
* Support `-h/--help` printing **Usage**, **Options**, **Environment**, **Examples**, and **Exit codes**.
* Support `--dry-run` when safe/applicable.
* Print machine‑parsable output when `--json` is passed.
* See examples:
  * `/scripts/templates/_template.sh`
  * `/scripts/templates/_template_uv.py` - **inline declared dependencies so no venv management needed!**
  * `/scripts/templates/_template.py`
* For bash scripts, assume modern bash > version 5, not the old version shipped with MacOS.

## How to Run the Stack (zero surprises)

* The canonical instructions live in `/docs/running.md`.
* Prefer `docker compose` over ad‑hoc `docker` calls. All Dockerfiles live in `/deploy/`.
* **No hidden Docker actions:** Scripts in `/scripts` **must not** build or run containers. If a script needs containers, it should print: *"Please use `make docker-up` (see docs/running.md)."*
* Minimal required commands:

  * `make dev` — local dev stack (compose or native, documented)
  * `make docker-up` / `make docker-build` — explicit container lifecycle

`/docs/running.md` should include:

* Prereqs (Docker version, runtime, env vars)
* One‑command start/stop + logs
* How to run tests, seed data, debug
* Common failures & remedies

---

## Commit & PR Process

* Use conventional commits (e.g., `feat:`, `fix:`, `docs:`). Commit messages must mention interfaces they touch (e.g., `BREAKING(IFaceName): ...`).
* PR checklist (CI enforces):

  * [ ] Public APIs have docs & examples
  * [ ] New/changed interfaces updated under `/docs/interfaces/`
  * [ ] `docs/running.md` stays accurate
  * [ ] Scripts respond to `--help` with required sections

---

## Tooling & CI (recommended defaults)

* **Pre‑commit hooks:** formatting, linting, docstyle

  * Shell: `shellcheck`
  * Docker: `hadolint`
  * Markdown: `markdownlint`
  * YAML: `yamllint`
* **Doc coverage:** fail PR if public items lack docs (e.g., pydocstyle/tsdoc check)
* **Link check:** verify README/docs links

---

## Architecture Decisions (ADRs)

* Add concise ADRs under `/docs/decisions/` using the format `YYYY‑MM‑DD-title.md`.
* Keep <2 pages; link related interfaces.

---

## Security & Secrets

* No secrets in the repo. Use `.env.example` to document required variables.
* If a secret is needed for local dev, document how to obtain it in `/docs/running.md`.

---