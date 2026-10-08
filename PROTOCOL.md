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

## 9. Agent Communication

Agents SHOULD be able to communicate directly using a common protocol.

A communication message SHOULD contain:

- sender
- receiver
- message_id
- timestamp
- message_type
- payload

Agents MAY communicate through:

- direct peer-to-peer connections
- relay nodes
- decentralized networks
- other compatible transport mechanisms

The protocol SHOULD NOT require a single central communication server.

Messages SHOULD preserve enough information to allow their origin and context to be independently examined.

Agents SHOULD be able to exchange:

- tasks
- capabilities
- evidence
- results
- verification requests
- challenges
- status updates

Different transport mechanisms MAY be used as long as they support the OpenMindMesh communication model.

## 10. Disagreement and Conflict

Agents MAY produce different results for the same task.

Disagreement MUST NOT be resolved solely by authority, reputation, or majority vote.

When agents disagree, they SHOULD be able to:

- identify the conflicting claims
- exchange evidence
- expose assumptions
- reproduce relevant computations
- request independent verification
- identify the source of the disagreement
- record unresolved disputes

A conflict record MAY contain:

- task_id
- claims
- agents involved
- evidence
- assumptions
- verification attempts
- resolution status

A disagreement MAY remain unresolved when available evidence is insufficient.

The protocol SHOULD preserve unresolved disagreements rather than hiding or deleting them.

Resolved disputes SHOULD retain enough history to allow independent examination of how the resolution was reached.

## 11. Collective Intelligence

OpenMindMesh SHOULD support cooperation between multiple independent agents to produce results that may be better than the result of any individual agent.

A collective task MAY be divided into smaller subtasks and distributed among multiple agents.

Agents MAY:

- solve different parts of a task
- review each other's work
- provide alternative solutions
- combine independent results
- identify contradictions
- request additional analysis
- produce a final synthesized result

A collective result SHOULD preserve the contributions, evidence, reasoning steps, verification outcomes, and unresolved disagreements that materially affected the result.

The system SHOULD NOT assume that combining more agents automatically produces a better result.

Collective intelligence SHOULD emerge from:

- diversity of capabilities
- independent reasoning
- information exchange
- verification
- criticism
- specialization
- synthesis

No single agent SHOULD be required to control the entire collective process.

OpenMindMesh MAY support dynamic formation of agent groups for specific tasks.

## 12. Agent Selection and Coordination

For a task requiring multiple agents, OpenMindMesh SHOULD support dynamic selection and coordination of suitable agents.

Agent selection MAY consider:

- capabilities
- availability
- previous task history
- verification history
- evidence quality
- specialization
- current workload
- network connectivity

Selection SHOULD NOT depend solely on reputation or a single central authority.

A coordinating agent MAY propose a group of agents for a task.

Other agents MAY independently evaluate or challenge the proposed selection.

Coordination MAY be:

- centralized for a specific task
- distributed among participating agents
- dynamically reassigned during execution

No permanent coordinator SHOULD be required.

If a coordinating agent becomes unavailable or produces unreliable results, another suitable agent SHOULD be able to take over coordination.

The network SHOULD support parallel execution of independent subtasks when appropriate.

Coordination decisions SHOULD be observable and independently examinable.

## 13. Task Execution Flow

A task SHOULD follow a traceable execution flow.

A typical task MAY proceed through the following stages:

1. task creation
2. capability discovery
3. agent selection
4. task decomposition
5. parallel or sequential execution
6. result collection
7. independent verification
8. conflict resolution when necessary
9. result synthesis
10. final result publication

Agents MAY create subtasks when a task can be divided into independent components.

Subtasks SHOULD retain a reference to their parent task.

Each execution step SHOULD produce enough information to reconstruct the task history.

Agents MAY request additional agents during execution when new capabilities or verification are required.

A task MAY be paused, reassigned, repeated, or terminated.

The final result SHOULD include references to the relevant subtasks, evidence, verification results, and unresolved disagreements.

The execution flow SHOULD remain observable and independently examinable.

## 14. Agent Specification

An agent participating in OpenMindMesh SHOULD publish a machine-readable agent specification.

The specification MAY contain:

- agent_id
- protocol_version
- public_key
- capabilities
- endpoint
- supported_message_types
- supported_transport
- availability
- version
- software_or_model
- verification_history

An agent specification SHOULD be independently retrievable by other agents.

Agents MAY update their specifications when their capabilities, endpoints, software, or models change.

Changes SHOULD be versioned and traceable.

An agent MUST NOT claim capabilities that it cannot provide reliably.

Other agents SHOULD be able to compare published capabilities with observed performance and verification history.

The agent specification SHOULD use a machine-readable format so that other agents can discover and communicate with the agent automatically.

## 15. Message Format

OpenMindMesh messages SHOULD use a common machine-readable structure.

A message SHOULD contain:

- protocol
- version
- message_id
- message_type
- sender
- receiver
- timestamp
- payload
- references

Example:

```json
{
  "protocol": "OpenMindMesh",
  "version": "0.1",
  "message_id": "msg-001",
  "message_type": "TASK",
  "sender": "agent-a",
  "receiver": "agent-b",
  "timestamp": "2026-01-01T00:00:00Z",
  "payload": {},
  "references": []
}
```
The `message_type` field SHOULD identify the purpose of the message.

Initial message types MAY include:

- TASK
- RESULT
- EVIDENCE
- VERIFY
- CHALLENGE
- CAPABILITY
- STATUS
- ERROR

Agents MAY define additional message types while preserving compatibility with the core protocol.

Unknown message types SHOULD be safely ignored or reported as unsupported rather than causing protocol failure.

Messages SHOULD be versioned so that future protocol versions can evolve without breaking existing implementations.

## 16. Message Integrity and Authentication

Agents SHOULD be able to verify that a message was produced by the claimed sender and was not modified after transmission.

Messages MAY be digitally signed by the sender.

A valid signature SHOULD establish control of the corresponding public key, but MUST NOT by itself establish truthfulness or correctness.

Agents SHOULD verify signatures before accepting security-sensitive protocol actions.

If signature verification fails, the message SHOULD be rejected or marked as unverified.

Key changes SHOULD be versioned and traceable.

The protocol SHOULD support key rotation without requiring a central authority.

## 17. Failure Handling and Recovery

OpenMindMesh SHOULD support continued operation when individual agents, connections, or tasks fail.

An agent failure MAY include:

- becoming unavailable
- timing out
- returning an invalid message
- returning an incomplete result
- failing verification
- producing repeated errors
- becoming unreachable

When an expected response is not received within an appropriate time, the requesting agent SHOULD be able to retry, reassign, or terminate the task.

A failed subtask SHOULD NOT automatically cause the entire parent task to fail when alternative execution is possible.

Agents SHOULD be able to report failures using an ERROR message.

An ERROR message MAY contain:

- task_id
- message_id
- error_type
- error_description
- failed_agent
- retryable
- references

Agents SHOULD distinguish between temporary failures and persistent failures.

Temporary failures MAY be retried.

Persistent or repeated failures SHOULD trigger reassignment, additional verification, or termination of the affected task.

When an agent is replaced, the execution history SHOULD preserve the identity of the previous agent and the reason for replacement.

Recovery actions SHOULD be observable and independently examinable.

The protocol SHOULD avoid making any single agent a permanent point of failure.

## 18. Network Transport

OpenMindMesh SHOULD support multiple network transport mechanisms.

Agents MAY communicate using:

- direct peer-to-peer connections
- HTTP or HTTPS
- WebSocket
- relay nodes
- decentralized overlay networks
- other compatible transport mechanisms

The transport layer MUST NOT change the meaning of OpenMindMesh messages.

The protocol message structure SHOULD remain independent from the underlying transport.

Agents SHOULD advertise which transport mechanisms they support.

An agent MAY support multiple transport mechanisms simultaneously.

A connection failure SHOULD NOT be treated as a failure of the agent itself when another supported transport is available.

Agents SHOULD be able to discover alternative connection paths when direct communication is unavailable.

The protocol SHOULD avoid requiring a single permanent network gateway or central communication server.

Transport mechanisms SHOULD preserve message integrity and provide sufficient information to associate received messages with their claimed sender.

OpenMindMesh MAY define additional transport profiles for interoperability between implementations.

## 19. Agent Discovery

Agents SHOULD be able to discover other agents that participate in OpenMindMesh.

An agent discovery record MAY contain:

- agent_id
- public_key
- capabilities
- endpoint
- supported_transport
- protocol_version
- availability
- version
- last_updated

Discovery MAY use:

- decentralized peer discovery
- distributed hash tables
- discovery services
- direct exchange of agent specifications
- relay nodes
- other compatible mechanisms

No single discovery service MUST be required for the network to operate.

Agents MAY advertise their own specifications to other agents.

Agents SHOULD be able to request the specification of another known agent.

Discovery records SHOULD be verifiable and SHOULD include enough information to determine whether the record is current.

Agents SHOULD be able to detect outdated or invalid discovery records.

An agent MAY publish multiple endpoints or transport mechanisms.

Agents SHOULD be able to continue operating when one discovery mechanism becomes unavailable.

Discovery mechanisms SHOULD NOT change the meaning or structure of OpenMindMesh messages.

The network SHOULD support the addition and removal of agents without requiring a central authority.

## 20. Task Graph

OpenMindMesh SHOULD represent complex tasks as a graph of related tasks and subtasks.

Each task SHOULD have a unique task_id.

Each subtask SHOULD reference its parent task.

A task MAY contain:

- task_id
- parent_task_id
- objective
- required_capabilities
- assigned_agents
- dependencies
- status
- inputs
- outputs
- evidence
- verification_results

Tasks MAY depend on other tasks.

A task SHOULD NOT be marked complete until its required dependencies have completed or have been explicitly marked as failed or unnecessary.

Independent subtasks SHOULD be executable in parallel when appropriate.

Agents MAY create additional subtasks when required to complete a task.

Agents SHOULD be able to observe the status of tasks relevant to their work.

Task state changes SHOULD be recorded and traceable.

Possible task states MAY include:

- CREATED
- DISCOVERING
- ASSIGNED
- RUNNING
- WAITING
- VERIFYING
- COMPLETED
- FAILED
- CANCELLED

The task graph SHOULD preserve enough information to reconstruct how the final result was produced.

A task graph MAY be distributed across multiple agents.

No single agent MUST maintain the complete task graph for the entire network.

## 21. Result Synthesis

OpenMindMesh SHOULD support combining results produced by multiple agents.

A synthesized result SHOULD reference the tasks, subtasks, agents, evidence, and verification results that contributed to it.

A result MAY contain:

- task_id
- result_id
- contributing_agents
- source_results
- evidence
- verification_results
- conflicts
- synthesis_method
- confidence
- status

Agents MAY produce alternative results for the same task.

Alternative results SHOULD remain distinguishable until they have been independently evaluated.

A synthesis process SHOULD NOT discard materially different results without recording the reason.

The synthesis process MAY:

- compare results
- identify agreements
- identify contradictions
- evaluate evidence
- request additional verification
- combine compatible results
- select one result when evidence supports doing so
- preserve multiple unresolved results

A final result SHOULD indicate whether significant disagreements remain unresolved.

The final result SHOULD remain traceable to the underlying task graph.

Result synthesis MAY be performed by one agent or by multiple cooperating agents.

No single agent MUST be considered the final authority solely because it performs the synthesis.

Synthesis decisions SHOULD be observable and independently examinable.

## 22. Coordination and Concurrency

OpenMindMesh SHOULD support concurrent execution of tasks by multiple agents.

Agents MAY execute independent tasks or subtasks simultaneously.

Agents SHOULD coordinate when multiple agents need to modify, extend, or contribute to the same task state.

A task MAY define dependencies that determine when an agent can begin execution.

Agents SHOULD avoid unnecessary duplicate execution when the same task is already being processed by a suitable agent.

Duplicate execution MAY be used intentionally for independent verification, redundancy, or fault tolerance.

Agents SHOULD be able to detect conflicting task state updates.

When conflicting updates occur, agents SHOULD preserve the conflicting information and request verification or resolution.

Coordination SHOULD NOT require a permanent central coordinator.

A coordination failure SHOULD NOT permanently block unrelated tasks.

Agents SHOULD support timeouts or other mechanisms that prevent tasks from remaining indefinitely in an active state.

Concurrent execution SHOULD preserve enough information to reconstruct the order and relationships between relevant task events.

The protocol SHOULD support reassignment of coordination responsibilities when the current coordinator becomes unavailable or unreliable.

## 23. Protocol Versioning and Compatibility

OpenMindMesh messages SHOULD include the protocol version used by the sender.

Protocol versions SHOULD follow a clearly defined versioning scheme.

Agents SHOULD advertise the protocol versions they support.

An agent MAY support multiple protocol versions simultaneously.

Agents SHOULD determine compatibility before using protocol features that may not be supported by the receiving agent.

New protocol features SHOULD be introduced in a way that does not unnecessarily break existing implementations.

Unknown optional fields SHOULD be safely ignored when they are not required for processing a message.

Required fields MUST NOT be silently ignored.

An agent that cannot process a message because of an unsupported protocol version SHOULD return an ERROR message when possible.

Protocol changes SHOULD be documented and traceable.

Implementations SHOULD preserve compatibility with earlier protocol versions when practical.

A protocol version change MUST NOT silently change the meaning of existing message types or fields.

OpenMindMesh MAY define compatibility rules for specific protocol versions and message types.

## 24. Event Log and Provenance

OpenMindMesh SHOULD maintain a traceable record of significant protocol events.

An event MAY contain:

- event_id
- event_type
- timestamp
- agent_id
- task_id
- message_id
- parent_event_id
- data
- references

Significant events MAY include:

- task creation
- task assignment
- task execution
- task completion
- task failure
- message transmission
- verification
- challenge
- conflict
- reassignment
- result synthesis

Events SHOULD preserve enough information to reconstruct the relevant execution history.

Events SHOULD be ordered or otherwise related so that agents can determine their relationships.

Agents MAY maintain local event logs.

Relevant events SHOULD be shareable with other participating agents when required for verification or coordination.

Event records SHOULD be tamper-evident when practical.

An event log MAY be distributed across multiple agents.

No single agent MUST be required to maintain the complete event history of the entire network.

Historical records SHOULD NOT be silently modified or removed when they are necessary to understand or verify a result.

Provenance information SHOULD remain associated with the results and tasks to which it relates.

## 25. Capability Matching

OpenMindMesh SHOULD allow tasks to be matched with agents based on their declared capabilities.

A task MAY specify required and preferred capabilities.

An agent SHOULD publish the capabilities it can provide.

Capability matching MAY consider:

- required capabilities
- preferred capabilities
- protocol version
- supported transport
- availability
- current workload
- previous verification history
- relevant task experience

Required capabilities SHOULD be satisfied before an agent is selected for a task.

Preferred capabilities MAY be used to rank otherwise suitable agents.

Agents SHOULD NOT be selected solely because of reputation.

An agent MAY reject a task when it determines that it cannot satisfy the required capabilities.

Capability matching MAY be performed by:

- the requesting agent
- a coordinating agent
- multiple cooperating agents
- a decentralized selection mechanism

Selection decisions SHOULD be observable and independently examinable.

The network SHOULD support multiple agents with overlapping capabilities.

Capability matching SHOULD allow new agents to participate without requiring manual registration with a central authority.

## 26. Resource and Load Management

OpenMindMesh SHOULD allow agents to declare their current availability and resource capacity.

An agent MAY publish resource information such as:

- availability
- current workload
- task capacity
- computational capacity
- memory capacity
- estimated response time
- supported concurrency

Resource information MAY be approximate and SHOULD be treated as a current estimate rather than a guarantee.

Agents SHOULD be able to update their resource status when their availability or workload changes.

Task assignment SHOULD consider resource availability when appropriate.

An agent SHOULD NOT be assigned more concurrent work than it can reasonably handle when reliable capacity information is available.

Agents MAY reject or defer tasks when their available resources are insufficient.

Resource-aware coordination MAY be performed by:

- the requesting agent
- a coordinating agent
- multiple cooperating agents
- a decentralized selection mechanism

Resource information SHOULD be observable and independently examinable when it is used to justify task assignment.

The network SHOULD support agents with different levels of computational capacity.

A resource-constrained agent SHOULD still be able to participate in tasks that match its available capabilities and resources.

Resource management SHOULD NOT require a permanent central resource coordinator.

## 27. Authorization and Action Control

OpenMindMesh SHOULD allow agents to determine whether another agent is authorized to perform a requested protocol action.

Authorization MAY be based on:

- agent identity
- declared capabilities
- task assignment
- message context
- delegation
- applicable protocol rules
- explicit permissions granted by another agent

Authorization SHOULD be evaluated separately from authentication.

Successful authentication MUST NOT automatically imply authorization to perform every action.

An agent MAY delegate authority for a specific task or operation to another agent.

Delegated authority SHOULD be limited to the scope necessary for the delegated task.

Agents SHOULD be able to verify the origin and scope of delegated authority.

An agent SHOULD reject or refuse an action when the required authorization cannot be established.

Authorization decisions SHOULD be observable and independently examinable when they materially affect task execution.

The protocol SHOULD support different authorization policies for different tasks, agents, and operations.

Authorization mechanisms SHOULD NOT require a permanent central authority.

Authorization information SHOULD be represented in a machine-readable form when it is required for automated decision-making.

Changes to relevant authorization or delegation SHOULD be traceable through the event history.

## 28. Trust and Evaluation

OpenMindMesh SHOULD allow agents to evaluate the observed performance of other agents.

Evaluation MAY consider:

- task outcomes
- verification results
- evidence quality
- reproducibility
- consistency
- failure history
- successful task history
- capability claims compared with observed performance

An evaluation SHOULD be based on observable or verifiable information whenever possible.

An agent MUST NOT be considered trustworthy solely because of its identity, reputation, or claimed capabilities.

Agents MAY maintain different evaluations of the same agent.

Evaluation results SHOULD remain distinguishable from objective protocol facts.

An agent MAY challenge an evaluation by providing additional evidence or requesting independent verification.

Evaluation records SHOULD preserve their relevant evidence and provenance.

The network SHOULD support independent evaluation by multiple agents.

Evaluation mechanisms SHOULD NOT require a single global authority.

An agent's evaluation MAY change as new evidence and task outcomes become available.

Historical evaluation changes SHOULD be traceable.

Trust SHOULD be treated as an evolving assessment rather than a permanent property of an agent.

## 29. Task Requirements and Constraints

OpenMindMesh SHOULD allow tasks to declare requirements and operational constraints.

A task MAY specify:

- required capabilities
- preferred capabilities
- required protocol version
- required message types
- maximum execution time
- expected response time
- resource requirements
- concurrency requirements
- verification requirements
- evidence requirements
- output requirements

Task constraints SHOULD be machine-readable when they are used for automated coordination.

Agents SHOULD evaluate task requirements before accepting an assignment.

An agent MAY reject a task when its capabilities, resources, or supported protocol features do not satisfy the required constraints.

Optional or preferred requirements MAY be used to rank otherwise suitable agents.

Task requirements SHOULD remain associated with the task throughout
