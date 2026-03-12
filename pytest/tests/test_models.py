from __future__ import annotations

from datetime import datetime

import pytest

from todo_app.models import Todo, clear_completed, create_todo, delete_todo, toggle_todo


def test_create_todo_sets_defaults() -> None:
    todo = create_todo("Write tests")

    assert todo.title == "Write tests"
    assert todo.completed is False
    assert todo.id
    assert datetime.fromisoformat(todo.created_at)


def test_create_todo_rejects_blank_title() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        create_todo("   ")


def test_toggle_todo_flips_completion_state() -> None:
    todo = Todo(id="1", title="Task", completed=False, created_at="2026-01-01T00:00:00+00:00")

    updated = toggle_todo([todo], todo_id="1")

    assert updated[0].completed is True
    assert updated[0].id == "1"


def test_delete_todo_removes_item() -> None:
    first = Todo(id="1", title="A", completed=False, created_at="2026-01-01T00:00:00+00:00")
    second = Todo(id="2", title="B", completed=False, created_at="2026-01-01T00:00:00+00:00")

    updated = delete_todo([first, second], todo_id="1")

    assert updated == [second]


def test_clear_completed_keeps_incomplete_only() -> None:
    first = Todo(id="1", title="A", completed=False, created_at="2026-01-01T00:00:00+00:00")
    second = Todo(id="2", title="B", completed=True, created_at="2026-01-01T00:00:00+00:00")

    updated = clear_completed([first, second])

    assert updated == [first]
