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
