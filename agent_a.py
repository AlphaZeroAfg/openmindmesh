import uuid

import requests

from crypto import generate_keypair, sign_omm_message
from schemas import OMMMessage, MessageType


if __name__ == "__main__":
    print("OpenMindMesh Agent A starting...")

    private_key, public_key = generate_keypair()

    message = OMMMessage(
        message_id=str(uuid.uuid4()),
        message_type=MessageType.TASK_ASSIGN,
        sender="agent-a",
        receiver="agent-b",
        payload={
            "task_id": "task-real-003",
            "objective": "Test signed OpenMindMesh communication",
            "input_data": {
                "message": "Hello from signed Agent A"
            },
            "sender_public_key": public_key,
        },
    )

    message_data = message.model_dump(mode="json")

    message.signature = sign_omm_message(
        message_data,
        private_key,
    )

    print("\n[A] → SIGNED TASK_ASSIGN → [B]")

    response = requests.post(
        "http://localhost:8001/message",
        json=message.model_dump(mode="json"),
        timeout=5,
    )

    response.raise_for_status()

    print("[A] ← RESPONSE ← [B]")
    print(response.json())

    print("\nOpenMindMesh signed message: SENT")
