# Copyright (c) 2022-2026 Kirkland Yuknis. All rights reserved.
# Source available for viewing only — see LICENSE.txt for terms.

"""
Shared utilities for cl-sdk study notebooks.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
ASSETS_DIR = ROOT / "assets"


def load_env() -> None:
    """Load .env from project root."""
    load_dotenv(ROOT / ".env")


def get_env(key: str, required: bool = True) -> str:
    """Retrieve an env var, raising clearly if required and missing."""
    value = os.environ.get(key)
    if required and not value:
        raise EnvironmentError(
            f"Required environment variable '{key}' is not set. "
            f"Copy .env.example to .env and fill in your values."
        )
    return value or ""
