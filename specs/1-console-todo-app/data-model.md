# Data Model: Console Todo Application

## Task Entity

### Attributes
- **id**: Integer
  - Auto-generated unique identifier
  - Primary key for the task
  - Sequential numbering starting from 1

- **title**: String
  - Required field
  - Text describing the task
  - Minimum length: 1 character
  - Maximum length: 255 characters

- **description**: String (Optional)
  - Optional field for additional details
  - Can be empty or null
  - Maximum length: 1000 characters

- **completed**: Boolean
  - Indicates completion status
  - Default value: false
  - Can be toggled between true and false

### Validation Rules
- Title is required and cannot be empty
- ID must be unique across all tasks
- ID must be a positive integer
- Completed status must be boolean (true/false)

### State Transitions
- **Incomplete → Complete**: When user marks task as complete
- **Complete → Incomplete**: When user marks task as incomplete

### Relationships
- No relationships with other entities (standalone entity)

### Example Representation
```python
class Task:
    id: int
    title: str
    description: str (optional)
    completed: bool
```

### Sample Data
```
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, bread, eggs, fruits",
  "completed": false
}
```

### Constraints
- All tasks stored in memory only (no persistence)
- Data exists only during application runtime
- No external dependencies for data storage