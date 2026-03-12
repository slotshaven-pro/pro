"""Domain models and pure todo list helpers."""

from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(slots=True)
class Todo:
    """Simple todo item model."""

    id: str
    title: str
    completed: bool
    created_at: str

    def to_dict(self) -> dict[str, object]:
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Todo":
        todo_id = str(data["id"])
        title = str(data["title"])
        completed = bool(data["completed"])
        created_at = str(data["created_at"])
        return cls(
            id=todo_id,
            title=title,
            completed=completed,
            created_at=created_at,
        )


def create_todo(title: str) -> Todo:
    """Create a todo from user input."""
    clean_title = title.strip()
    if not clean_title:
        msg = "Todo title cannot be empty."
        raise ValueError(msg)

    return Todo(
        id=str(uuid4()),
        title=clean_title,
        completed=False,
        created_at=_iso_utc_now(),
    )


def toggle_todo(todos: list[Todo], todo_id: str) -> list[Todo]:
    """Flip the completed flag for a single todo by id."""
    updated: list[Todo] = []
    for todo in todos:
        if todo.id == todo_id:
            updated.append(replace(todo, completed=not todo.completed))
        else:
            updated.append(todo)
    return updated


def delete_todo(todos: list[Todo], todo_id: str) -> list[Todo]:
    """Remove a todo by id."""
    return [todo for todo in todos if todo.id != todo_id]


def clear_completed(todos: list[Todo]) -> list[Todo]:
    """Remove all completed todos."""
    return [todo for todo in todos if not todo.completed]


def format_todo(todo: Todo) -> str:
    """Format a todo for display in the list widget."""
    marker = "[x]" if todo.completed else "[ ]"
    return f"{marker} {todo.title}"


def _iso_utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

