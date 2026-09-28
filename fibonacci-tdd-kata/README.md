Some commands to enter in the terminal to see if everything will compile on Github :

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest --cov=src/fibonacci_tdd_kata --cov-report=term-missing 