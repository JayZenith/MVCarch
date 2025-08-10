from flask import Flask, request, jsonify, send_from_directory
from .container import Container
import os


# Flask routes (endpoints) and uses TaskController 
# to handle them. Ex) /api/tasks with POST calls create_task
# on te controller 
def create_app(container: Container) -> Flask:
    app = Flask(__name__)
    app.container = container
    
    # Serves the frontend index.html file 
    @app.route('/')
    def index():
        return send_from_directory('../static', 'index.html')
    
    @app.route('/api/tasks', methods=['POST'])
    def create_task():
        data = request.get_json()
        task = app.container.task_controller.create_task(data['name'], data['scheduled_time'])
        return jsonify(task), 201
    
    @app.route('/api/tasks', methods=['GET'])
    def get_tasks():
        tasks = app.container.task_controller.get_all_tasks()
        return jsonify(tasks)
    
    @app.route('/api/tasks/<task_id>', methods=['GET'])
    def get_task(task_id: str):
        task = app.container.task_controller.get_task(task_id)
        if task:
            return jsonify(task)
        return jsonify({'error': 'Task not found'}), 404
    
    return app