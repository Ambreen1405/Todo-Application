"""
Task model for the Console Todo Application.

This module defines the Task data model with validation rules
as specified in the data model document.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo item with the following attributes:
    - id: Unique identifier (auto-generated)
    - title: Required text describing the task
    - description: Optional text providing more details about the task
    - completed: Boolean indicating completion status
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

    def __post_init__(self):
        """Validate the task attributes after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Title is required and cannot be empty")

        if len(self.title) > 255:
            raise ValueError("Title must be 255 characters or less")

        if self.description and len(self.description) > 1000:
            raise ValueError("Description must be 1000 characters or less")

        if not isinstance(self.completed, bool):
            raise ValueError("Completed status must be boolean")

        if self.id <= 0:
            raise ValueError("ID must be a positive integer")