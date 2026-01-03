"""
Unit tests for the TodoService.
"""

import pytest
from src.services.todo_service import TodoService
from src.models.task import Task


class TestTodoService:
    """Test cases for the TodoService."""

    def setup_method(self):
        """Set up a fresh service instance for each test."""
        self.service = TodoService()

    def test_add_task_success(self):
        """Test adding a task successfully."""
        task = self.service.add_task("Test Task", "Test Description")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed is False

        # Verify the task was added to the service
        tasks = self.service.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].id == 1

    def test_add_task_optional_description(self):
        """Test adding a task with optional description."""
        task = self.service.add_task("Test Task")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description is None
        assert task.completed is False

    def test_add_task_title_validation(self):
        """Test title validation when adding a task."""
        with pytest.raises(ValueError, match="Title is required and cannot be empty"):
            self.service.add_task("")

        with pytest.raises(ValueError, match="Title is required and cannot be empty"):
            self.service.add_task("   ")

        with pytest.raises(ValueError, match="Title must be 255 characters or less"):
            self.service.add_task("x" * 256)

    def test_add_task_description_validation(self):
        """Test description validation when adding a task."""
        with pytest.raises(ValueError, match="Description must be 1000 characters or less"):
            self.service.add_task("Test Task", "x" * 1001)

    def test_get_all_tasks_empty(self):
        """Test getting all tasks when none exist."""
        tasks = self.service.get_all_tasks()

        assert tasks == []

    def test_get_all_tasks_with_tasks(self):
        """Test getting all tasks when they exist."""
        self.service.add_task("Task 1")
        self.service.add_task("Task 2", "Description for Task 2")

        tasks = self.service.get_all_tasks()

        assert len(tasks) == 2
        assert tasks[0].id == 1
        assert tasks[0].title == "Task 1"
        assert tasks[1].id == 2
        assert tasks[1].title == "Task 2"

    def test_get_task_by_id_found(self):
        """Test getting a task by ID when it exists."""
        self.service.add_task("Test Task", "Description")
        task = self.service.get_task_by_id(1)

        assert task is not None
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Description"
        assert task.completed is False

    def test_get_task_by_id_not_found(self):
        """Test getting a task by ID when it doesn't exist."""
        task = self.service.get_task_by_id(999)

        assert task is None

    def test_update_task_success(self):
        """Test updating a task successfully."""
        self.service.add_task("Original Task", "Original Description")
        updated_task = self.service.update_task(1, "Updated Task", "Updated Description")

        assert updated_task is not None
        assert updated_task.id == 1
        assert updated_task.title == "Updated Task"
        assert updated_task.description == "Updated Description"
        assert updated_task.completed is False

    def test_update_task_partial(self):
        """Test updating only title or description."""
        self.service.add_task("Original Task", "Original Description")

        # Update only title
        updated_task = self.service.update_task(1, title="Updated Title")
        assert updated_task.title == "Updated Title"
        assert updated_task.description == "Original Description"

        # Update only description
        updated_task = self.service.update_task(1, description="Updated Description")
        assert updated_task.title == "Updated Title"
        assert updated_task.description == "Updated Description"

    def test_update_task_not_found(self):
        """Test updating a task that doesn't exist."""
        result = self.service.update_task(999, "New Title")

        assert result is None

    def test_update_task_title_validation(self):
        """Test title validation when updating a task."""
        self.service.add_task("Original Task")

        with pytest.raises(ValueError, match="Title cannot be empty"):
            self.service.update_task(1, title="")

        with pytest.raises(ValueError, match="Title cannot be empty"):
            self.service.update_task(1, title="   ")

        with pytest.raises(ValueError, match="Title must be 255 characters or less"):
            self.service.update_task(1, title="x" * 256)

    def test_update_task_description_validation(self):
        """Test description validation when updating a task."""
        self.service.add_task("Original Task")

        with pytest.raises(ValueError, match="Description must be 1000 characters or less"):
            self.service.update_task(1, description="x" * 1001)

    def test_delete_task_success(self):
        """Test deleting a task successfully."""
        self.service.add_task("Test Task")
        result = self.service.delete_task(1)

        assert result is True
        assert len(self.service.get_all_tasks()) == 0

    def test_delete_task_not_found(self):
        """Test deleting a task that doesn't exist."""
        result = self.service.delete_task(999)

        assert result is False

    def test_toggle_task_status_complete(self):
        """Test toggling a task from incomplete to complete."""
        self.service.add_task("Test Task")
        task = self.service.toggle_task_status(1)

        assert task is not None
        assert task.completed is True

    def test_toggle_task_status_incomplete(self):
        """Test toggling a task from complete to incomplete."""
        self.service.add_task("Test Task")
        self.service.toggle_task_status(1)  # Mark as complete
        task = self.service.toggle_task_status(1)  # Mark as incomplete

        assert task is not None
        assert task.completed is False

    def test_toggle_task_status_not_found(self):
        """Test toggling status of a task that doesn't exist."""
        result = self.service.toggle_task_status(999)

        assert result is None

    def test_auto_generated_ids(self):
        """Test that task IDs are auto-generated sequentially."""
        task1 = self.service.add_task("Task 1")
        task2 = self.service.add_task("Task 2")
        task3 = self.service.add_task("Task 3")

        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3

    def test_clear_all_tasks(self):
        """Test clearing all tasks."""
        self.service.add_task("Task 1")
        self.service.add_task("Task 2")

        self.service.clear_all_tasks()

        tasks = self.service.get_all_tasks()
        assert len(tasks) == 0