"""
Contract tests for the view tasks functionality.
"""

import pytest
from src.services.todo_service import TodoService


class TestViewTasksContract:
    """Contract tests for the view tasks functionality."""

    def setup_method(self):
        """Set up a fresh service instance for each test."""
        self.service = TodoService()

    def test_view_tasks_contract_with_tasks(self):
        """
        Contract test for view all tasks functionality with tasks.

        Given: The application has tasks in memory
        When: The user selects the view tasks option
        Then: All tasks are displayed with their ID, title, description, and completion status
        """
        # Given: Add some tasks
        task1 = self.service.add_task("Task 1", "Description 1")
        task2 = self.service.add_task("Task 2")
        task3 = self.service.add_task("Task 3", "Description 3")
        self.service.toggle_task_status(2)  # Mark task 2 as complete

        # When: Get all tasks
        all_tasks = self.service.get_all_tasks()

        # Then: Verify all tasks are returned with correct attributes
        assert len(all_tasks) == 3

        # Check each task
        assert all_tasks[0].id == task1.id
        assert all_tasks[0].title == "Task 1"
        assert all_tasks[0].description == "Description 1"
        assert all_tasks[0].completed is False

        assert all_tasks[1].id == task2.id
        assert all_tasks[1].title == "Task 2"
        assert all_tasks[1].description is None
        assert all_tasks[1].completed is True  # Toggled to complete

        assert all_tasks[2].id == task3.id
        assert all_tasks[2].title == "Task 3"
        assert all_tasks[2].description == "Description 3"
        assert all_tasks[2].completed is False

    def test_view_tasks_contract_empty(self):
        """
        Contract test for view tasks functionality with no tasks.

        Given: The application has no tasks in memory
        When: The user selects the view tasks option
        Then: A message indicates that there are no tasks to display
        """
        # Given: No tasks in the system

        # When: Get all tasks
        all_tasks = self.service.get_all_tasks()

        # Then: Verify empty list is returned
        assert len(all_tasks) == 0

    def test_view_tasks_contract_persistence(self):
        """
        Contract test for task persistence during view operations.

        Given: Tasks exist in memory
        When: The view operation is performed multiple times
        Then: The same tasks are returned each time
        """
        # Given: Add some tasks
        self.service.add_task("Task 1", "Description 1")
        self.service.add_task("Task 2")

        # When: Get all tasks multiple times
        tasks_first_call = self.service.get_all_tasks()
        tasks_second_call = self.service.get_all_tasks()

        # Then: Verify the same tasks are returned
        assert len(tasks_first_call) == 2
        assert len(tasks_second_call) == 2
        assert tasks_first_call[0].id == tasks_second_call[0].id
        assert tasks_first_call[1].id == tasks_second_call[1].id
        assert tasks_first_call[0].title == tasks_second_call[0].title
        assert tasks_first_call[1].title == tasks_second_call[1].title

    def test_view_tasks_contract_ordering(self):
        """
        Contract test for consistent task ordering.

        Given: Multiple tasks exist
        When: The view operation is performed
        Then: Tasks are returned in a consistent order
        """
        # Given: Add tasks in a specific order
        task1 = self.service.add_task("First Task")
        task2 = self.service.add_task("Second Task")
        task3 = self.service.add_task("Third Task")

        # When: Get all tasks
        tasks = self.service.get_all_tasks()

        # Then: Verify tasks are in the order they were added
        assert tasks[0].id == task1.id
        assert tasks[1].id == task2.id
        assert tasks[2].id == task3.id