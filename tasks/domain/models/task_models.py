from datetime import datetime

from tasks.domain.enums import TaskStatus


class Task:
    id: int
    description: str
    status: TaskStatus
    createdAt: datetime
    updatedAt: datetime | None

    def __init__(self, id: int, description: str, status: TaskStatus, createdAt: datetime, updatedAt: datetime | None):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status.value,
            "createdAt": self.createdAt.isoformat(),
            "updatedAt": self.updatedAt.isoformat() if self.updatedAt else None,
        }
