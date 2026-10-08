from agent import Agent
from schemas import Capability


def test_agent_creation():
    agent = Agent(
        agent_id="agent-test",
        model_provenance="python-agent",
        capabilities=[
            Capability(
                name="reasoning",
                input_type="text",
                output_type="text",
            )
        ],
        endpoint="http://localhost:8001",
    )

    spec = agent.get_spec()

    assert spec.agent_id == "agent-test"
    assert spec.public_key
    assert spec.model_provenance == "python-agent"
    assert len(spec.capabilities) == 1
    assert spec.capabilities[0].name == "reasoning"

    print("OpenMindMesh agent test: PASSED")


if __name__ == "__main__":
    test_agent_creation()
