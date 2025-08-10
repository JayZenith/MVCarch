from .models import TaskRepository
from .controllers import TaskController

class Container:
    def __init__(self):
        self._task_repository = None
        self._task_controller = None
    
    @property
    def task_repository(self):
        if self._task_repository is None:
            self._task_repository = TaskRepository()
        return self._task_repository
    
    @property
    def task_controller(self):
        if self._task_controller is None:
            self._task_controller = TaskController(self.task_repository)
        return self._task_controller