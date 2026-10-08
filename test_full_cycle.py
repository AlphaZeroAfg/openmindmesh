from unittest.mock import patch
from fastapi.testclient import TestClient

from server import app
from agent_network import send_task
from network_verification import request_verification
from schemas import EvidenceRecord, VerificationOutcome


def test_full_cycle():
    client = TestClient(app)

    def fake_task_post(url, json, timeout):
        response = client.post("/task", json=json)

        class FakeResponse:
            def raise_for_status(self):
                assert response.status_code == 200

            def json(self):
                return response.json()

        return FakeResponse()

    with patch("agent_network.requests.post", fake_task_post):
        result = send_task(
            sender="agent-a",
            receiver_endpoint="http://localhost:8001",
            task_id="task-full-001",
            objective="Complete OpenMindMesh full cycle test",
            input_data={
                "message": "Hello from agent-a"
            },
        )

    assert result["status"] == "completed"

    evidence = EvidenceRecord(
        claim="Task was executed successfully",
        evidence_type="execution_log",
        payload={
            "agent": "agent-b",
            "task": "task-full-001",
        },
        uncertainty_score=0.0,
    )

    def fake_verification_post(url, json, timeout):
        response = client.post("/message", json=json)

        class FakeResponse:
            def raise_for_status(self):
                assert response.status_code == 200

            def json(self):
                return response.json()

        return FakeResponse()

    with patch("network_verification.requests.post", fake_verification_post):
        verification = request_verification(
            task_id="task-full-001",
            target_agent_id="agent-b",
            evidence=evidence,
        )

    assert verification["status"] == "verified"
    assert verification["outcome"] == VerificationOutcome.VERIFIED.value

    print("\nOpenMindMesh FULL CYCLE: PASSED")


if __name__ == "__main__":
    test_full_cycle()
    print("OpenMindMesh full cycle test: PASSED")
