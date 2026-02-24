"""kerygma-profiles: Per-project social identity for ORGAN VII distribution.

Part of ORGAN VII (Kerygma) — the marketing and distribution layer
of the eight-organ creative-institutional system.
"""

__version__ = "0.1.0"

from kerygma_profiles.registry import ProfileRegistry, ProjectProfile
from kerygma_profiles.secrets import resolve_secret

__all__ = [
    "ProfileRegistry",
    "ProjectProfile",
    "resolve_secret",
]
