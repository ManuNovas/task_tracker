from json import load, dump
from os.path import exists

from tasks.application.ports.output import TaskOutputPort


class TaskJsonRepository(TaskOutputPort):
    FILE_PATH = "./tasks.json"
    data: list[dict]

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

    def add(self, task: dict):
        self.open()
        self.data.append(task)
        self.save()

    def get_last(self) -> dict:
        self.open()
        return self.data[-1]

    def get_by_id(self, task_id: int) -> dict | None:
        self.open()
        for data in self.data:
            if data["id"] == task_id:
                return data
        return None

    def update(self, task: dict) -> bool:
        self.open()
        i = 0
        for data in self.data:
            if data["id"] == task["id"]:
                self.data[i] = task
                self.save()
                return True
            i += 1
        return False
