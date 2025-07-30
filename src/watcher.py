import os
import time
from logger import log_event, log_failure
from memory import load_memory, save_memory

DATASET_DIR = "datasets"

os.makedirs(DATASET_DIR, exist_ok=True)


def watch(interval: int = 10) -> None:
    seen = set()
    mem = load_memory()
    while True:
        try:
            files = {
                f for f in os.listdir(DATASET_DIR)
                if f.endswith((".py", ".json", ".md", ".sh"))
            }
            new_files = files - seen
            for fname in new_files:
                path = os.path.join(DATASET_DIR, fname)
                with open(path, "r", errors="ignore") as fp:
                    mem[fname] = fp.read()
                log_event(f"ingested {fname}")
            if new_files:
                save_memory(mem)
            seen |= new_files
            time.sleep(interval)
        except KeyboardInterrupt:
            break
        except Exception as e:
            log_failure(f"watcher error: {e}")
            time.sleep(interval)

if __name__ == "__main__":
    watch()

