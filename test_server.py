from datetime import datetime, timedelta, timezone

from fastapi.testclient import TestClient

from server import app
from crypto import generate_keypair, sign_omm_message
from schemas import OMMMessage, MessageType


client = TestClient(app)


def make_signed_message(message_id, timestamp=None):
    private_key, public_key = generate_keypair()

    message = OMMMessage(
        message_id=message_id,
        message_type=MessageType.TASK_ASSIGN,
        sender="agent-a",
        receiver="agent-b",
        timestamp=timestamp or datetime.now(timezone.utc).isoformat(),
        payload={
            "task_id": "security-test",
            "sender_public_key": public_key,
        },
    )

    data = message.model_dump(mode="json")
    message.signature = sign_omm_message(data, private_key)

    return message.model_dump(mode="json")


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_receive_task():
    response = client.post(
        "/task",
        json={
            "task_id": "task-001",
            "objective": "test task",
            "input_data": {"value": 42},
        },
    )

    assert response.status_code == 200
    assert response.json()["status"] == "completed"


def test_duplicate_message_rejected():
    message = make_signed_message("security-duplicate-001")

    first = client.post("/message", json=message)
    second = client.post("/message", json=message)

    assert first.json()["status"] == "verified"
    assert second.json()["status"] == "rejected"
    assert second.json()["reason"] == "Duplicate message ID"


def test_old_message_rejected():
    old_timestamp = (
        datetime.now(timezone.utc) - timedelta(minutes=10)
    ).isoformat()

    message = make_signed_message(
        "security-old-001",
        timestamp=old_timestamp,
    )

    response = client.post("/message", json=message)

    assert response.json()["status"] == "rejected"
    assert response.json()["reason"] == (
        "Message timestamp outside allowed window"
    )


def test_tampered_message_rejected():
    message = make_signed_message("security-tampered-001")
    message["sender"] = "attacker"

    response = client.post("/message", json=message)

    assert response.json()["status"] == "rejected"
    assert response.json()["reason"] == "Invalid message signature"


if __name__ == "__main__":
    test_health()
    test_receive_task()
    test_duplicate_message_rejected()
    test_old_message_rejected()
    test_tampered_message_rejected()
    print("All server security tests passed.")
