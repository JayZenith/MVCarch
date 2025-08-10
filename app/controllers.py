import uuid
from datetime import datetime
from typing import List, Dict, Optional
from .models import Task, TaskRepository


# Takes TaskRepository as dependency to perform ops 
# like creating, retreiving, and listing tasks 
class TaskController:
    def __init__(self, task_repository: TaskRepository):
        self._repository = task_repository
    
    def create_task(self, name: str, scheduled_time: str) -> Dict:
        task_id = str(uuid.uuid4())
        scheduled_dt = datetime.fromisoformat(scheduled_time.replace('Z', '+00:00'))
        task = Task(task_id, name, scheduled_dt)
        saved_task = self._repository.save(task)
        return saved_task.to_dict()
    
    def get_task(self, task_id: str) -> Optional[Dict]:
        task = self._repository.find_by_id(task_id)
        return task.to_dict() if task else None
    
    def get_all_tasks(self) -> List[Dict]:
        tasks = self._repository.find_all()
        return [task.to_dict() for task in tasks]