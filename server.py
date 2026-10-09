
from datetime import datetime, timezone, timedelta
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict

from crypto import verify_signature
from schemas import (
    OMMMessage,
    MessageType,
    EvidenceRecord,
    VerificationOutcome,
)


app = FastAPI(title="OpenMindMesh Agent")

SEEN_MESSAGE_IDS = set()
MAX_MESSAGE_AGE = timedelta(minutes=5)


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


@app.post("/message")
def receive_message(message: OMMMessage):
    message_data = message.model_dump(mode="json")
    signature = message_data.pop("signature", None)

    if message.message_type not in (
        MessageType.TASK_ASSIGN,
        MessageType.VERIFY_REQUEST,
    ):
        return {
            "status": "rejected",
            "reason": "Message type is not yet supported securely",
        }

    public_key = message.payload.get("sender_public_key")

    if not public_key or not signature:
        return {
            "status": "rejected",
            "reason": "Missing public key or signature",
        }

    try:
        valid = verify_signature(
            message_data,
            signature,
            public_key,
        )
    except (ValueError, TypeError):
        valid = False

    if not valid:
        return {
            "status": "rejected",
            "reason": "Invalid message signature",
        }

    try:
        timestamp = datetime.fromisoformat(
            message.timestamp.replace("Z", "+00:00")
        )
        now = datetime.now(timezone.utc)

        if timestamp.tzinfo is None:
            timestamp = timestamp.replace(tzinfo=timezone.utc)

        if abs(now - timestamp) > MAX_MESSAGE_AGE:
            return {
                "status": "rejected",
                "reason": "Message timestamp outside allowed window",
            }
    except (ValueError, TypeError):
        return {
            "status": "rejected",
            "reason": "Invalid message timestamp",
        }

    if message.message_id in SEEN_MESSAGE_IDS:
        return {
            "status": "rejected",
            "reason": "Duplicate message ID",
        }

    SEEN_MESSAGE_IDS.add(message.message_id)

    if message.message_type == MessageType.TASK_ASSIGN:
        return {
            "status": "verified",
            "message_id": message.message_id,
            "message_type": message.message_type,
            "sender": message.sender,
            "receiver": message.receiver,
            "signature_valid": True,
            "message": "TASK_ASSIGN verified successfully",
        }

    evidence = EvidenceRecord(
        **message.payload["evidence"]
    )

    if evidence.uncertainty_score <= 0.5:
        outcome = VerificationOutcome.VERIFIED
    else:
        outcome = VerificationOutcome.UNCERTAIN

    return {
        "status": "verified",
        "message_type": MessageType.VERIFY_RESULT,
        "task_id": message.payload["task_id"],
        "target_agent_id": message.sender,
        "signature_valid": True,
        "outcome": outcome.value,
        "evidence_check": evidence.model_dump(mode="json"),
    }
