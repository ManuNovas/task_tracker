from sys import argv

from tasks.adapters.input import TaskCliAdapter
from tasks.adapters.output import TaskJsonRepository
from tasks.application.use_cases import TaskUseCases

repository = TaskJsonRepository()
use_cases = TaskUseCases(repository)
adapter = TaskCliAdapter(use_cases)

adapter.main(argv)
