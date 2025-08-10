import pytest
import sys
import os

# Add the parent directory to the path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
from unittest.mock import Mock
from app.models import Task, TaskRepository
from app.controllers import TaskController
from app.views import create_app
from app.container import Container

class TestTask:
    def test_task_creation(self):
        task = Task("1", "Test", datetime.now())
        assert task.id == "1"
        assert task.name == "Test"
        assert task.status == "pending"
    
    def test_task_to_dict(self):
        dt = datetime(2024, 1, 1, 12, 0, 0)
        task = Task("1", "Test", dt)
        result = task.to_dict()
        assert result["id"] == "1"
        assert result["name"] == "Test"

class TestTaskRepository:
    def test_save_and_find(self):
        repo = TaskRepository()
        task = Task("1", "Test", datetime.now())
        
        saved = repo.save(task)
        assert saved == task
        
        found = repo.find_by_id("1")
        assert found == task
    
    def test_find_all(self):
        repo = TaskRepository()
        task1 = Task("1", "Test1", datetime.now())
        task2 = Task("2", "Test2", datetime.now())
        
        repo.save(task1)
        repo.save(task2)
        
        all_tasks = repo.find_all()
        assert len(all_tasks) == 2

class TestTaskController:
    def test_create_task(self, mocker):
        mock_repo = Mock()
        mock_task = Mock()
        mock_task.to_dict.return_value = {"id": "1", "name": "Test"}
        mock_repo.save.return_value = mock_task
        
        controller = TaskController(mock_repo)
        result = controller.create_task("Test", "2024-01-01T12:00:00")
        
        assert result == {"id": "1", "name": "Test"}
        mock_repo.save.assert_called_once()
    
    def test_get_task(self):
        mock_repo = Mock()
        mock_task = Mock()
        mock_task.to_dict.return_value = {"id": "1"}
        mock_repo.find_by_id.return_value = mock_task
        
        controller = TaskController(mock_repo)
        result = controller.get_task("1")
        
        assert result == {"id": "1"}
        mock_repo.find_by_id.assert_called_once_with("1")

class TestViews:
    @pytest.fixture
    def app(self):
        container = Container()
        app = create_app(container)
        app.config['TESTING'] = True
        return app
    
    @pytest.fixture
    def client(self, app):
        return app.test_client()
    
    def test_create_task_endpoint(self, client):
        response = client.post('/api/tasks', 
            json={'name': 'Test', 'scheduled_time': '2024-01-01T12:00:00Z'})
        assert response.status_code == 201
    
    def test_get_tasks_endpoint(self, client):
        response = client.get('/api/tasks')
        assert response.status_code == 200
        assert isinstance(response.json, list)