from datetime import datetime
from dataclasses import dataclass


@dataclass
class Task:
    desc: str
    status: str = "todo"
    created_at: str = datetime.now().isoformat()
    updated_at: str = datetime.now().isoformat()

    def update_status(self, new_status):
        self.status = new_status
        self.updated_at = datetime.now().isoformat()
