from crypto import generate_keypair
from schemas import AgentSpec, Capability


class Agent:
    def __init__(
        self,
        agent_id: str,
        model_provenance: str,
        capabilities: list[Capability],
        endpoint: str,
    ):
        private_key, public_key = generate_keypair()

        self.private_key = private_key

        self.spec = AgentSpec(
            agent_id=agent_id,
            public_key=public_key,
            model_provenance=model_provenance,
            capabilities=capabilities,
            endpoint=endpoint,
        )

    def get_spec(self) -> AgentSpec:
        return self.spec


if __name__ == "__main__":
    agent = Agent(
        agent_id="agent-001",
        model_provenance="python-agent",
        capabilities=[
            Capability(
                name="reasoning",
                input_type="text",
                output_type="text",
                description="Basic reasoning capability",
            )
        ],
        endpoint="http://localhost:8001",
    )

    print(agent.get_spec().model_dump_json(indent=2))
