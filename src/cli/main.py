"""
Console Todo Application - Main CLI Interface

This module implements the menu-driven console interface
for the todo application as specified in the requirements.
"""

import sys
from typing import Optional
from src.services.todo_service import TodoService


class TodoCLI:
    """
    Console interface for the Todo Application.
    Implements a menu-driven interface with numbered options.
    """

    def __init__(self):
        """Initialize the CLI with a TodoService instance."""
        self.service = TodoService()

    def display_menu(self):
        """Display the main menu options to the user."""
        print("\nConsole Todo Application")
        print("========================")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Exit")
        print()

    def get_user_choice(self) -> int:
        """
        Get and validate user menu choice.

        Returns:
            The user's menu choice (1-6)

        Raises:
            ValueError: If the input is not a valid integer
        """
        choice_str = input("Select an option: ").strip()
        try:
            choice = int(choice_str)
            if 1 <= choice <= 6:
                return choice
            else:
                raise ValueError("Choice must be between 1 and 6")
        except ValueError:
            raise ValueError(f"'{choice_str}' is not a valid menu option. Please enter a number between 1 and 6.")

    def add_task(self):
        """Handle adding a new task."""
        try:
            title = input("Enter task title: ").strip()
            if not title:
                print("Error: Title is required and cannot be empty")
                return

            description_input = input("Enter task description (optional, press Enter to skip): ").strip()
            description = description_input if description_input else None

            task = self.service.add_task(title, description)
            print(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def view_tasks(self):
        """Handle viewing all tasks."""
        tasks = self.service.get_all_tasks()

        if not tasks:
            print("No tasks found")
            return

        # Print header
        print(f"{'ID':<4} {'Title':<20} {'Description':<30} {'Status':<12}")
        print("-" * 70)

        # Print each task
        for task in tasks:
            status = "Complete" if task.completed else "Incomplete"
            description = task.description if task.description else ""
            # Truncate long titles and descriptions for display
            title_display = task.title[:19] + "..." if len(task.title) > 19 else task.title
            desc_display = description[:27] + "..." if len(description) > 27 else description
            print(f"{task.id:<4} {title_display:<20} {desc_display:<30} {status:<12}")

    def update_task(self):
        """Handle updating a task."""
        try:
            task_id_str = input("Enter task ID to update: ").strip()
            task_id = int(task_id_str)

            task = self.service.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found")
                return

            print(f"Current task: {task.title}")
            if task.description:
                print(f"Current description: {task.description}")

            new_title = input("Enter new title (or press Enter to keep current): ").strip()
            new_title = new_title if new_title else None

            new_description = input("Enter new description (or press Enter to keep current): ").strip()
            new_description = new_description if new_description else None

            updated_task = self.service.update_task(task_id, new_title, new_description)
            if updated_task:
                print("Task updated successfully")
            else:
                print("Error: Failed to update task")

        except ValueError as e:
            print(f"Error: {e}")

    def delete_task(self):
        """Handle deleting a task."""
        try:
            task_id_str = input("Enter task ID to delete: ").strip()
            task_id = int(task_id_str)

            success = self.service.delete_task(task_id)
            if success:
                print("Task deleted successfully")
            else:
                print(f"Error: Task with ID {task_id} not found")

        except ValueError as e:
            print(f"Error: {e}")

    def mark_task_status(self):
        """Handle toggling task completion status."""
        try:
            task_id_str = input("Enter task ID to mark complete/incomplete: ").strip()
            task_id = int(task_id_str)

            task = self.service.toggle_task_status(task_id)
            if task:
                status = "Complete" if task.completed else "Incomplete"
                print(f"Task {task_id} marked as {status}")
            else:
                print(f"Error: Task with ID {task_id} not found")

        except ValueError as e:
            print(f"Error: {e}")

    def run(self):
        """Main application loop."""
        print("Welcome to Console Todo Application!")

        while True:
            try:
                self.display_menu()
                choice = self.get_user_choice()

                if choice == 1:
                    self.add_task()
                elif choice == 2:
                    self.view_tasks()
                elif choice == 3:
                    self.update_task()
                elif choice == 4:
                    self.delete_task()
                elif choice == 5:
                    self.mark_task_status()
                elif choice == 6:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select a number between 1 and 6.")

            except ValueError as e:
                print(f"Error: {e}")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


def main():
    """Entry point for the application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()