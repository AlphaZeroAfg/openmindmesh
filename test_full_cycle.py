from agent_network import send_task
from network_verification import request_verification
from schemas import EvidenceRecord, VerificationOutcome


def test_full_cycle():
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

    verification = request_verification(
        task_id="task-full-001",
        target_agent_id="agent-b",
        evidence=evidence,
    )

    assert verification.outcome == VerificationOutcome.VERIFIED

    print("\nOpenMindMesh FULL CYCLE: PASSED")


if __name__ == "__main__":
    test_full_cycle()
