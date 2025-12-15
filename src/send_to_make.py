import json
import requests
import os

MAKE_WEBHOOK_URL = os.getenv("MAKE_WEBHOOK_URL")

if not MAKE_WEBHOOK_URL:
    raise RuntimeError("MAKE_WEBHOOK_URL environment variable is not set")

def send_to_make(payload: dict):
    response = requests.post(
        MAKE_WEBHOOK_URL,
        json=payload,
        timeout=10
    )
    response.raise_for_status()


def run():
    with open("output.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    send_to_make(data)
    print("Payload sent to Make")


if __name__ == "__main__":
    run()
