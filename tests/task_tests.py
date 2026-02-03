from datetime import datetime
from unittest import TestCase

from tasks.adapters.input import TaskCliAdapter
from tasks.adapters.output import TaskJsonRepository
from tasks.application.use_cases import TaskUseCases
from tasks.domain.enums import TaskStatus


class TaskTests(TestCase):
    repository: TaskJsonRepository
    adapter: TaskCliAdapter

    def setUp(self) -> None:
        self.repository = TaskJsonRepository()
        use_cases = TaskUseCases(self.repository)
        self.adapter = TaskCliAdapter(use_cases)

    def add_task(self) -> dict:
        task = {
            "id": self.repository.get_next_id(),
            "description": "Learn python basis",
            "status": TaskStatus.TODO.value,
            "createdAt": datetime.now().isoformat(),
            "updatedAt": None,
        }
        self.repository.add(task)
        return task

    def test_without_command(self):
        code = self.adapter.main(["main.py"])
        self.assertEqual(code, 1)

    def test_add_success(self):
        description = "Learn python basis"
        code = self.adapter.main(["main.py", "add", description])
        task = self.repository.get_last()
        self.assertEqual(code, 0)
        self.assertEqual(description, task["description"])

    def test_update_success(self):
        task = self.add_task()
        description = "Learn python basis updated"
        code = self.adapter.main(["main.py", "update", task["id"], description])
        updated_task = self.repository.get_by_id(task["id"])
        self.assertEqual(code, 0)
        self.assertEqual(description, updated_task["description"])

    def test_update_not_found(self):
        code = self.adapter.main(["main.py", "update", "-1", "Learn python basis updated"])
        self.assertEqual(code, 3)

    def test_unknown_command(self):
        code = self.adapter.main(["main.py", "patch"])
        self.assertEqual(code, 2)
