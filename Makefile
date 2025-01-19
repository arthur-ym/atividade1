
# Target to invoke the poetry lock process
lock:
	@echo "Starting the lock process..."
	@python3 -m pip install -q poetry==1.8.3
	@poetry lock

# Target to invoke the quality process
quality:
	@echo "Starting the quality process..."
	@poetry install --no-dev
	@poetry run pre-commit install
	@poetry run pre-commit run --all-files

# Target to invoke the testing process
tests:
	@echo "Starting the tests process..."
	@poetry install
	@poetry run pytest --cov=. --cov-fail-under=70
