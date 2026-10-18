from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="Task Management API",
    version="1.0.0"
)

tasks = []

class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5, max_length=500)
    status: str = "pending"
    priority: str = "medium"


@app.get("/")
def home():
    return {
        "message": "Task Management API is running"
    }


@app.post("/api/v1/tasks")
def create_task(task: TaskCreate):

    new_task = {
        "id": len(tasks) + 1,
        **task.model_dump()
    }

    tasks.append(new_task)

    return {
        "message": "Task created successfully",
        "task": new_task
    }


@app.get("/api/v1/tasks")
def get_tasks():
    return {
        "tasks": tasks
    }

@app.get("/api/v1/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.put("/api/v1/tasks/{task_id}")
def update_task(task_id: int):
    return {
        "message": "Update task",
        "task_id": task_id
    }


@app.patch("/api/v1/tasks/{task_id}")
def patch_task(task_id: int):
    return {
        "message": "Partially update task",
        "task_id": task_id
    }


@app.delete("/api/v1/tasks/{task_id}")
def delete_task(task_id: int):
    return {
        "message": "Delete task",
        "task_id": task_id
    }