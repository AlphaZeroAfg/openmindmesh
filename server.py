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

def sign_omm_message(
    message: Dict[str, Any],
    private_key_hex: str,
) -> str:
    """
    Sign an OpenMindMesh message without including its signature field.
    """
    signable_message = dict(message)
    signable_message.pop("signature", None)

    return sign_message(
        signable_message,
        private_key_hex,
    )
