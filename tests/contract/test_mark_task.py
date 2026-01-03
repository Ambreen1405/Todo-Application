"""
Contract tests for the mark task functionality.
"""

import pytest
from src.services.todo_service import TodoService


class TestMarkTaskContract:
    """Contract tests for the mark task functionality."""

    def setup_method(self):
        """Set up a fresh service instance for each test."""
        self.service = TodoService()

    def test_mark_task_contract_toggle_complete(self):
        """
        Contract test for mark task functionality - toggle to complete.

        Given: The application has tasks in memory
        When: The user selects the mark task option and provides a valid task ID
        Then: The task's completion status is toggled (complete becomes incomplete, incomplete becomes complete)
        """
        # Given: Add a task (initially incomplete)
        task = self.service.add_task("Test Task", "Description")

        # Verify initial state
        assert task.completed is False

        # When: Toggle the task status
        toggled_task = self.service.toggle_task_status(task.id)

        # Then: Verify the status was toggled to complete
        assert toggled_task is not None
        assert toggled_task.id == task.id
        assert toggled_task.completed is True

    def test_mark_task_contract_toggle_incomplete(self):
        """
        Contract test for mark task functionality - toggle to incomplete.

        Given: The application has a completed task in memory
        When: The user selects the mark task option and provides the task ID
        Then: The task's completion status is toggled to incomplete
        """
        # Given: Add a task and mark it as complete
        task = self.service.add_task("Test Task", "Description")
        self.service.toggle_task_status(task.id)  # Mark as complete

        # Verify it's complete
        assert task.completed is False  # Original task object doesn't update
        current_task = self.service.get_task_by_id(task.id)
        assert current_task.completed is True

        # When: Toggle the task status again
        toggled_task = self.service.toggle_task_status(task.id)

        # Then: Verify the status was toggled to incomplete
        assert toggled_task is not None
        assert toggled_task.id == task.id
        assert toggled_task.completed is False

    def test_mark_task_contract_invalid_id(self):
        """
        Contract test for mark task functionality with invalid ID.

        Given: The application has tasks in memory
        When: The user selects the mark task option and provides an invalid task ID
        Then: An appropriate error message is displayed
        """
        # Given: Add a task
        self.service.add_task("Test Task")

        # When: Try to toggle status of non-existent task
        result = self.service.toggle_task_status(999)

        # Then: Verify appropriate response
        assert result is None

    def test_mark_task_contract_multiple_tasks(self):
        """
        Contract test for mark task functionality with multiple tasks.

        Given: The application has multiple tasks in memory
        When: The user marks specific tasks as complete/incomplete
        Then: Only the specified task's status changes
        """
        # Given: Add multiple tasks
        task1 = self.service.add_task("Task 1")
        task2 = self.service.add_task("Task 2")
        task3 = self.service.add_task("Task 3")

        # Verify initial states
        all_tasks = self.service.get_all_tasks()
        for task in all_tasks:
            assert task.completed is False

        # When: Mark only task 2 as complete
        self.service.toggle_task_status(task2.id)

        # Then: Verify only task 2's status changed
        updated_task1 = self.service.get_task_by_id(task1.id)
        updated_task2 = self.service.get_task_by_id(task2.id)
        updated_task3 = self.service.get_task_by_id(task3.id)

        assert updated_task1.completed is False
        assert updated_task2.completed is True
        assert updated_task3.completed is False

    def test_mark_task_contract_persistence(self):
        """
        Contract test for mark task status persistence.

        Given: A task's status has been changed
        When: The task is retrieved again
        Then: The new status is preserved
        """
        # Given: Add a task and change its status
        task = self.service.add_task("Test Task")
        self.service.toggle_task_status(task.id)

        # When: Retrieve the task again
        retrieved_task = self.service.get_task_by_id(task.id)

        # Then: Verify the status change was persisted
        assert retrieved_task.completed is True

    def test_mark_task_contract_invalid_input_protection(self):
        """
        Contract test for input validation in mark task functionality.

        Given: The application is running
        When: Invalid input is provided to the toggle function
        Then: Appropriate error handling occurs
        """
        # Given: Add a task
        task = self.service.add_task("Test Task")

        # When: Try to toggle with negative ID
        result = self.service.toggle_task_status(-1)

        # Then: Verify appropriate response
        assert result is None