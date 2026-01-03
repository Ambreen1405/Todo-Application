# Interface Contracts: Console Todo Application

## CLI Interface Contract

### Menu Options
The application presents users with a numbered menu of available operations.

### Input/Output Protocol
- **Input**: User enters a number to select a menu option
- **Output**: Application displays results in a formatted text-based interface

### Operation Contracts

#### 1. Add Task
- **Input**: Menu selection (1), followed by title and optional description
- **Success Output**: Confirmation message with task ID
- **Error Output**: Error message if title is empty
- **Validation**: Title is required and must not be empty

#### 2. View All Tasks
- **Input**: Menu selection (2)
- **Success Output**: Formatted list of all tasks with ID, title, description, and completion status
- **Error Output**: "No tasks found" if no tasks exist
- **Validation**: None

#### 3. Update Task by ID
- **Input**: Menu selection (3), followed by task ID and new details
- **Success Output**: Confirmation message
- **Error Output**: Error message if task ID doesn't exist
- **Validation**: Task ID must exist in the system

#### 4. Delete Task by ID
- **Input**: Menu selection (4), followed by task ID
- **Success Output**: Confirmation message
- **Error Output**: Error message if task ID doesn't exist
- **Validation**: Task ID must exist in the system

#### 5. Mark Task Complete/Incomplete
- **Input**: Menu selection (5), followed by task ID
- **Success Output**: Confirmation message with new status
- **Error Output**: Error message if task ID doesn't exist
- **Validation**: Task ID must exist in the system

#### 6. Exit Application
- **Input**: Menu selection (6)
- **Output**: Goodbye message and application termination
- **Validation**: None

### Error Handling Contract
- All error messages will be clear and informative
- Invalid menu selections will prompt user to try again
- Invalid task IDs will result in appropriate error messages
- Empty inputs where not allowed will be rejected with explanations

### Data Format Contract
- Tasks displayed in tabular format with columns: ID, Title, Description, Status
- Status displayed as "Complete" or "Incomplete"
- IDs displayed as integers
- All text displayed in UTF-8 encoding