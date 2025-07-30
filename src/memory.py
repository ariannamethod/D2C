import json
import os

MEM_DIR = "mem"
MEM_FILE = os.path.join(MEM_DIR, "memory.json")

os.makedirs(MEM_DIR, exist_ok=True)


def load_memory() -> dict:
    if os.path.exists(MEM_FILE):
        with open(MEM_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_memory(mem: dict) -> None:
    with open(MEM_FILE, "w", encoding="utf-8") as f:
        json.dump(mem, f, indent=2)
