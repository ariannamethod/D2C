import os
from datetime import datetime

LOG_DIR = "logs"
FAIL_DIR = "failures"

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(FAIL_DIR, exist_ok=True)


def log_event(message: str) -> None:
    path = os.path.join(LOG_DIR, "events.log")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.utcnow().isoformat()} {message}\n")


def log_failure(message: str) -> None:
    path = os.path.join(FAIL_DIR, "fail.log")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.utcnow().isoformat()} {message}\n")
