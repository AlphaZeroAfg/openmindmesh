from crypto import (
    canonical_json,
    generate_keypair,
    sign_message,
    verify_signature,
)


def test_crypto():
    private_key, public_key = generate_keypair()

    message = {
        "protocol": "OpenMindMesh",
        "version": "0.1",
        "message_id": "test-001",
        "message_type": "TASK_ASSIGN",
        "sender": "agent-a",
        "receiver": "agent-b",
        "payload": {
            "objective": "test message"
        },
    }

    # Canonical JSON must be deterministic
    canonical = canonical_json(message)
    assert isinstance(canonical, bytes)

    # Sign the message
    signature = sign_message(message, private_key)

    # Verify the original message
    assert verify_signature(
        message,
        signature,
        public_key,
    )

    # Modified message must fail verification
    modified_message = dict(message)
    modified_message["receiver"] = "agent-c"

    assert not verify_signature(
        modified_message,
        signature,
        public_key,
    )

    print("OpenMindMesh crypto test: PASSED")


if __name__ == "__main__":
    test_crypto()
