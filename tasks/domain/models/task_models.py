from datetime import datetime

from tasks.domain.enums import TaskStatus


class Task:
    id: int
    description: str
    status: TaskStatus
    created_at: datetime
    updated_at: datetime | None

    def __init__(self, data: dict):
        self.id = int(data["id"])
        self.description = data["description"]
        self.status = TaskStatus(data["status"])
        self.created_at = datetime.fromisoformat(data["createdAt"])
        self.updated_at = datetime.fromisoformat(data["updatedAt"]) if data["updatedAt"] else None

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status.value,
            "createdAt": self.created_at.isoformat(),
            "updatedAt": self.updated_at.isoformat() if self.updated_at else None,
        }

    def set_description(self, description: str):
        self.description = description
        self.updated_at = datetime.now()
