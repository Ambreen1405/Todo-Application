# Quickstart Guide: Console Todo Application

## Prerequisites
- Python 3.8 or higher installed on your system
- Basic command line knowledge

## Setup

### 1. Clone or Access the Project
```
# If using a repository:
git clone <repository-url>
cd <project-directory>
```

### 2. Navigate to the Source Directory
```
cd src/cli
```

## Running the Application

### Execute the Application
```
python main.py
```

## Using the Application

### Initial Menu
Upon running the application, you'll see a menu with numbered options:
```
Console Todo Application
========================
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit
```

### Adding a Task
1. Select option `1` to add a task
2. Enter the task title when prompted
3. Optionally enter a description
4. The system will confirm with the new task's ID

### Viewing All Tasks
1. Select option `2` to view all tasks
2. The system will display a formatted list of all tasks with their ID, title, description, and status

### Updating a Task
1. Select option `3` to update a task
2. Enter the task ID when prompted
3. Enter the new title and description
4. The system will confirm the update

### Deleting a Task
1. Select option `4` to delete a task
2. Enter the task ID when prompted
3. The system will confirm the deletion

### Marking Task Complete/Incomplete
1. Select option `5` to toggle task completion
2. Enter the task ID when prompted
3. The system will confirm the new status

### Exiting the Application
1. Select option `6` to exit
2. The application will terminate

## Example Workflow

### Adding and Managing Tasks
```
Console Todo Application
========================
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit

Select an option: 1
Enter task title: Buy groceries
Enter task description (optional): Milk, bread, eggs
Task added successfully with ID: 1

Select an option: 2
ID  Title             Description       Status
--  -----             -----------       ------
1   Buy groceries     Milk, bread, eggs Incomplete

Select an option: 5
Enter task ID: 1
Task 1 marked as Complete

Select an option: 2
ID  Title             Description       Status
--  -----             -----------       ------
1   Buy groceries     Milk, bread, eggs Complete

Select an option: 6
Goodbye!
```

## Error Handling
- If you enter an invalid menu option, the application will prompt you to try again
- If you enter a non-existent task ID, the application will display an appropriate error message
- If you provide an empty title when adding a task, the application will prompt you to enter a valid title

## Troubleshooting
- **Python not found**: Ensure Python 3.8+ is installed and in your PATH
- **Module not found**: Ensure you're running the command from the correct directory
- **Permission error**: Ensure you have read/write permissions for the project directory