from datetime import datetime
from json import load, dump
from os.path import exists

from tasks.application.ports.output import TaskOutputPort
from tasks.domain.enums import TaskStatus
from tasks.domain.models import Task


class TaskJsonRepository(TaskOutputPort):
    FILE_PATH = "./tasks.json"
    data: list[dict]

    @staticmethod
    def to_task(data: dict) -> Task:
        return Task(
            id=data["id"],
            description=data["description"],
            status=TaskStatus(data["status"]),
            createdAt=datetime.fromisoformat(data["createdAt"]),
            updatedAt=datetime.fromisoformat(data["updatedAt"]) if data["updatedAt"] else None,
        )

    def open(self):
        if not exists(self.FILE_PATH):
            with open(self.FILE_PATH, "w") as file:
                file.write("[]")
        with open(self.FILE_PATH, "r") as file:
            self.data = load(file)

    def get_next_id(self) -> int:
        self.open()
        return (self.data[-1]["id"] + 1) if len(self.data) > 0 else 1

    def save(self):
        with open(self.FILE_PATH, "w") as file:
            dump(self.data, file)

    def add(self, task: Task):
        self.open()
        self.data.append(task.to_dict())
        self.save()

    def get_last(self) -> Task:
        self.open()
        return self.to_task(self.data[-1])
