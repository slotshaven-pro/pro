from __future__ import annotations

from pathlib import Path

from todo_app.models import Todo
from todo_app.storage import load_todos, save_todos


def test_load_todos_creates_missing_file(tmp_path: Path) -> None:
    data_path = tmp_path / "data" / "todos.json"

    todos = load_todos(str(data_path))

    assert todos == []
    assert data_path.exists()


def test_save_and_load_roundtrip(tmp_path: Path) -> None:
    data_path = tmp_path / "todos.json"
    source = [
        Todo(id="1", title="A", completed=False, created_at="2026-01-01T00:00:00+00:00"),
        Todo(id="2", title="B", completed=True, created_at="2026-01-01T00:00:00+00:00"),
    ]

    save_todos(str(data_path), source)
    loaded = load_todos(str(data_path))

    assert loaded == source


def test_load_todos_handles_malformed_json(tmp_path: Path) -> None:
    data_path = tmp_path / "todos.json"
    data_path.write_text("{bad json", encoding="utf-8")

    loaded = load_todos(str(data_path))

    assert loaded == []

