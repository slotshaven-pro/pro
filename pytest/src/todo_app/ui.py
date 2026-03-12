"""UI for the todo desktop app."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox

import ttkbootstrap as ttk

from .models import clear_completed, create_todo, delete_todo, format_todo, toggle_todo
from .storage import load_todos, save_todos


class TodoApp:
    """Todo app controller and UI widgets."""

    def __init__(self, root: ttk.Window, data_path: str) -> None:
        self.root = root
        self.data_path = data_path
        self.todos = load_todos(data_path)
        self.visible_todo_ids: list[str] = []

        self.title_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Ready")

        self._build_layout()
        self._refresh_list()

    def _build_layout(self) -> None:
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        input_frame = ttk.Frame(self.root, padding=10)
        input_frame.grid(row=0, column=0, sticky="ew")
        input_frame.columnconfigure(0, weight=1)

        title_entry = ttk.Entry(input_frame, textvariable=self.title_var)
        title_entry.grid(row=0, column=0, sticky="ew", padx=(0, 8))
        title_entry.bind("<Return>", self._on_add_from_event)

        add_button = ttk.Button(input_frame, text="Add", command=self.on_add)
        add_button.grid(row=0, column=1, sticky="ew")

        list_frame = ttk.Frame(self.root, padding=(10, 0, 10, 10))
        list_frame.grid(row=1, column=0, sticky="nsew")
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        self.todo_listbox = tk.Listbox(list_frame, activestyle="none")
        self.todo_listbox.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.todo_listbox.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.todo_listbox.config(yscrollcommand=scrollbar.set)

        actions_frame = ttk.Frame(self.root, padding=(10, 0, 10, 6))
        actions_frame.grid(row=2, column=0, sticky="ew")
        actions_frame.columnconfigure((0, 1, 2), weight=1)

        toggle_button = ttk.Button(actions_frame, text="Toggle Complete", command=self.on_toggle)
        toggle_button.grid(row=0, column=0, sticky="ew", padx=(0, 6))

        delete_button = ttk.Button(actions_frame, text="Delete", command=self.on_delete, bootstyle="danger")
        delete_button.grid(row=0, column=1, sticky="ew", padx=(0, 6))

        clear_button = ttk.Button(actions_frame, text="Clear Completed", command=self.on_clear_completed)
        clear_button.grid(row=0, column=2, sticky="ew")

        status_label = ttk.Label(self.root, textvariable=self.status_var, anchor="w", padding=(10, 0, 10, 10))
        status_label.grid(row=3, column=0, sticky="ew")

    def on_add(self) -> None:
        try:
            new_todo = create_todo(self.title_var.get())
        except ValueError as exc:
            self._set_status(str(exc))
            return

        self.todos.append(new_todo)
        self.title_var.set("")
        self._persist_and_refresh("Todo added.")

    def on_toggle(self) -> None:
        todo_id = self._selected_todo_id()
        if not todo_id:
            self._set_status("Select a todo to toggle.")
            return

        self.todos = toggle_todo(self.todos, todo_id)
        self._persist_and_refresh("Todo updated.")

    def on_delete(self) -> None:
        todo_id = self._selected_todo_id()
        if not todo_id:
            self._set_status("Select a todo to delete.")
            return

        self.todos = delete_todo(self.todos, todo_id)
        self._persist_and_refresh("Todo deleted.")

    def on_clear_completed(self) -> None:
        if not any(todo.completed for todo in self.todos):
            self._set_status("No completed todos to clear.")
            return

        confirmed = messagebox.askyesno(
            title="Clear completed",
            message="Remove all completed todos?",
            parent=self.root,
        )
        if not confirmed:
            self._set_status("Clear completed canceled.")
            return

        self.todos = clear_completed(self.todos)
        self._persist_and_refresh("Completed todos cleared.")

    def _on_add_from_event(self, _event: tk.Event) -> None:
        self.on_add()

    def _selected_todo_id(self) -> str | None:
        selected = self.todo_listbox.curselection()
        if not selected:
            return None
        index = selected[0]
        if index >= len(self.visible_todo_ids):
            return None
        return self.visible_todo_ids[index]

    def _persist_and_refresh(self, status_message: str) -> None:
        save_todos(self.data_path, self.todos)
        self._refresh_list()
        self._set_status(status_message)

    def _refresh_list(self) -> None:
        self.todo_listbox.delete(0, tk.END)
        self.visible_todo_ids = []

        for todo in self.todos:
            self.todo_listbox.insert(tk.END, format_todo(todo))
            self.visible_todo_ids.append(todo.id)

    def _set_status(self, message: str) -> None:
        self.status_var.set(message)

