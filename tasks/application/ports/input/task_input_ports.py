from abc import ABC, abstractmethod

from tasks.application.ports.output import TaskOutputPort
from tasks.domain.enums import TaskStatus


class TaskInputPort(ABC):
    output: TaskOutputPort

    def __init__(self, output: TaskOutputPort):
        self.output = output

    @abstractmethod
    def add(self, description: str) -> int:
        pass

    @abstractmethod
    def update(self, task_id: int, description: str) -> bool:
        pass

    @abstractmethod
    def delete(self, task_id: int) -> bool:
        pass

    @abstractmethod
    def mark_in_progress(self, task_id: int) -> bool:
        pass

    @abstractmethod
    def mark_done(self, task_id: int) -> bool:
        pass

    @abstractmethod
    def list(self, status: TaskStatus | None) -> list[dict]:
        pass
