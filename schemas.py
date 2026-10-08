from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


# --- Enums ---

class MessageType(str, Enum):
    CAPABILITY_ANNOUNCE = "CAPABILITY_ANNOUNCE"
    TASK_ASSIGN = "TASK_ASSIGN"
    RESULT_SUBMIT = "RESULT_SUBMIT"
    VERIFY_REQUEST = "VERIFY_REQUEST"
    VERIFY_RESULT = "VERIFY_RESULT"


class EvidenceType(str, Enum):
    EXECUTION_LOG = "execution_log"
    API_RESPONSE = "api_response"
    REASONING_TRACE = "reasoning_trace"


class VerificationOutcome(str, Enum):
    VERIFIED = "verified"
    REJECTED = "rejected"
    UNCERTAIN = "uncertain"


# --- Core Structures ---

class Capability(BaseModel):
    name: str
    input_type: str
    output_type: str
    description: Optional[str] = None


class AgentSpec(BaseModel):
    agent_id: str
    public_key: str
    model_provenance: str
    capabilities: List[Capability]
    endpoint: str


class TaskConstraints(BaseModel):
    timeout_ms: int = 5000
    require_execution_proof: bool = False


class Task(BaseModel):
    task_id: str
    parent_task_id: Optional[str] = None
    objective: str
    input_data: Dict[str, Any]
    constraints: TaskConstraints = Field(default_factory=TaskConstraints)


class EvidenceRecord(BaseModel):
    claim: str
    evidence_type: EvidenceType
    payload: Dict[str, Any]
    uncertainty_score: float = Field(ge=0.0, le=1.0, default=0.0)


class ResultPayload(BaseModel):
    task_id: str
    output: Dict[str, Any]
    evidence: EvidenceRecord


class VerificationPayload(BaseModel):
    task_id: str
    target_agent_id: str
    outcome: VerificationOutcome
    reasoning: str
    evidence_check: Optional[EvidenceRecord] = None


# --- Protocol Message Format ---

class OMMMessage(BaseModel):
    protocol: str = "OpenMindMesh"
    version: str = "0.1"
    message_id: str
    message_type: MessageType
    sender: str
    receiver: str
    timestamp: str = Field(
        default_factory=lambda: datetime.utcnow().isoformat() + "Z"
    )
    payload: Dict[str, Any]
    signature: Optional[str] = None
