.PHONY: test
test:
	poetry run pytest

.PHONY: lint
lint:
	flake8 ./src ./tests ./core
