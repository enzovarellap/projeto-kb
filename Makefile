.PHONY: install serve validate ingest index index-update sync-drive test lint format docker docker-run pre-commit-install

install:
	pip install -r requirements.txt

serve:
	python server.py

validate:
	python validate_okf.py

ingest:
	python ingest.py --src $(SRC) --out $(OUT) $(if $(TYPE),--type $(TYPE),)

index:
	python embeddings.py

index-update:
	python embeddings.py --update

sync-drive:
	python ingest_drive.py --folder-id $(FOLDER_ID) --out $(or $(OUT),kb/drive-import) $(if $(TYPE),--type $(TYPE),) $(if $(INCREMENTAL),--incremental,) $(if $(RECURSIVE),--recursive,)

test:
	pytest tests/ -v

lint:
	ruff check .

format:
	ruff format .

docker:
	docker build -t projeto-kb .

docker-run:
	docker run -p 8000:8000 --env-file .env projeto-kb

pre-commit-install:
	pip install pre-commit && pre-commit install
