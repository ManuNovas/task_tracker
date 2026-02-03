from datetime import datetime

from tasks.application.ports.input import TaskInputPort
from tasks.domain.enums import TaskStatus
from tasks.domain.models import Task


class TaskUseCases(TaskInputPort):
    def add(self, description: str) -> int:
        data = {
            "id": self.output.get_next_id(),
            "description": description,
            "status": TaskStatus.TODO.value,
            "createdAt": datetime.now().isoformat(),
            "updatedAt": None,
        }
        self.output.add(data)
        return data["id"]

    def update(self, task_id: int, description: str) -> bool:
        data = self.output.get_by_id(task_id)
        if data is None:
            return False
        task = Task(data)
        task.set_description(description)
        return self.output.update(task.to_dict())

    def delete(self, task_id: int) -> bool:
        return self.output.delete(task_id)

    def mark_status(self, task_id: int, status: TaskStatus) -> bool:
        data = self.output.get_by_id(task_id)
        if data is None:
            return False
        task = Task(data)
        task.set_status(status)
        return self.output.update(task.to_dict())

    def mark_in_progress(self, task_id: int) -> bool:
        return self.mark_status(task_id, TaskStatus.IN_PROGRESS)

    def mark_done(self, task_id: int) -> bool:
        return self.mark_status(task_id, TaskStatus.DONE)
