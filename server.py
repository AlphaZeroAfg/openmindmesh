from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict


app = FastAPI(title="OpenMindMesh Agent")


class TaskRequest(BaseModel):
    task_id: str
    objective: str
    input_data: Dict[str, Any] = {}


@app.get("/health")
def health():
    return {
        "status": "ok",
        "protocol": "OpenMindMesh",
        "version": "0.1",
    }


@app.post("/task")
def receive_task(task: TaskRequest):
    return {
        "status": "received",
        "task_id": task.task_id,
        "objective": task.objective,
        "input_data": task.input_data,
    }
