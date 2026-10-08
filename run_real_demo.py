import subprocess
import sys
import time

import requests

from network_verification import request_verification
from schemas import EvidenceRecord


def main():
    print("=== OpenMindMesh REAL TWO-AGENT DEMO ===")

    print("\nStarting Agent B...")
    server = subprocess.Popen(
        [sys.executable, "agent_b.py"]
    )

    try:
        print("Waiting for Agent B...")
        for _ in range(20):
            try:
                response = requests.get(
                    "http://localhost:8001/health",
                    timeout=1,
                )

                if response.status_code == 200:
                    print("Agent B is ready.")
                    break

            except requests.RequestException:
                time.sleep(0.5)
        else:
            raise RuntimeError("Agent B did not start.")

        print("\nStarting Agent A...")
        subprocess.run(
            [sys.executable, "agent_a.py"],
            check=True,
        )

        print("\n[A] → VERIFY_REQUEST → [B]")

        evidence = EvidenceRecord(
            claim="Task was executed successfully",
            evidence_type="execution_log",
            payload={
                "agent": "agent-b",
                "task": "task-real-003",
            },
            uncertainty_score=0.0,
        )

        verification = request_verification(
            task_id="task-real-003",
            target_agent_id="agent-b",
            evidence=evidence,
        )

        if verification["status"] != "verified":
            raise RuntimeError("Network verification failed.")

        print("\n[B] → VERIFY_RESULT → [A]")
        print(verification)

        print("\n=== REAL NETWORK VERIFICATION: PASSED ===")
        print("\n=== REAL TWO-AGENT COMMUNICATION: PASSED ===")

    finally:
        print("\nStopping Agent B...")
        server.terminate()
        server.wait(timeout=5)


if __name__ == "__main__":
    main()
