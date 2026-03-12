"""JSON persistence helpers for todos."""

from __future__ import annotations

import json
import logging
from pathlib import Path

from .models import Todo

LOGGER = logging.getLogger(__name__)


def load_todos(path: str) -> list[Todo]:
    """Load todos from JSON storage."""
    file_path = Path(path)
    if not file_path.exists():
        _create_storage_file(file_path)
        return []

    try:
        raw_value = json.loads(file_path.read_text(encoding="utf-8"))
        if not isinstance(raw_value, list):
            raise ValueError("JSON root must be a list")
        return [Todo.from_dict(item) for item in raw_value]
    except (json.JSONDecodeError, TypeError, ValueError, OSError) as exc:
        LOGGER.warning("Failed to load todos from %s: %s", file_path, exc)
        return []


def save_todos(path: str, todos: list[Todo]) -> None:
    """Save todos to JSON storage."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    payload = [todo.to_dict() for todo in todos]
    file_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _create_storage_file(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("[]\n", encoding="utf-8")

