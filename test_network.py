from fastapi.testclient import TestClient

from server import app
from agent_network import send_task


def test_agent_network(monkeypatch):
    client = TestClient(app)

    def fake_post(url, json, timeout):
        response = client.post("/task", json=json)

        class FakeResponse:
            def raise_for_status(self):
                assert response.status_code == 200

            def json(self):
                return response.json()

        return FakeResponse()

    monkeypatch.setattr(
        "agent_network.requests.post",
        fake_post,
    )

    result = send_task(
        sender="agent-a",
        receiver_endpoint="http://localhost:8001",
        task_id="task-network-001",
        objective="Test communication between two OpenMindMesh agents",
        input_data={
            "message": "Hello from agent-a"
        },
    )

    assert result["status"] == "completed"
    assert result["task_id"] == "task-network-001"


if __name__ == "__main__":
    test_agent_network()
    print("OpenMindMesh network test: PASSED")
