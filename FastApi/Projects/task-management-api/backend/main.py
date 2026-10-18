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

class TaskUpdate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5, max_length=500)
    status: str
    priority: str

class TaskPatch(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=100
    )

    description: str | None = Field(
        default=None,
        min_length=5,
        max_length=500
    )

    status: str | None = None
    priority: str | None = None

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
def update_task(task_id: int, task_data: TaskUpdate):

    for index, task in enumerate(tasks):

        if task["id"] == task_id:

            updated_task = {
                "id": task_id,
                **task_data.model_dump()
            }

            tasks[index] = updated_task

            return {
                "message": "Task updated successfully",
                "task": updated_task
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.patch("/api/v1/tasks/{task_id}")
def patch_task(task_id: int, task_data: TaskPatch):

    for task in tasks:

        if task["id"] == task_id:

            update_data = task_data.model_dump(
                exclude_unset=True
            )

            task.update(update_data)

            return {
                "message": "Task partially updated",
                "task": task
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.delete("/api/v1/tasks/{task_id}")
def delete_task(task_id: int):

    for index, task in enumerate(tasks):

        if task["id"] == task_id:

            deleted_task = tasks.pop(index)

            return {
                "message": "Task deleted successfully",
                "task": deleted_task
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )