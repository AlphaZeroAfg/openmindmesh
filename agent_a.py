from agent_network import send_task


if __name__ == "__main__":
    print("OpenMindMesh Agent A starting...")

    result = send_task(
        sender="agent-a",
        receiver_endpoint="http://localhost:8001",
        task_id="task-real-001",
        objective="Test real communication between Agent A and Agent B",
        input_data={
            "message": "Hello from Agent A"
        },
    )

    print("\nAgent A received:")
    print(result)
