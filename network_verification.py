from schemas import EvidenceRecord
from verifier import verify_result


def request_verification(
    task_id: str,
    target_agent_id: str,
    evidence: EvidenceRecord,
):
    print(f"\n[agent-a]")
    print("  ↓ VERIFY_REQUEST → agent-b")

    result = verify_result(
        task_id=task_id,
        target_agent_id=target_agent_id,
        evidence=evidence,
    )

    print("  ↑ VERIFY_RESULT ← agent-b")
    print(f"  Outcome: {result.outcome.value}")

    return result


if __name__ == "__main__":
    evidence = EvidenceRecord(
        claim="Task was executed successfully",
        evidence_type="execution_log",
        payload={
            "agent": "agent-b",
            "task": "task-network-001",
        },
        uncertainty_score=0.0,
    )

    result = request_verification(
        task_id="task-network-001",
        target_agent_id="agent-b",
        evidence=evidence,
    )

    print("\nVerification completed.")
    print(result.model_dump_json(indent=2))
