"""
Unit tests for the utility functions.
"""

import pytest
from src.lib.utils import validate_task_title, validate_task_description, format_task_display, safe_int_input
from src.models.task import Task
from unittest.mock import patch


class TestUtils:
    """Test cases for the utility functions."""

    def test_validate_task_title_valid(self):
        """Test that valid task titles pass validation."""
        assert validate_task_title("Valid Title") is True
        assert validate_task_title("A") is True  # Minimum length
        assert validate_task_title("x" * 255) is True  # Maximum length

    def test_validate_task_title_invalid(self):
        """Test that invalid task titles fail validation."""
        assert validate_task_title("") is False  # Empty
        assert validate_task_title("   ") is False  # Only whitespace
        assert validate_task_title(None) is False  # None value
        assert validate_task_title("x" * 256) is False  # Too long

    def test_validate_task_description_valid(self):
        """Test that valid task descriptions pass validation."""
        assert validate_task_description("Valid Description") is True
        assert validate_task_description("") is True  # Empty is allowed
        assert validate_task_description("   ") is True  # Whitespace is allowed
        assert validate_task_description("x" * 1000) is True  # Maximum length
        assert validate_task_description(None) is True  # None is allowed

    def test_validate_task_description_invalid(self):
        """Test that invalid task descriptions fail validation."""
        assert validate_task_description("x" * 1001) is False  # Too long

    def test_format_task_display(self):
        """Test formatting a task for display."""
        task = Task(id=1, title="Test Title", description="Test Description", completed=False)
        formatted = format_task_display(task)

        # Check that it contains the expected elements
        assert "1" in formatted  # ID
        assert "Test Title" in formatted  # Title
        assert "Test Description" in formatted  # Description
        assert "Incomplete" in formatted  # Status

        # Test with completed task
        task.completed = True
        formatted_completed = format_task_display(task)
        assert "Complete" in formatted_completed

        # Test with long title (should be truncated)
        long_task = Task(id=2, title="x" * 30, description="Desc", completed=False)
        formatted_long = format_task_display(long_task)
        assert "..." in formatted_long  # Should be truncated

    @patch('builtins.input', return_value='5')
    def test_safe_int_input_valid(self, mock_input):
        """Test safe integer input with valid input."""
        result = safe_int_input("Enter a number: ")
        assert result == 5

    @patch('builtins.input', return_value='5')
    def test_safe_int_input_with_range(self, mock_input):
        """Test safe integer input with range validation."""
        result = safe_int_input("Enter a number: ", min_val=1, max_val=10)
        assert result == 5

    @patch('builtins.input', return_value='invalid')
    def test_safe_int_input_invalid(self, mock_input):
        """Test safe integer input with invalid input."""
        with pytest.raises(ValueError, match="not a valid integer"):
            safe_int_input("Enter a number: ")

    @patch('builtins.input', return_value='0')
    def test_safe_int_input_below_min(self, mock_input):
        """Test safe integer input below minimum value."""
        with pytest.raises(ValueError, match="must be at least 1"):
            safe_int_input("Enter a number: ", min_val=1)

    @patch('builtins.input', return_value='15')
    def test_safe_int_input_above_max(self, mock_input):
        """Test safe integer input above maximum value."""
        with pytest.raises(ValueError, match="must be at most 10"):
            safe_int_input("Enter a number: ", max_val=10)