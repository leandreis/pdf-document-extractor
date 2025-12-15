import json
import requests

from config import MAKE_WEBHOOK_URL

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
