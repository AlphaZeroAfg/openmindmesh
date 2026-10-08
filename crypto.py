import json
from typing import Any, Dict

from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    NoEncryption,
    PrivateFormat,
    PublicFormat,
)


def canonical_json(data: Dict[str, Any]) -> bytes:
    """
    Convert a message to deterministic Canonical JSON bytes.
    """
    return json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def generate_keypair() -> tuple[str, str]:
    """
    Generate an Ed25519 keypair.

    Returns:
        (private_key_hex, public_key_hex)
    """
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    private_bytes = private_key.private_bytes(
        Encoding.Raw,
        PrivateFormat.Raw,
        NoEncryption(),
    )

    public_bytes = public_key.public_bytes(
        Encoding.Raw,
        PublicFormat.Raw,
    )

    return private_bytes.hex(), public_bytes.hex()


def sign_message(
    message: Dict[str, Any],
    private_key_hex: str,
) -> str:
    """
    Sign a message using an Ed25519 private key.
    """
    private_key = Ed25519PrivateKey.from_private_bytes(
        bytes.fromhex(private_key_hex)
    )

    signature = private_key.sign(canonical_json(message))

    return signature.hex()


def verify_signature(
    message: Dict[str, Any],
    signature_hex: str,
    public_key_hex: str,
) -> bool:
    """
    Verify an Ed25519 signature.
    """
    public_key = Ed25519PublicKey.from_public_bytes(
        bytes.fromhex(public_key_hex)
    )

    try:
        public_key.verify(
            bytes.fromhex(signature_hex),
            canonical_json(message),
        )
        return True
    except Exception:
        return False

def sign_omm_message(
    message: Dict[str, Any],
    private_key_hex: str,
) -> str:
    """
    Sign an OpenMindMesh message without including its signature field.
    """
    signable_message = dict(message)
    signable_message.pop("signature", None)

    return sign_message(
        signable_message,
        private_key_hex,
    )
