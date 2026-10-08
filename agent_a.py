import uuid

import requests

from schemas import OMMMessage, MessageType


if __name__ == "__main__":
    print("OpenMindMesh Agent A starting...")

    message = OMMMessage(
        message_id=str(uuid.uuid4()),
        message_type=MessageType.TASK_ASSIGN,
        sender="agent-a",
        receiver="agent-b",
        payload={
            "task_id": "task-real-002",
            "objective": "Test real OpenMindMesh protocol communication",
            "input_data": {
                "message": "Hello from Agent A"
            },
        },
    )

    print("\n[A] → TASK_ASSIGN → [B]")

    response = requests.post(
        "http://localhost:8001/message",
        json=message.model_dump(mode="json"),
        timeout=5,
    )

    response.raise_for_status()

    print("[A] ← RESPONSE ← [B]")
    print(response.json())

    print("\nOpenMindMesh protocol message: PASSED")
