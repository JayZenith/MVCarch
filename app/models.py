from datetime import datetime
from typing import List, Dict, Optional

class Task:
    def __init__(self, id: str, name: str, scheduled_time: datetime, status: str = "pending"):
        self.id = id
        self.name = name
        self.scheduled_time = scheduled_time
        self.status = status
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "scheduled_time": self.scheduled_time.isoformat(),
            "status": self.status
        }

class TaskRepository:
    def __init__(self):
        self._tasks: Dict[str, Task] = {}
    
    def save(self, task: Task) -> Task:
        self._tasks[task.id] = task
        return task
    
    def find_by_id(self, task_id: str) -> Optional[Task]:
        return self._tasks.get(task_id)
    
    def find_all(self) -> List[Task]:
        return list(self._tasks.values())