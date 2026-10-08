from schemas import EvidenceRecord, VerificationOutcome, VerificationPayload


def verify_result(
    task_id: str,
    target_agent_id: str,
    evidence: EvidenceRecord,
) -> VerificationPayload:
    """
    Perform a minimal evidence-based verification.
    """

    if evidence.uncertainty_score <= 0.5:
        outcome = VerificationOutcome.VERIFIED
        reasoning = "Evidence uncertainty is within the verification threshold."
    else:
        outcome = VerificationOutcome.UNCERTAIN
        reasoning = "Evidence uncertainty is above the verification threshold."

    return VerificationPayload(
        task_id=task_id,
        target_agent_id=target_agent_id,
        outcome=outcome,
        reasoning=reasoning,
        evidence_check=evidence,
    )


if __name__ == "__main__":
    evidence = EvidenceRecord(
        claim="Task was executed",
        evidence_type="execution_log",
        payload={
            "agent": "agent-b"
        },
        uncertainty_score=0.0,
    )

    result = verify_result(
        task_id="task-001",
        target_agent_id="agent-b",
        evidence=evidence,
    )

    print(result.model_dump_json(indent=2))
