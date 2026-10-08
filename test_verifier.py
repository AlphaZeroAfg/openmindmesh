from schemas import EvidenceRecord, VerificationOutcome
from verifier import verify_result


def test_verified_result():
    evidence = EvidenceRecord(
        claim="Task was executed",
        evidence_type="execution_log",
        payload={"agent": "agent-b"},
        uncertainty_score=0.0,
    )

    result = verify_result(
        task_id="task-001",
        target_agent_id="agent-b",
        evidence=evidence,
    )

    assert result.outcome == VerificationOutcome.VERIFIED
    assert result.task_id == "task-001"
    assert result.target_agent_id == "agent-b"


def test_uncertain_result():
    evidence = EvidenceRecord(
        claim="Task was executed",
        evidence_type="execution_log",
        payload={"agent": "agent-b"},
        uncertainty_score=0.8,
    )

    result = verify_result(
        task_id="task-002",
        target_agent_id="agent-b",
        evidence=evidence,
    )

    assert result.outcome == VerificationOutcome.UNCERTAIN


if __name__ == "__main__":
    test_verified_result()
    test_uncertain_result()
    print("OpenMindMesh verifier test: PASSED")
