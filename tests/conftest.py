"""Shared fixtures for kerygma-profiles tests."""

from pathlib import Path

import pytest


PROFILES_DIR = Path(__file__).parent.parent / "profiles"


@pytest.fixture
def profiles_dir():
    """Path to the real profiles directory."""
    return PROFILES_DIR


@pytest.fixture
def tmp_profiles(tmp_path):
    """Create a temporary profiles directory with sample profiles."""
    profiles = tmp_path / "profiles"
    profiles.mkdir()

    default = profiles / "_default.yaml"
    default.write_text(
        "profile_id: _default\n"
        "display_name: System Default\n"
        "organ: null\n"
        "repos: []\n"
        "voice:\n"
        "  tone: institutional\n"
        "  hashtags: ['#test']\n"
        "  tagline: Test system\n"
        "platforms:\n"
        "  mastodon:\n"
        "    instance_url: https://mastodon.social\n"
        "    access_token: test-token-literal\n"
        "    visibility: public\n"
        "  discord:\n"
        "    webhook_url: https://discord.com/api/webhooks/test\n"
        "channels:\n"
        "  - channel_id: mastodon-primary\n"
        "    platform: mastodon\n"
        "    max_length: 500\n"
        "    enabled: true\n"
        "rss_feed_url: https://example.com/feed.xml\n"
    )

    project = profiles / "my-product.yaml"
    project.write_text(
        "profile_id: my-product\n"
        "display_name: My Product\n"
        "organ: III\n"
        "repos:\n"
        "  - my-product-repo\n"
        "  - my-product-docs\n"
        "voice:\n"
        "  tone: friendly\n"
        "  hashtags: ['#myproduct', '#saas']\n"
        "  tagline: The best product\n"
        "platforms:\n"
        "  mastodon:\n"
        "    instance_url: https://mastodon.social\n"
        "    access_token: env://MY_PRODUCT_MASTODON_TOKEN\n"
        "    visibility: public\n"
        "channels:\n"
        "  - channel_id: mastodon-product\n"
        "    platform: mastodon\n"
        "    max_length: 500\n"
        "    enabled: true\n"
    )

    return profiles
