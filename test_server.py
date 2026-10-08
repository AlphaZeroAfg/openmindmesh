from fastapi.testclient import TestClient

from server import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["protocol"] == "OpenMindMesh"


def test_receive_task():
    response = client.post(
        "/task",
        json={
            "task_id": "task-001",
            "objective": "test task",
            "input_data": {
                "value": 42
            },
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "received"
    assert data["task_id"] == "task-001"
    assert data["objective"] == "test task"
    assert data["input_data"]["value"] == 42


if __name__ == "__main__":
    test_health()
    test_receive_task()
    print("OpenMindMesh server tests: PASSED")
