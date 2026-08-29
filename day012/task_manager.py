"""
Task:
Implement a task management system using object-oriented programming
and algorithms.

Requirements:
- Create `Task` and `TaskManager` classes.
- A Task has an ID, title, priority, and completion status.
- A TaskManager manages multiple tasks.
- Task IDs must be unique.
- Tasks can be marked as completed.
- The manager can return all incomplete tasks ordered by priority.
- The manager can find the task with the highest priority.
- The manager can calculate the percentage of completed tasks.
"""


class Task:
    def __init__(self, task_id: str, title: str, priority: int) -> None:
        if not task_id or not title:
            raise ValueError("Task id or title can not be empty.")

        if not 1 <= priority <= 5:
            raise ValueError("Priority must be between 1 and 5.")

        self.task_id = task_id
        self.title = title
        self.priority = priority
        self._is_complete: bool = False

    def __eq__(self, other) -> bool:
        if not isinstance(other, Task):
            return NotImplemented

        return self.task_id == other.task_id

    def complete(self) -> None:
        self._is_complete = True


class TaskManager:
    def __init__(self) -> None:
        self.tasks: list[Task] = []

    def _find_incomplete(self) -> list[Task]:
        return [task for task in self.tasks if not task._is_complete]

    def add_task(self, task: Task) -> None:
        for existing_task in self.tasks:
            if existing_task == task:
                raise ValueError("Task has already added in TaskManager.")

        self.tasks.append(task)

    def complete_task(self, task_id: str) -> None:
        for task in self.tasks:
            if task.task_id == task_id:
                task.complete()
                return

        raise ValueError("Unknown task.")

    def incomplete_tasks(self) -> list[Task]:
        incompleted_tasks = self._find_incomplete()

        return sorted(incompleted_tasks, key=lambda task: task.priority, reverse=True)

    def highest_priority_task(self) -> Task | None:
        incompleted_tasks = self._find_incomplete()

        if not incompleted_tasks:
            return None

        return max(incompleted_tasks, key=lambda task: task.priority)

    def completion_percentage(self) -> float:
        if not self.tasks:
            return 0.0

        completed = len(self.tasks) - len(self._find_incomplete())

        return completed / len(self.tasks) * 100
