# DISCOVERY — organvm/kerygma-profiles

**Verdict:** VALUE FOUND → promote into the ranked tier.
**Date:** 2026-06-22 (auto-discovery)

## Value Thesis

`kerygma-profiles` is the **multi-tenant social-identity control plane** for the
entire ORGANVM distribution layer — the one place that answers, for any repo in
the estate, *"which accounts, which voice, which hashtags, which channels and
length limits, which secrets, and which content cadence apply when we publish on
its behalf?"* It is not a script or a stub: it is a GRADUATED, production-tier
Python package (v0.1.0) with a clean importable API (`ProfileRegistry.resolve()`,
`resolve_secret()`), a working CLI (`list` / `show` / `validate`), lazy
1Password/env secret resolution with graceful fallback, 24 passing tests, and a
green CI pipeline. Its real latent value is **leverage through multi-tenancy**:
because identity lives here as declarative YAML (7 live product profiles +
`_default` + 18 dissolved, each carrying tone, hashtags, platform credentials,
channel configs, SEO keywords, and calendars), a *single* publishing pipeline can
serve N products without per-product code — exactly the capability ORGAN-IV
delivery, social-automation, and kerygma-pipeline need. The estate already
declares this repo `produces → ORGAN-IV: profile_registry` and "consumed by all
distribution tools," but today that edge is config-by-convention rather than a
hardened, contract-validated dependency. Closing that gap turns an already-useful
library into trustworthy shared infrastructure the whole estate can build on — a
reusable asset (the per-project social-identity-registry pattern itself is
genuinely extractable/open-sourceable). This is the opposite of archival.

## What It Already Does

- **`ProfileRegistry`** (`registry.py`) — loads `*.yaml` profiles from a directory,
  warns on repo-ownership collisions, resolves the profile for a repo name with
  `_default` fallback, raises `KeyError` only when nothing matches and no default
  is loaded.
- **`resolve_secret()`** (`secrets.py`) — resolves `op://` (1Password CLI),
  `env://`, or literal references; in-memory cache; falls back to
  `KERYGMA_PROFILE_*` env vars when the `op` CLI is absent.
- **CLI** (`cli.py`) — `kerygma-profiles list | show <id> | validate [id]`, with
  secret redaction on display and unresolvable-secret reporting on validate.
- **Profiles** (`profiles/`) — `_default` + live products (e.g. `amp-lab-media`
  carries a full YouTube content strategy, SEO keyword sets, and per-format
  cadence) and a `dissolved-2026-03-11/` archive of sunset products.

## Single Best Concrete First Task

**Harden the registry into a validated contract: ship a JSON Schema for the
profile YAML format and wire `kerygma-profiles validate` into CI as a required
gate.** The `validate` command already exists and `_default` already passes; this
task adds (a) a `profiles/profile.schema.json` describing required fields
(`profile_id`, `display_name`, `platforms`, `channels`) and structural shape, (b)
a schema check inside `cmd_validate`, and (c) a CI step running
`kerygma-profiles validate` over all profiles so a malformed or half-authored
profile can never reach a downstream consumer. This is self-contained, keeps the
build green, and directly converts the `produces → ORGAN-IV` edge from convention
into a guaranteed, machine-checked interface — the prerequisite for every other
distribution tool to depend on this repo with confidence.
