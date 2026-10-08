from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict

from schemas import OMMMessage, MessageType


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
    result = {
        "status": "completed",
        "task_id": task.task_id,
        "objective": task.objective,
        "output": {
            "received_input": task.input_data
        },
        "evidence": {
            "claim": "Task input was received and processed",
            "evidence_type": "execution_log",
            "payload": {
                "agent": "openmindmesh-agent"
            },
            "uncertainty_score": 0.0
        }
    }

    return result


@app.post("/message")
def receive_message(message: OMMMessage):
    if message.message_type == MessageType.TASK_ASSIGN:
        return {
            "status": "received",
            "protocol": message.protocol,
            "version": message.version,
            "message_id": message.message_id,
            "message_type": message.message_type,
            "sender": message.sender,
            "receiver": message.receiver,
            "payload": message.payload,
        }

    return {
        "status": "received",
        "message_id": message.message_id,
        "message_type": message.message_type,
    }
