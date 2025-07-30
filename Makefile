.PHONY: check format serve deploy

check:
ruff .

format:
ruff format .

serve:
uvicorn app:app --reload --port 8000

deploy:
git push
