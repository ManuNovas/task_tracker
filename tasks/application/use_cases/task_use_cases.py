from datetime import datetime

from tasks.application.ports.input import TaskInputPort
from tasks.domain.enums import TaskStatus
from tasks.domain.models import Task


class TaskUseCases(TaskInputPort):
    def add(self, description: str) -> int:
        task = Task(
            id=self.output.get_next_id(),
            description=description,
            status=TaskStatus.TODO,
            createdAt=datetime.now(),
            updatedAt=None
        )
        self.output.add(task.to_dict())
        return task.id
