"""
Unit tests for the Task model.
"""

import pytest
from src.models.task import Task


class TestTask:
    """Test cases for the Task model."""

    def test_task_creation_valid(self):
        """Test creating a valid task."""
        task = Task(id=1, title="Test Task", description="Test Description", completed=False)

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed is False

    def test_task_creation_optional_description(self):
        """Test creating a task with optional description."""
        task = Task(id=1, title="Test Task", completed=True)

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description is None
        assert task.completed is True

    def test_task_creation_default_completed(self):
        """Test creating a task with default completed status."""
        task = Task(id=1, title="Test Task")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.completed is False

    def test_task_title_required(self):
        """Test that task title is required."""
        with pytest.raises(ValueError, match="Title is required and cannot be empty"):
            Task(id=1, title="")

        with pytest.raises(ValueError, match="Title is required and cannot be empty"):
            Task(id=1, title="   ")

        with pytest.raises(ValueError, match="Title is required and cannot be empty"):
            Task(id=1, title=None)

    def test_task_title_length_limit(self):
        """Test that task title has a length limit."""
        long_title = "x" * 256  # 256 characters, exceeding the limit

        with pytest.raises(ValueError, match="Title must be 255 characters or less"):
            Task(id=1, title=long_title)

    def test_task_description_length_limit(self):
        """Test that task description has a length limit."""
        long_description = "x" * 1001  # 1001 characters, exceeding the limit

        with pytest.raises(ValueError, match="Description must be 1000 characters or less"):
            Task(id=1, title="Test Task", description=long_description)

    def test_task_completed_must_be_boolean(self):
        """Test that completed status must be boolean."""
        with pytest.raises(ValueError, match="Completed status must be boolean"):
            Task(id=1, title="Test Task", completed="true")

        with pytest.raises(ValueError, match="Completed status must be boolean"):
            Task(id=1, title="Test Task", completed=1)

    def test_task_id_must_be_positive(self):
        """Test that task ID must be positive."""
        with pytest.raises(ValueError, match="ID must be a positive integer"):
            Task(id=0, title="Test Task")

        with pytest.raises(ValueError, match="ID must be a positive integer"):
            Task(id=-1, title="Test Task")