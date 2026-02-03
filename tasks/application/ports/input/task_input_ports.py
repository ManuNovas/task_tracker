from abc import ABC

from tasks.application.ports.output import TaskOutputPort


class TaskInputPort(ABC):
    output: TaskOutputPort

    def __init__(self, output: TaskOutputPort):
        self.output = output

    def add(self, description: str) -> int:
        pass
