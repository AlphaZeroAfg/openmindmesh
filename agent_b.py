import uvicorn

from server import app


if __name__ == "__main__":
    print("OpenMindMesh Agent B starting...")
    print("Listening on http://localhost:8001")

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8001,
    )
