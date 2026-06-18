.PHONY: install serve validate ingest test

install:
	pip install -r requirements.txt

serve:
	python server.py

validate:
	python validate_okf.py

ingest:
	python ingest.py --src $(SRC) --out $(OUT) $(if $(TYPE),--type $(TYPE),)

test:
	pytest tests/ -v
