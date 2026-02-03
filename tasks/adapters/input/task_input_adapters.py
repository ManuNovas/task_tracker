from tasks.application.ports.input import TaskInputPort


class TaskCliAdapter:
    input_port: TaskInputPort

    def __init__(self, input_port: TaskInputPort):
        self.input_port = input_port

    def main(self, argv: list[str]) -> int:
        argl = len(argv)
        if argl < 2:
            print("You should specify a command to continue")
            return 1
        if argv[1] == "add" and argl == 3:
            description = argv[2]
            task_id = self.input_port.add(description)
            print(f"Task {task_id} added")
        else:
            print("Unknown command or not enough arguments to continue")
            return 2
        return 0
