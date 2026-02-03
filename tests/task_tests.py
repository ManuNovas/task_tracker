from unittest import TestCase

from tasks.adapters.input import TaskCliAdapter
from tasks.adapters.output import TaskJsonRepository
from tasks.application.use_cases import TaskUseCases


class TaskTests(TestCase):
    repository: TaskJsonRepository
    adapter: TaskCliAdapter

    def setUp(self) -> None:
        self.repository = TaskJsonRepository()
        use_cases = TaskUseCases(self.repository)
        self.adapter = TaskCliAdapter(use_cases)

    def test_without_command(self):
        code = self.adapter.main(["main.py"])
        self.assertEqual(code, 1)

    def test_add_success(self):
        description = "Learn python basis"
        code = self.adapter.main(["main.py", "add", description])
        task = self.repository.get_last()
        self.assertEqual(code, 0)
        self.assertEqual(description, task["description"])
