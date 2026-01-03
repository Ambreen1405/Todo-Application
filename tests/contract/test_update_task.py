"""
Contract tests for the update task functionality.
"""

import pytest
from src.services.todo_service import TodoService


class TestUpdateTaskContract:
    """Contract tests for the update task functionality."""

    def setup_method(self):
        """Set up a fresh service instance for each test."""
        self.service = TodoService()

    def test_update_task_contract_success(self):
        """
        Contract test for update task functionality.

        Given: The application has tasks in memory
        When: The user selects the update task option and provides a valid task ID with new details
        Then: The task is updated with the new information
        """
        # Given: Add a task
        original_task = self.service.add_task("Original Title", "Original Description")

        # When: Update the task
        updated_task = self.service.update_task(original_task.id, "New Title", "New Description")

        # Then: Verify the task was updated
        assert updated_task is not None
        assert updated_task.id == original_task.id
        assert updated_task.title == "New Title"
        assert updated_task.description == "New Description"
        assert updated_task.completed == original_task.completed  # Status should remain unchanged

    def test_update_task_contract_partial_update_title(self):
        """
        Contract test for partial update - title only.

        Given: The application has tasks in memory
        When: The user updates only the title
        Then: Only the title changes, other fields remain the same
        """
        # Given: Add a task
        original_task = self.service.add_task("Original Title", "Original Description")

        # When: Update only the title
        updated_task = self.service.update_task(original_task.id, title="New Title")

        # Then: Verify only the title changed
        assert updated_task is not None
        assert updated_task.id == original_task.id
        assert updated_task.title == "New Title"
        assert updated_task.description == "Original Description"  # Should remain unchanged
        assert updated_task.completed == original_task.completed  # Status should remain unchanged

    def test_update_task_contract_partial_update_description(self):
        """
        Contract test for partial update - description only.

        Given: The application has tasks in memory
        When: The user updates only the description
        Then: Only the description changes, other fields remain the same
        """
        # Given: Add a task
        original_task = self.service.add_task("Original Title", "Original Description")

        # When: Update only the description
        updated_task = self.service.update_task(original_task.id, description="New Description")

        # Then: Verify only the description changed
        assert updated_task is not None
        assert updated_task.id == original_task.id
        assert updated_task.title == "Original Title"  # Should remain unchanged
        assert updated_task.description == "New Description"
        assert updated_task.completed == original_task.completed  # Status should remain unchanged

    def test_update_task_contract_invalid_id(self):
        """
        Contract test for update task functionality with invalid ID.

        Given: The application has tasks in memory
        When: The user selects the update task option and provides an invalid task ID
        Then: An appropriate error message is displayed
        """
        # Given: Add a task
        self.service.add_task("Test Task")

        # When: Try to update non-existent task
        result = self.service.update_task(999, "New Title")

        # Then: Verify appropriate response
        assert result is None

    def test_update_task_contract_title_validation(self):
        """
        Contract test for title validation during update.

        Given: The application has tasks in memory
        When: The user updates a task with an empty title
        Then: An appropriate error is raised
        """
        # Given: Add a task
        task = self.service.add_task("Original Title")

        # When/Then: Verify empty title raises an error
        with pytest.raises(ValueError, match="Title cannot be empty"):
            self.service.update_task(task.id, title="")

        with pytest.raises(ValueError, match="Title cannot be empty"):
            self.service.update_task(task.id, title="   ")  # Only whitespace

    def test_update_task_contract_title_length_validation(self):
        """
        Contract test for title length validation during update.

        Given: The application has tasks in memory
        When: The user updates a task with a title longer than 255 characters
        Then: An appropriate error is raised
        """
        # Given: Add a task
        task = self.service.add_task("Original Title")

        # When/Then: Verify long title raises an error
        long_title = "x" * 256  # 256 characters, exceeding the limit
        with pytest.raises(ValueError, match="Title must be 255 characters or less"):
            self.service.update_task(task.id, title=long_title)

    def test_update_task_contract_description_length_validation(self):
        """
        Contract test for description length validation during update.

        Given: The application has tasks in memory
        When: The user updates a task with a description longer than 1000 characters
        Then: An appropriate error is raised
        """
        # Given: Add a task
        task = self.service.add_task("Original Title")

        # When/Then: Verify long description raises an error
        long_description = "x" * 1001  # 1001 characters, exceeding the limit
        with pytest.raises(ValueError, match="Description must be 1000 characters or less"):
            self.service.update_task(task.id, description=long_description)

    def test_update_task_contract_persistence(self):
        """
        Contract test for update task persistence.

        Given: A task has been updated
        When: The task is retrieved again
        Then: The updates are preserved
        """
        # Given: Add a task
        task = self.service.add_task("Original Title", "Original Description")

        # When: Update the task
        self.service.update_task(task.id, "New Title", "New Description")

        # When: Retrieve the task again
        retrieved_task = self.service.get_task_by_id(task.id)

        # Then: Verify the updates were persisted
        assert retrieved_task.title == "New Title"
        assert retrieved_task.description == "New Description"

    def test_update_task_contract_multiple_updates(self):
        """
        Contract test for multiple updates to the same task.

        Given: A task exists
        When: The task is updated multiple times
        Then: Each update is applied correctly
        """
        # Given: Add a task
        task = self.service.add_task("Original Title", "Original Description")

        # When: Multiple updates
        self.service.update_task(task.id, "First Update")
        first_updated = self.service.get_task_by_id(task.id)

        self.service.update_task(task.id, description="Second Update")
        second_updated = self.service.get_task_by_id(task.id)

        # Then: Verify all updates were applied
        assert first_updated.title == "First Update"
        assert first_updated.description == "Original Description"

        assert second_updated.title == "First Update"  # Should remain from first update
        assert second_updated.description == "Second Update"