from fastapi import FastAPI, HTTPException
from typing import Dict, List

app = FastAPI()

# In-memory database (a simple list to store tasks)
tasks: List[Dict] = []
task_id_counter: int = 1  # Counter to generate unique IDs

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Task Manager with CI/CD, Kubernetes, and Ingress(Nginx)!"}

# Helper function to create a task with an auto-incremented ID
def create_task(task: Dict) -> Dict:
    global task_id_counter
    new_task = task.copy()  # Avoid modifying the input dict
    new_task["id"] = task_id_counter
    task_id_counter += 1
    return new_task

# Endpoint to fetch all tasks
@app.get("/tasks")
def get_tasks() -> List[Dict]:
    return {"tasks": tasks}

# Endpoint to add a new task
@app.post("/tasks")
def add_task(task: Dict):
    task_with_id = create_task(task)  # Automatically assign ID
    tasks.append(task_with_id)
    return {"message": "✅ Task added successfully!", "task": task_with_id}

# Endpoint to update a task by its id
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Dict):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            # Preserve the original id, update other fields
            tasks[i] = {"id": task_id, **updated_task}
            return {"message": "✅ Task updated successfully!", "task": tasks[i]}
    raise HTTPException(status_code=404, detail="❌ Task not found")

# Endpoint to delete a task by its id
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted_task = tasks.pop(i)
            return {"message": "✅ Task deleted successfully!", "task": deleted_task}
    raise HTTPException(status_code=404, detail="❌ Task not found")
