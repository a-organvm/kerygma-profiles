"""Secret resolver with 1Password CLI and env var support.

Supports three reference formats:
  - op://vault/item/field  -> 1Password CLI (subprocess: op read)
  - env://VAR_NAME         -> environment variable lookup
  - literal string         -> returned as-is

Caches resolved secrets in memory for the process lifetime.
Falls back to env var convention (KERYGMA_PROFILE_{item}_{field})
if `op` CLI is not available.
"""

from __future__ import annotations

import logging
import os
import subprocess

logger = logging.getLogger("kerygma.profiles.secrets")

_secret_cache: dict[str, str] = {}


def resolve_secret(value: str) -> str:
    """Resolve a secret reference.

    Supports:
    - op://vault/item/field  -> 1Password CLI (subprocess: op read)
    - env://VAR_NAME         -> environment variable
    - literal string         -> returned as-is
    """
    if not isinstance(value, str) or not value:
        return value

    if value.startswith("op://"):
        return _resolve_op(value)

    if value.startswith("env://"):
        var_name = value[6:]
        return os.environ.get(var_name, "")

    return value


def _resolve_op(ref: str) -> str:
    """Resolve a 1Password op:// reference."""
    if ref in _secret_cache:
        return _secret_cache[ref]

    # Try 1Password CLI
    try:
        result = subprocess.run(
            ["op", "read", ref],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode == 0:
            secret = result.stdout.strip()  # allow-secret
            _secret_cache[ref] = secret
            return secret
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: derive env var name from op:// path
    # op://kerygma/mastodon-system/access-token -> KERYGMA_PROFILE_MASTODON_SYSTEM_ACCESS_TOKEN
    parts = ref.replace("op://", "").split("/")
    if len(parts) >= 3:
        env_name = f"KERYGMA_PROFILE_{'_'.join(parts[1:])}".upper().replace("-", "_")
        val = os.environ.get(env_name, "")
        if val:
            _secret_cache[ref] = val
            return val

    logger.warning("Could not resolve secret: %s", ref)  # allow-secret
    return ""


def clear_cache() -> None:
    """Clear the in-memory secret cache."""
    _secret_cache.clear()
