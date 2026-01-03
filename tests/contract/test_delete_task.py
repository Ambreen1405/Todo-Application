"""
Contract tests for the delete task functionality.
"""

import pytest
from src.services.todo_service import TodoService


class TestDeleteTaskContract:
    """Contract tests for the delete task functionality."""

    def setup_method(self):
        """Set up a fresh service instance for each test."""
        self.service = TodoService()

    def test_delete_task_contract_success(self):
        """
        Contract test for delete task functionality.

        Given: The application has tasks in memory
        When: The user selects the delete task option and provides a valid task ID
        Then: The task is removed from the list
        """
        # Given: Add a task
        task = self.service.add_task("Test Task", "Description")

        # Verify the task exists
        initial_tasks = self.service.get_all_tasks()
        assert len(initial_tasks) == 1
        assert initial_tasks[0].id == task.id

        # When: Delete the task
        result = self.service.delete_task(task.id)

        # Then: Verify the task was deleted
        assert result is True
        final_tasks = self.service.get_all_tasks()
        assert len(final_tasks) == 0

    def test_delete_task_contract_multiple_tasks(self):
        """
        Contract test for delete task functionality with multiple tasks.

        Given: The application has multiple tasks in memory
        When: The user deletes one task
        Then: Only the specified task is removed, others remain
        """
        # Given: Add multiple tasks
        task1 = self.service.add_task("Task 1")
        task2 = self.service.add_task("Task 2")
        task3 = self.service.add_task("Task 3")

        initial_tasks = self.service.get_all_tasks()
        assert len(initial_tasks) == 3

        # When: Delete task 2
        result = self.service.delete_task(task2.id)

        # Then: Verify only task 2 was deleted
        assert result is True
        remaining_tasks = self.service.get_all_tasks()
        assert len(remaining_tasks) == 2

        # Verify task1 and task3 still exist
        remaining_ids = [t.id for t in remaining_tasks]
        assert task1.id in remaining_ids
        assert task3.id in remaining_ids
        assert task2.id not in remaining_ids

    def test_delete_task_contract_invalid_id(self):
        """
        Contract test for delete task functionality with invalid ID.

        Given: The application has tasks in memory
        When: The user selects the delete task option and provides an invalid task ID
        Then: An appropriate error message is displayed
        """
        # Given: Add a task
        self.service.add_task("Test Task")

        # When: Try to delete non-existent task
        result = self.service.delete_task(999)

        # Then: Verify appropriate response
        assert result is False

        # Verify original task still exists
        tasks = self.service.get_all_tasks()
        assert len(tasks) == 1

    def test_delete_task_contract_persistence(self):
        """
        Contract test for delete task persistence.

        Given: A task has been deleted
        When: The task list is retrieved again
        Then: The deleted task does not appear
        """
        # Given: Add a task and delete it
        task = self.service.add_task("Test Task")
        self.service.delete_task(task.id)

        # When: Get all tasks again
        tasks = self.service.get_all_tasks()

        # Then: Verify the task is gone
        assert len(tasks) == 0

        # And verify the task cannot be retrieved by ID
        retrieved_task = self.service.get_task_by_id(task.id)
        assert retrieved_task is None

    def test_delete_task_contract_id_reuse_protection(self):
        """
        Contract test for ID reuse after deletion.

        Given: A task has been deleted
        When: A new task is added
        Then: The new task gets a different ID (no ID reuse)
        """
        # Given: Add and delete a task
        task1 = self.service.add_task("First Task")
        self.service.delete_task(task1.id)

        # When: Add a new task
        task2 = self.service.add_task("Second Task")

        # Then: Verify the new task has a different ID
        assert task2.id != task1.id
        assert task2.id == 2  # Should be the next sequential ID

    def test_delete_task_contract_all_tasks(self):
        """
        Contract test for deleting all tasks.

        Given: The application has multiple tasks in memory
        When: All tasks are deleted
        Then: The task list is empty
        """
        # Given: Add multiple tasks
        task1 = self.service.add_task("Task 1")
        task2 = self.service.add_task("Task 2")
        task3 = self.service.add_task("Task 3")

        # When: Delete all tasks individually
        result1 = self.service.delete_task(task1.id)
        result2 = self.service.delete_task(task2.id)
        result3 = self.service.delete_task(task3.id)

        # Then: Verify all deletions succeeded and list is empty
        assert result1 is True
        assert result2 is True
        assert result3 is True

        tasks = self.service.get_all_tasks()
        assert len(tasks) == 0

    def test_delete_task_contract_get_after_delete(self):
        """
        Contract test for retrieving deleted task.

        Given: A task has been deleted
        When: An attempt is made to retrieve the deleted task
        Then: None is returned
        """
        # Given: Add and delete a task
        task = self.service.add_task("Test Task")
        self.service.delete_task(task.id)

        # When: Try to retrieve the deleted task
        retrieved = self.service.get_task_by_id(task.id)

        # Then: Verify None is returned
        assert retrieved is None

    def test_delete_task_contract_view_after_delete(self):
        """
        Contract test for viewing tasks after deletion.

        Given: A task has been deleted
        When: All tasks are viewed
        Then: The deleted task does not appear in the list
        """
        # Given: Add tasks and delete one
        task1 = self.service.add_task("Task 1")
        task2 = self.service.add_task("Task 2")
        self.service.delete_task(task1.id)

        # When: Get all tasks
        tasks = self.service.get_all_tasks()

        # Then: Verify only task2 remains
        assert len(tasks) == 1
        assert tasks[0].id == task2.id
        assert tasks[0].title == "Task 2"