from crypto import (
    canonical_json,
    generate_keypair,
    sign_message,
    sign_omm_message,
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
        "signature": None,
    }

    # Canonical JSON must be deterministic
    canonical = canonical_json(message)
    assert isinstance(canonical, bytes)

    # Sign the OpenMindMesh message without its signature field
    signature = sign_omm_message(message, private_key)

    # Verify the message without its signature field
    signable_message = dict(message)
    signable_message.pop("signature")

    assert verify_signature(
        signable_message,
        signature,
        public_key,
    )

    # Modified message must fail verification
    modified_message = dict(signable_message)
    modified_message["receiver"] = "agent-c"

    assert not verify_signature(
        modified_message,
        signature,
        public_key,
    )

    print("OpenMindMesh crypto test: PASSED")


if __name__ == "__main__":
    test_crypto()
