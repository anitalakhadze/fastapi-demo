from fastapi import APIRouter, HTTPException
from typing import List
from app.models.tasks import Task

router = APIRouter()

tasks = []

@router.post("/tasks", response_model=Task, status_code=201)
def create_task(task: Task):
    task.id = len(tasks) + 1
    tasks.append(task)
    return task

@router.get("/tasks", response_model=List[Task], status_code=200)
def get_tasks():
    return tasks

@router.get("/tasks/{task_id}", response_model=Task, status_code=200)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/tasks/{task_id}", response_model=Task, status_code=200)
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasls/{task_id}", status_code=204)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            deleted_task = tasks.pop(index)
            return deleted_task;
    raise HTTPException(status_code=404, detail="Task not found")