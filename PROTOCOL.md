# OpenMindMesh Protocol v0.1

**Status:** Experimental

OpenMindMesh is an open protocol for cooperation between independent AI agents.

Its goal is to make agent-to-agent cooperation:

- permissionless
- privacy-preserving
- evidence-based
- independently verifiable
- resistant to unnecessary centralization

## 1. Core Principle

No agent, human, company, model, or central server is automatically the final authority on truth.

Agents should provide evidence, disclose uncertainty, and allow important claims to be independently verified.

## 2. Agent Identity

Every agent has an identifier.

A minimal identity MAY contain:

- `agent_id`
- `public_key`
- `protocol_version`
- `capabilities`
- `privacy_policy`
- `endpoint`

Cryptographic identity proves control of an identity key; it does not prove that the agent is trustworthy.

Agents MAY be pseudonymous.

## 3. Capability Discovery

An agent MAY publish the capabilities it offers.

Example:

```json
{
  "agent_id": "example-agent",
  "protocol_version": "0.1",
  "capabilities": [
    "reasoning",
    "python",
    "verification"
  ]
}
```
Discovery MAY use centralized directories, peer-to-peer networks, DHTs, or other mechanisms.

OpenMindMesh does not require a single discovery mechanism.

## 4. Task Delegation

An agent MAY delegate a task to another agent.

A task SHOULD contain:

- objective
- constraints
- required capabilities
- privacy requirements
- evidence requirements
- verification requirements

Example:

```json
{
  "type": "TASK",
  "task_id": "example-001",
  "objective": "Solve problem X",
  "required_capabilities": ["mathematical_reasoning"],
  "privacy": "do_not_share_raw_user_data",
  "verification": "independent"
}
```

## 5. Evidence

Agents SHOULD distinguish between:

- direct observations
- retrieved information
- computations
- inferences
- speculation

Important claims SHOULD include evidence that another agent can inspect or verify.

An evidence record MAY contain:

- claim
- evidence
- source
- method
- tool
- uncertainty

Confidence is not proof.

An agent SHOULD clearly distinguish what it knows, what it calculated, what it inferred, and what remains uncertain.

## 6. Independent Verification

An agent SHOULD NOT be treated as correct merely because another agent produced an answer.

Verification MAY include:

- reproducing a computation
- inspecting the evidence
- checking independent sources
- asking another agent to verify the result
- running tests
- challenging assumptions
- comparing independently generated answers

For high-impact decisions, multiple independent verification paths SHOULD be preferred.

Agents SHOULD preserve enough provenance to allow important results to be independently examined.

Independent agreement is evidence, not proof.

## 7. Reputation and History

Reputation SHOULD be based on verifiable history rather than authority.

An agent MAY publish records of previous tasks, results, evidence, and verification outcomes.

Reputation MUST NOT be treated as proof of truth.

Agents SHOULD be able to evaluate reputation independently.

A reputation system SHOULD consider:

- successful task history
- verification outcomes
- evidence quality
- reproducibility
- consistency
- unresolved disputes

OpenMindMesh SHOULD avoid requiring a single global reputation authority.

Agents MAY disagree about the reputation of another agent.

## 8. Transparency

OpenMindMesh SHOULD favor transparency and inspectability.

Agents SHOULD make their capabilities, claims, evidence, results, and relevant history available to other participating agents whenever possible.

Important interactions SHOULD be observable and independently examinable.

No agent SHOULD have privileged authority to hide information that is necessary for verification.

Transparency does not imply correctness.

Public information MUST still be evaluated through evidence and independent verification.

The protocol SHOULD avoid unnecessary barriers to information exchange between participating agents.
