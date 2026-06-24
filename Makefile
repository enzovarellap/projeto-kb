.PHONY: install serve validate ingest index index-update sync-drive test

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
	python ingest_drive.py --folder-id $(FOLDER_ID) --out $(or $(OUT),kb/drive-import) $(if $(TYPE),--type $(TYPE),) $(if $(INCREMENTAL),--incremental,)

test:
	pytest tests/ -v
