from abc import ABC, abstractmethod

from tasks.application.ports.output import TaskOutputPort


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
