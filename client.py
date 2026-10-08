import requests


def send_task(
    endpoint: str,
    task_id: str,
    objective: str,
    input_data: dict,
):
    response = requests.post(
        f"{endpoint}/task",
        json={
            "task_id": task_id,
            "objective": objective,
            "input_data": input_data,
        },
        timeout=5,
    )

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    result = send_task(
        endpoint="http://localhost:8001",
        task_id="task-001",
        objective="test communication",
        input_data={"value": 42},
    )

    print(result)
