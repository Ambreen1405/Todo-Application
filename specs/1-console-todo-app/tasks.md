---
description: "Task list for Console Todo Application implementation"
---

# Tasks: Console Todo Application

**Input**: Design documents from `/specs/1-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Test tasks included as specified in feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/, tests/
- [X] T002 Initialize Python project with requirements.txt and setup.py
- [ ] T003 [P] Configure linting and formatting tools (pylint, black, flake8)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create Task model in src/models/task.py
- [X] T005 [P] Create TodoService in src/services/todo_service.py
- [X] T006 Create CLI interface framework in src/cli/main.py
- [X] T007 Setup in-memory storage mechanism in src/services/todo_service.py
- [X] T008 Configure error handling utilities in src/lib/utils.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add a Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks with required title and optional description

**Independent Test**: Can be fully tested by starting the application, selecting the add task option, providing a title and description, and verifying the task appears in the list. Delivers the core value of allowing users to create tasks.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T009 [P] [US1] Unit test for Task model validation in tests/unit/test_task.py
- [X] T010 [P] [US1] Contract test for add task functionality in tests/contract/test_add_task.py
- [X] T011 [P] [US1] Integration test for add task workflow in tests/integration/test_cli.py

### Implementation for User Story 1

- [X] T012 [P] [US1] Implement Task model with validation in src/models/task.py
- [X] T013 [US1] Implement add_task method in TodoService in src/services/todo_service.py
- [X] T014 [US1] Implement add task menu option in src/cli/main.py
- [X] T015 [US1] Add validation for required title in src/services/todo_service.py
- [X] T016 [US1] Add auto-generated ID assignment in src/services/todo_service.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P2)

**Goal**: Enable users to see all their tasks with their current status (completed/incomplete)

**Independent Test**: Can be fully tested by adding some tasks and then viewing the complete list. Delivers visibility into all tasks.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T017 [P] [US2] Contract test for view tasks functionality in tests/contract/test_view_tasks.py
- [X] T018 [P] [US2] Integration test for view tasks workflow in tests/integration/test_cli.py

### Implementation for User Story 2

- [X] T019 [US2] Implement get_all_tasks method in TodoService in src/services/todo_service.py
- [X] T020 [US2] Implement view tasks menu option in src/cli/main.py
- [X] T021 [US2] Format task display in tabular format in src/cli/main.py
- [X] T022 [US2] Handle empty task list case in src/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Task Complete/Incomplete (Priority: P3)

**Goal**: Enable users to update the completion status of a specific task by ID

**Independent Test**: Can be fully tested by adding a task, viewing it as incomplete, marking it complete, and verifying the status changed. Delivers task management functionality.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T023 [P] [US3] Contract test for mark task functionality in tests/contract/test_mark_task.py
- [X] T024 [P] [US3] Integration test for mark task workflow in tests/integration/test_cli.py

### Implementation for User Story 3

- [X] T025 [US3] Implement toggle_task_status method in TodoService in src/services/todo_service.py
- [X] T026 [US3] Implement mark task menu option in src/cli/main.py
- [X] T027 [US3] Add validation for valid task ID in src/services/todo_service.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task by ID (Priority: P4)

**Goal**: Enable users to modify the details of an existing task by providing its ID

**Independent Test**: Can be fully tested by adding a task, updating its details, and verifying the changes. Delivers task editing functionality.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T028 [P] [US4] Contract test for update task functionality in tests/contract/test_update_task.py
- [X] T029 [P] [US4] Integration test for update task workflow in tests/integration/test_cli.py

### Implementation for User Story 4

- [X] T030 [US4] Implement update_task method in TodoService in src/services/todo_service.py
- [X] T031 [US4] Implement update task menu option in src/cli/main.py
- [X] T032 [US4] Add validation for valid task ID in src/services/todo_service.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Task by ID (Priority: P5)

**Goal**: Enable users to remove a task from their list by providing its ID

**Independent Test**: Can be fully tested by adding a task, deleting it, and verifying it's no longer in the list. Delivers task removal functionality.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T033 [P] [US5] Contract test for delete task functionality in tests/contract/test_delete_task.py
- [X] T034 [P] [US5] Integration test for delete task workflow in tests/integration/test_cli.py

### Implementation for User Story 5

- [X] T035 [US5] Implement delete_task method in TodoService in src/services/todo_service.py
- [X] T036 [US5] Implement delete task menu option in src/cli/main.py
- [X] T037 [US5] Add validation for valid task ID in src/services/todo_service.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T038 [P] Documentation updates in README.md
- [X] T039 Error handling for invalid menu selections in src/cli/main.py
- [X] T040 [P] Unit tests for all service methods in tests/unit/
- [X] T041 Input validation for special characters in task details
- [ ] T042 Performance validation for large number of tasks
- [ ] T043 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence