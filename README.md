# Console Todo Application

A simple in-memory console-based todo application built with Python.

## Features

- Add tasks with titles and optional descriptions
- View all tasks with their completion status
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete
- Menu-driven interface

## Requirements

- Python 3.8 or higher

## Installation

1. Clone or download the repository
2. Navigate to the project directory
3. No additional dependencies required (uses Python standard library only)

## Usage

To run the application:

```bash
python src/cli/main.py
```

Follow the on-screen menu prompts to manage your tasks.

## Project Structure

```
src/
├── models/
│   └── task.py          # Task data model
├── services/
│   └── todo_service.py  # Business logic for todo operations
├── cli/
│   └── main.py          # Console interface and menu system
└── lib/
    └── utils.py         # Utility functions

tests/
├── unit/
│   ├── test_task.py     # Task model tests
│   └── test_todo_service.py  # Todo service tests
├── integration/
│   └── test_cli.py      # CLI integration tests
└── contract/
    ├── test_add_task.py
    ├── test_view_tasks.py
    ├── test_mark_task.py
    ├── test_update_task.py
    └── test_delete_task.py
```

## Architecture

The application follows a clean architecture pattern with separation of concerns:

- **Models**: Define data structures (Task model)
- **Services**: Contain business logic (TodoService)
- **CLI**: Handle user interface and input/output
- **Lib**: Utility functions

## Testing

To run the tests:

```bash
pytest tests/
```

The application includes unit, integration, and contract tests to ensure functionality and reliability.# Todo-Application
# Todo-Application
# Todo-Application
# Todo-Application
