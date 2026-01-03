"""
TodoService for the Console Todo Application.

This module implements the business logic for todo operations
using in-memory storage as specified in the requirements.
"""

from typing import List, Optional
from src.models.task import Task


class TodoService:
    """
    Business logic layer for todo operations.
    Uses in-memory storage to store tasks during application runtime.
    """

    def __init__(self):
        """Initialize the service with an empty task list and ID counter."""
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task with the provided title and optional description.

        Args:
            title: Required task title
            description: Optional task description

        Returns:
            The created Task object with a unique ID and marked as incomplete

        Raises:
            ValueError: If title is empty or invalid
        """
        # Validate title
        if not title or not title.strip():
            raise ValueError("Title is required and cannot be empty")

        if len(title) > 255:
            raise ValueError("Title must be 255 characters or less")

        if description and len(description) > 1000:
            raise ValueError("Description must be 1000 characters or less")

        # Create task with auto-generated ID
        task = Task(
            id=self._next_id,
            title=title.strip(),
            description=description.strip() if description else None,
            completed=False
        )

        self._tasks.append(task)
        self._next_id += 1

        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the system.

        Returns:
            List of all tasks, or empty list if no tasks exist
        """
        return self._tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The task if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None,
                   description: Optional[str] = None) -> Optional[Task]:
        """
        Update an existing task by its ID.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            The updated task if found, None otherwise

        Raises:
            ValueError: If title is empty when provided
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return None

        # Validate new title if provided
        if title is not None:
            if not title or not title.strip():
                raise ValueError("Title cannot be empty")

            if len(title) > 255:
                raise ValueError("Title must be 255 characters or less")

            task.title = title.strip()

        # Update description if provided
        if description is not None:
            if description and len(description) > 1000:
                raise ValueError("Description must be 1000 characters or less")

            task.description = description.strip() if description else None

        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was deleted, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        self._tasks.remove(task)
        return True

    def toggle_task_status(self, task_id: int) -> Optional[Task]:
        """
        Toggle the completion status of a task by its ID.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            The updated task if found, None otherwise
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return None

        task.completed = not task.completed
        return task

    def clear_all_tasks(self):
        """Clear all tasks from memory."""
        self._tasks.clear()
        self._next_id = 1