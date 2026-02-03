from abc import ABC, abstractmethod


class TaskOutputPort(ABC):
    @abstractmethod
    def get_next_id(self) -> int:
        pass

    @abstractmethod
    def add(self, task: dict):
        pass

    @abstractmethod
    def get_last(self) -> dict:
        pass

    @abstractmethod
    def get_by_id(self, task_id: int) -> dict | None:
        pass

    @abstractmethod
    def update(self, task: dict) -> bool:
        pass

    @abstractmethod
    def delete(self, task_id: int) -> bool:
        pass

    @abstractmethod
    def get_all(self, status: str | None) -> list[dict]:
        pass
