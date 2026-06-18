.PHONY: install serve validate ingest index index-update test

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

test:
	pytest tests/ -v
