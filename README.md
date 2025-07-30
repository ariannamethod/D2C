# D2C

D2C is a lightweight CPU‑only language model agent. The repository contains a minimal implementation of a self‑contained model with simple logging, memory and dataset watching utilities.

## Structure
- `src/` — core source code
  - `model.py` — minimal GPT style model and tokenizer
  - `core_infer.py` — CPU inference script
  - `logger.py` — event and failure logging
  - `memory.py` — persistent memory storage
  - `trainer.py` — placeholder training loop
  - `watcher.py` — watches the `datasets/` directory for new files and updates memory
- `datasets/` — place training files here (used by `watcher.py`)
- `logs/` and `failures/` — runtime logs
- `mem/` — memory snapshots

## Usage
Install dependencies:
```bash
pip install -r requirements.txt
```

Run the dataset watcher (ctrl‑c to stop):
```bash
python -m watcher
```

Generate text with the model:
```bash
python -m core_infer --start "Hello" --num_tokens 20
```

The agent runs entirely on the CPU and performs no external API calls.
