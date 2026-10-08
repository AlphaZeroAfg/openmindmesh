import requests


def send_task(
    sender: str,
    receiver_endpoint: str,
    task_id: str,
    objective: str,
    input_data: dict,
):
    print(f"\n[{sender}]")
    print(f"  ↓ TASK_ASSIGN → {receiver_endpoint}")

    response = requests.post(
        f"{receiver_endpoint}/task",
        json={
            "task_id": task_id,
            "objective": objective,
            "input_data": input_data,
        },
        timeout=5,
    )

    response.raise_for_status()

    result = response.json()

    print(f"  ↑ RESULT_SUBMIT ← {receiver_endpoint}")
    print(f"  Status: {result['status']}")
    print(f"  Task: {result['task_id']}")

    return result


if __name__ == "__main__":
    result = send_task(
        sender="agent-a",
        receiver_endpoint="http://localhost:8001",
        task_id="task-network-001",
        objective="Test communication between two OpenMindMesh agents",
        input_data={
            "message": "Hello from agent-a"
        },
    )

    print("\nOpenMindMesh network test completed.")
    print(result)
