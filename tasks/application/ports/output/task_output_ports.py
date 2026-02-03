from abc import ABC

from tasks.domain.models import Task


class TaskOutputPort(ABC):
    def get_next_id(self) -> int:
        pass

    def add(self, task: Task):
        pass

    def get_last(self) -> Task:
        pass
