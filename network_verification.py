
import requests

from crypto import generate_keypair, sign_omm_message
from schemas import EvidenceRecord, OMMMessage, MessageType


def request_verification(
    task_id: str,
    target_agent_id: str,
    evidence: EvidenceRecord,
):
    private_key, public_key = generate_keypair()

    message = OMMMessage(
        message_id=f"verify-{task_id}",
        message_type=MessageType.VERIFY_REQUEST,
        sender="agent-a",
        receiver=target_agent_id,
        payload={
            "task_id": task_id,
            "evidence": evidence.model_dump(mode="json"),
            "sender_public_key": public_key,
        },
    )

    message_data = message.model_dump(mode="json")

    message.signature = sign_omm_message(
        message_data,
        private_key,
    )

    print("\n[agent-a]")
    print("  ↓ SIGNED VERIFY_REQUEST → agent-b")

    response = requests.post(
        "http://localhost:8001/message",
        json=message.model_dump(mode="json"),
        timeout=5,
    )

    response.raise_for_status()
    result = response.json()

    print("  ↑ VERIFY_RESULT ← agent-b")
    print(f"  Status: {result['status']}")

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

    print("\nNetwork verification completed.")
    print(result)
