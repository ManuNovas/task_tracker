from tasks.application.ports.input import TaskInputPort


class TaskCliAdapter:
    input_port: TaskInputPort

    def __init__(self, input_port: TaskInputPort):
        self.input_port = input_port

    @staticmethod
    def task_not_found(task_id: int) -> int:
        print(f"Task {str(task_id)} not found")
        return 3

    def main(self, argv: list[str]) -> int:
        argl = len(argv)
        if argl < 2:
            print("You should specify a command to continue")
            return 1
        command = argv[1]
        if command == "add" and argl == 3:
            description = argv[2]
            task_id = self.input_port.add(description)
            print(f"Task {str(task_id)} added")
        elif command == "update" and argl == 4:
            task_id = int(argv[2])
            description = argv[3]
            updated = self.input_port.update(task_id, description)
            if updated:
                print(f"Task {str(task_id)} updated")
            else:
                return self.task_not_found(task_id)
        elif command == "delete" and argl == 3:
            task_id = int(argv[2])
            deleted = self.input_port.delete(task_id)
            if deleted:
                print(f"Task {str(task_id)} deleted")
            else:
                return self.task_not_found(task_id)
        else:
            print("Unknown command or not enough arguments to continue")
            return 2
        return 0
