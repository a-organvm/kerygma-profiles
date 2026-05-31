# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

`kerygma_profiles` — per-project social identity profiles for ORGAN-VII (Kerygma). Enables multi-tenant distribution where each project (or product) can have its own social accounts, voice, hashtags, and content calendar.

## Package Structure

Source is in `kerygma_profiles/`, installed as the `kerygma_profiles` package:

| Module | Purpose |
|--------|---------|
| `registry.py` | `ProfileRegistry` — loads YAML profiles from a directory, resolves which profile applies to a repo name (falls back to `_default`). `ProjectProfile` dataclass holds identity config. |
| `secrets.py` | `resolve_secret()` — resolves `op://` (1Password CLI), `env://` (env var), or literal strings. Caches in memory. Falls back to `KERYGMA_PROFILE_*` env vars if `op` CLI unavailable. |
| `cli.py` | CLI entry point (`kerygma-profiles`): `list`, `show <id>`, `validate [id]`. |

## Profiles

Profile YAML files live in `profiles/` directory. Each `.yaml` file defines:
- `profile_id` — unique identifier (e.g., `_default`, `my-product`)
- `display_name` — human-readable name
- `repos` — list of repo names this profile applies to (empty = fallback)
- `voice` — tone, hashtags, tagline
- `platforms` — per-platform credentials (using `op://` or `env://` references)
- `channels` — channel configurations with max_length and enabled flags
- `calendar` — project-specific calendar events

## Development Commands

```bash
pip install -e .[dev]
pytest tests/ -v
ruff check kerygma_profiles/
```

## Key Design Details

- **Secret resolution is lazy** — secrets are only resolved when `resolve_secret()` is called, not at profile load time. This allows validation to report unresolvable secrets without failing the load.
- **_default profile** — when no profile's `repos` list matches a given repo name, the registry falls back to `_default`. If no `_default` is loaded, `resolve()` raises `KeyError`.
- **1Password fallback** — if `op` CLI is not available, `op://vault/item/field` references fall back to env var `KERYGMA_PROFILE_{ITEM}_{FIELD}` (uppercased, hyphens to underscores).
- **No runtime dependencies beyond pyyaml** — subprocess calls to `op` are best-effort.

<!-- ORGANVM:AUTO:START -->
## System Context (auto-generated — do not edit)

**Organ:** ORGAN-VII (Marketing) | **Tier:** infrastructure | **Status:** GRADUATED
**Org:** `organvm-vii-kerygma` | **Repo:** `kerygma-profiles`

### Edges
- **Produces** → `ORGAN-IV`: profile_registry

### Siblings in Marketing
`announcement-templates`, `social-automation`, `distribution-strategy`, `.github`, `kerygma-pipeline`

### Governance
- *Standard ORGANVM governance applies*

*Last synced: 2026-05-23T00:26:31Z*

## Active Handoff Protocol

If `.conductor/active-handoff.md` exists, **READ IT FIRST** before doing any work.
It contains constraints, locked files, conventions, and completed work from the
originating agent. You MUST honor all constraints listed there.

If the handoff says "CROSS-VERIFICATION REQUIRED", your self-assessment will
NOT be trusted. A different agent will verify your output against these constraints.

## Session Review Protocol

At the end of each session that produces or modifies files:
1. Run `organvm session review --latest` to get a session summary
2. Check for unimplemented plans: `organvm session plans --project .`
3. Export significant sessions: `organvm session export <id> --slug <slug>`
4. Run `organvm prompts distill --dry-run` to detect uncovered operational patterns

Transcripts are on-demand (never committed):
- `organvm session transcript <id>` — conversation summary
- `organvm session transcript <id> --unabridged` — full audit trail
- `organvm session prompts <id>` — human prompts only


## System Library

Plans: 269 indexed | Chains: 5 available | SOPs: 8 active
Discover: `organvm plans search <query>` | `organvm chains list` | `organvm sop lifecycle`
Library: `/Users/4jp/Code/organvm/praxis-perpetua/library`


## Active Directives

| Scope | Phase | Name | Description |
|-------|-------|------|-------------|
| system | any | atomic-clock | The Atomic Clock |
| system | any | execution-sequence | Execution Sequence |
| system | any | multi-agent-dispatch | Multi-Agent Dispatch |
| system | any | session-handoff-avalanche | Session Handoff Avalanche |
| system | any | system-loops | System Loops |
| system | any | prompting-standards | Prompting Standards |
| system | any | background-task-resilience | background-task-resilience |
| system | any | context-window-conservation | context-window-conservation |
| system | any | session-self-critique | session-self-critique |
| system | any | the-descent-protocol | the-descent-protocol |
| system | any | the-membrane-protocol | the-membrane-protocol |
| system | any | theory-to-concrete-gate | theory-to-concrete-gate |
| system | any | triangulation-protocol | triangulation-protocol |

Linked skills: SOP-TRIADIC-REVIEW-PROTOCOL, cicd-resilience-and-recovery, continuous-learning-agent, evaluation-to-growth, genesis-dna, multi-agent-workforce-planner, promotion-and-state-transitions, quality-gate-baseline-calibration, repo-onboarding-and-habitat-creation, session-self-critique, structural-integrity-audit, the-membrane-protocol, triple-reference


**Prompting (Anthropic)**: context 200K tokens, format: XML tags, thinking: extended thinking (budget_tokens)


## Atomization Pipeline

Run `organvm atoms pipeline --write && organvm atoms fanout --write` to generate task queue.


## System Density (auto-generated)

AMMOI: 25% | Edges: 0 | Tensions: 0 | Clusters: 0 | Adv: 27 | Events(24h): 37975
Structure: 8 organs / 148 repos / 1654 components (depth 17) | Inference: 0% | Organs: META-ORGANVM:63%, ORGAN-I:53%, ORGAN-II:48%, ORGAN-III:54% +5 more
Last pulse: 2026-05-23T00:26:28 | Δ24h: n/a | Δ7d: n/a


## Dialect Identity (Trivium)

**Dialect:** SIGNAL_PROPAGATION | **Classical Parallel:** Astronomy | **Translation Role:** The Broadcast — structure-preserving projection to external

Strongest translations: III (structural), VI (analogical), I (analogical)

Scan: `organvm trivium scan VII <OTHER>` | Matrix: `organvm trivium matrix` | Synthesize: `organvm trivium synthesize`


## Logos Documentation Layer

**Status:** ACTIVE | **Symmetry:** 0.5 (DREAM)

Nature demands a documentation counterpart. This formation maintains its narrative record in `docs/logos/`.

### The Tetradic Counterpart
- **[Telos (Idealized Form)](../docs/logos/telos.md)** — The dream and theoretical grounding.
- **[Pragma (Concrete State)](../docs/logos/pragma.md)** — The honest account of what exists.
- **[Praxis (Remediation Plan)](../docs/logos/praxis.md)** — The attack vectors for evolution.
- **[Receptio (Reception)](../docs/logos/receptio.md)** — The account of the constructed polis.

### Alchemical I/O
- **[Source & Transmutation](../docs/logos/alchemical-io.md)** — Narrative of inputs, process, and returns.



*Compliance: Record exists without implementation.*

<!-- ORGANVM:AUTO:END -->
