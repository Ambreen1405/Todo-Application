"""
Integration tests for the CLI interface.
"""

import pytest
from unittest.mock import patch, Mock
from src.cli.main import TodoCLI
from src.services.todo_service import TodoService


class TestTodoCLI:
    """Test cases for the TodoCLI integration."""

    def setup_method(self):
        """Set up a fresh CLI instance for each test."""
        self.cli = TodoCLI()

    @patch('builtins.input', side_effect=['Test Task', 'Test Description'])
    @patch('builtins.print')
    def test_add_task_integration(self, mock_print, mock_input):
        """Test adding a task through the CLI interface."""
        self.cli.add_task()

        # Verify the task was added
        tasks = self.cli.service.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].title == "Test Task"
        assert tasks[0].description == "Test Description"
        assert tasks[0].completed is False

        # Verify success message was printed
        mock_print.assert_called()
        assert any("Task added successfully" in str(call) for call in mock_print.call_args_list)

    @patch('builtins.input', side_effect=['Test Task', ''])  # Empty description
    @patch('builtins.print')
    def test_add_task_optional_description(self, mock_print, mock_input):
        """Test adding a task with optional description through the CLI."""
        self.cli.add_task()

        tasks = self.cli.service.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].title == "Test Task"
        assert tasks[0].description is None

    @patch('builtins.input', side_effect=['', 'Test Task'])  # First try empty, then valid
    @patch('builtins.print')
    def test_add_task_validation_error(self, mock_print, mock_input):
        """Test handling validation errors when adding a task."""
        self.cli.add_task()

        # Verify error message was printed
        mock_print.assert_called()
        assert any("Error:" in str(call) for call in mock_print.call_args_list)

        # Verify no task was added
        tasks = self.cli.service.get_all_tasks()
        assert len(tasks) == 0

    @patch('builtins.input', side_effect=['Test Task 1', 'Test Task 2'])
    @patch('builtins.print')
    def test_view_tasks_multiple(self, mock_print, mock_input):
        """Test viewing multiple tasks through the CLI."""
        # Add two tasks
        self.cli.service.add_task("Test Task 1")
        self.cli.service.add_task("Test Task 2", "Description for Task 2")

        # View tasks
        self.cli.view_tasks()

        # Verify tasks were displayed (by checking print was called)
        mock_print.assert_called()

    @patch('builtins.input', side_effect=['Test Task'])
    @patch('builtins.print')
    def test_view_tasks_single(self, mock_print, mock_input):
        """Test viewing a single task through the CLI."""
        # Add one task
        self.cli.service.add_task("Test Task")

        # View tasks
        self.cli.view_tasks()

        # Verify tasks were displayed
        mock_print.assert_called()

    @patch('builtins.input', side_effect=['Test Task'])
    @patch('builtins.print')
    def test_view_tasks_empty(self, mock_print, mock_input):
        """Test viewing tasks when none exist."""
        # Don't add any tasks

        # View tasks
        self.cli.view_tasks()

        # Verify "No tasks found" message was printed
        assert any("No tasks found" in str(call) for call in mock_print.call_args_list)

    @patch('builtins.input', side_effect=['1', 'Updated Title', 'Updated Description'])
    @patch('builtins.print')
    def test_update_task_integration(self, mock_print, mock_input):
        """Test updating a task through the CLI."""
        # Add a task first
        self.cli.service.add_task("Original Title", "Original Description")

        # Update the task
        self.cli.update_task()

        # Verify the task was updated
        tasks = self.cli.service.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].title == "Updated Title"
        assert tasks[0].description == "Updated Description"

    @patch('builtins.input', side_effect=['999', 'New Title'])  # Non-existent task ID
    @patch('builtins.print')
    def test_update_task_not_found(self, mock_print, mock_input):
        """Test updating a task that doesn't exist."""
        self.cli.update_task()

        # Verify error message was printed
        assert any("not found" in str(call) for call in mock_print.call_args_list)

    @patch('builtins.input', side_effect=['1'])
    @patch('builtins.print')
    def test_delete_task_integration(self, mock_print, mock_input):
        """Test deleting a task through the CLI."""
        # Add a task first
        self.cli.service.add_task("Test Task")

        # Delete the task
        self.cli.delete_task()

        # Verify the task was deleted
        tasks = self.cli.service.get_all_tasks()
        assert len(tasks) == 0

    @patch('builtins.input', side_effect=['999'])  # Non-existent task ID
    @patch('builtins.print')
    def test_delete_task_not_found(self, mock_print, mock_input):
        """Test deleting a task that doesn't exist."""
        self.cli.delete_task()

        # Verify error message was printed
        assert any("not found" in str(call) for call in mock_print.call_args_list)

    @patch('builtins.input', side_effect=['1'])
    @patch('builtins.print')
    def test_mark_task_status_integration(self, mock_print, mock_input):
        """Test marking a task status through the CLI."""
        # Add a task first
        self.cli.service.add_task("Test Task")

        # Mark task as complete
        self.cli.mark_task_status()

        # Verify the task status was updated
        tasks = self.cli.service.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].completed is True

    @patch('builtins.input', side_effect=['999'])  # Non-existent task ID
    @patch('builtins.print')
    def test_mark_task_status_not_found(self, mock_print, mock_input):
        """Test marking status of a task that doesn't exist."""
        self.cli.mark_task_status()

        # Verify error message was printed
        assert any("not found" in str(call) for call in mock_print.call_args_list)

    @patch('builtins.input', side_effect=['2', '6'])  # View tasks then exit
    @patch('builtins.print')
    def test_main_menu_flow(self, mock_print, mock_input):
        """Test basic menu flow."""
        # Add a task first
        self.cli.service.add_task("Test Task")

        # Try to run the menu with a few commands
        self.cli.display_menu()
        choice = self.cli.get_user_choice()

        assert choice == 2  # Should be the '2' we input

    @patch('builtins.input', side_effect=['99', '1', 'Test Task', '6'])  # Invalid then valid
    @patch('builtins.print')
    def test_invalid_menu_choice(self, mock_print, mock_input):
        """Test handling of invalid menu choices."""
        try:
            choice = self.cli.get_user_choice()
            # Should raise ValueError for invalid choice
            assert False, "Expected ValueError for invalid choice"
        except ValueError:
            # This is expected
            pass

    def test_service_initialization(self):
        """Test that the CLI initializes with a TodoService."""
        assert isinstance(self.cli.service, TodoService)