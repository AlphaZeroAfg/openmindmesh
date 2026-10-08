from client import send_task


def test_send_task(monkeypatch):
    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {
                "status": "received",
                "task_id": "task-001",
                "objective": "test communication",
                "input_data": {"value": 42},
            }

    def fake_post(url, json, timeout):
        assert url == "http://localhost:8001/task"
        assert json["task_id"] == "task-001"
        assert json["objective"] == "test communication"
        assert json["input_data"]["value"] == 42
        assert timeout == 5
        return FakeResponse()

    monkeypatch.setattr("client.requests.post", fake_post)

    result = send_task(
        endpoint="http://localhost:8001",
        task_id="task-001",
        objective="test communication",
        input_data={"value": 42},
    )

    assert result["status"] == "received"
    assert result["task_id"] == "task-001"
    assert result["input_data"]["value"] == 42


if __name__ == "__main__":
    print("OpenMindMesh client test: PASSED")
