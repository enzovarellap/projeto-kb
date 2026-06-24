.PHONY: install serve validate ingest index index-update sync-drive test test-cov lint docker-build

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

test-cov:
	pytest tests/ -v --cov=. --cov-report=term-missing --cov-fail-under=70

lint:
	ruff check .

docker-build:
	docker build -t projeto-kb .
