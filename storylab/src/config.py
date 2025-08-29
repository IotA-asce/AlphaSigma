"""Load configuration from environment variables."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Dict

REQUIRED_KEYS = [
    "OPENAI_API_KEY",
    "OPENAI_MODEL_ID",
    "GCP_API_KEY",
    "GCP_MODEL_ID",
    "TIMEZONE",
]


def _ensure_no_env_committed(root: Path) -> None:
    """Raise an error if a tracked `.env` file exists."""
    try:
        result = subprocess.run(
            ["git", "ls-files", ".env"],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return
    if result.stdout.strip():
        raise RuntimeError(
            ".env file is committed to git; remove it and use .env.sample"
        )


def _load_env_file(env_path: Path) -> None:
    """Populate ``os.environ`` with values from an ``.env`` file."""
    if not env_path.exists():
        return
    with env_path.open() as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                os.environ.setdefault(key, value)


def load_config() -> Dict[str, str]:
    """Return required configuration values.

    Loads variables from a local ``.env`` file if present and ensures they
    exist in the environment. Raises ``RuntimeError`` if any required key is
    missing or if a ``.env`` file has been committed to git.
    """

    root = Path(__file__).resolve().parents[2]
    env_file = root / ".env"

    _load_env_file(env_file)
    _ensure_no_env_committed(root)

    config = {}
    missing = []
    for key in REQUIRED_KEYS:
        value = os.getenv(key)
        if value:
            config[key] = value
        else:
            missing.append(key)
    if missing:
        raise RuntimeError(
            "Missing required environment variables: " + ", ".join(missing)
        )
    return config
