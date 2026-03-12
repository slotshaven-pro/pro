"""Application entrypoint."""

from __future__ import annotations

from pathlib import Path

import ttkbootstrap as ttk

from .ui import TodoApp


def main() -> None:
    app_window = ttk.Window(themename="flatly")
    app_window.title("Todo List")
    app_window.geometry("620x460")

    TodoApp(root=app_window, data_path=str(default_data_path()))

    app_window.mainloop()


def default_data_path() -> Path:
    project_root = Path(__file__).resolve().parents[2]
    return project_root / "data" / "todos.json"


if __name__ == "__main__":
    main()

