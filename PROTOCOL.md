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

```text
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
