"""
Contract tests for the add task functionality.
"""

import pytest
from src.services.todo_service import TodoService


class TestAddTaskContract:
    """Contract tests for the add task functionality."""

    def setup_method(self):
        """Set up a fresh service instance for each test."""
        self.service = TodoService()

    def test_add_task_contract_success(self):
        """
        Contract test for add task functionality.

        Given: The console application is running
        When: The user selects the add task option and provides a title
        Then: A new task with the provided title is created with a unique ID and marked as incomplete
        """
        # When: Add a task with a title
        task = self.service.add_task("Test Task")

        # Then: Verify the task has the provided title, unique ID, and is incomplete
        assert task.title == "Test Task"
        assert task.id == 1
        assert task.completed is False

    def test_add_task_contract_with_description(self):
        """
        Contract test for add task functionality with description.

        Given: The console application is running
        When: The user selects the add task option and provides both a title and description
        Then: A new task with the provided title and description is created with a unique ID and marked as incomplete
        """
        # When: Add a task with title and description
        task = self.service.add_task("Test Task", "Test Description")

        # Then: Verify the task has the provided title, description, unique ID, and is incomplete
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.id == 1
        assert task.completed is False

    def test_add_task_contract_unique_ids(self):
        """
        Contract test for unique ID generation.

        Given: The application has tasks in memory
        When: The user adds multiple tasks
        Then: Each task has a unique ID
        """
        # When: Add multiple tasks
        task1 = self.service.add_task("Task 1")
        task2 = self.service.add_task("Task 2")
        task3 = self.service.add_task("Task 3")

        # Then: Verify all IDs are unique
        ids = [task1.id, task2.id, task3.id]
        assert len(ids) == len(set(ids))  # All IDs are unique
        assert ids == [1, 2, 3]  # Sequential IDs

    def test_add_task_contract_default_status(self):
        """
        Contract test for default completion status.

        Given: A new task is being created
        When: The task is added
        Then: The task is marked as incomplete by default
        """
        # When: Add a task
        task = self.service.add_task("Test Task")

        # Then: Verify the task is incomplete by default
        assert task.completed is False

    def test_add_task_contract_title_required(self):
        """
        Contract test for required title validation.

        Given: User tries to add a task
        When: The user provides an empty title
        Then: An appropriate error is raised
        """
        # When/Then: Verify empty title raises an error
        with pytest.raises(ValueError, match="Title is required and cannot be empty"):
            self.service.add_task("")

        with pytest.raises(ValueError, match="Title is required and cannot be empty"):
            self.service.add_task("   ")  # Only whitespace

    def test_add_task_contract_title_length_limit(self):
        """
        Contract test for title length validation.

        Given: User tries to add a task
        When: The user provides a title longer than 255 characters
        Then: An appropriate error is raised
        """
        # When/Then: Verify long title raises an error
        long_title = "x" * 256  # 256 characters, exceeding the limit
        with pytest.raises(ValueError, match="Title must be 255 characters or less"):
            self.service.add_task(long_title)

    def test_add_task_contract_description_length_limit(self):
        """
        Contract test for description length validation.

        Given: User tries to add a task with description
        When: The user provides a description longer than 1000 characters
        Then: An appropriate error is raised
        """
        # When/Then: Verify long description raises an error
        long_description = "x" * 1001  # 1001 characters, exceeding the limit
        with pytest.raises(ValueError, match="Description must be 1000 characters or less"):
            self.service.add_task("Test Task", long_description)

    def test_add_task_contract_task_persistence(self):
        """
        Contract test for task persistence in memory.

        Given: A task has been added
        When: The service is queried for all tasks
        Then: The added task is present in the list
        """
        # Given: Add a task
        added_task = self.service.add_task("Test Task")

        # When: Get all tasks
        all_tasks = self.service.get_all_tasks()

        # Then: Verify the added task is in the list
        assert len(all_tasks) == 1
        assert all_tasks[0].id == added_task.id
        assert all_tasks[0].title == added_task.title
        assert all_tasks[0].completed == added_task.completed