# Todo App med pytest

Beginner-friendly desktop todo list app built with Python and `ttkbootstrap`.

## Project layout

```text
src/todo_app/
  __init__.py
  main.py
  models.py
  storage.py
  ui.py
tests/
  conftest.py
  test_models.py
  test_storage.py
data/
  todos.json  # created automatically
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the app

```bash
PYTHONPATH=src python3 -m todo_app.main
```

## Run checks

```bash
ruff check .
pytest -q
```
