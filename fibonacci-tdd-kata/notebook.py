# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.24.2",
#     "pytest==9.1.1",
# ]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import pytest


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # TDD Demo: Fibonacci with marimo

    This notebook illustrates the **Red → Green → Refactor** cycle of
    Test-Driven Development. Each section below corresponds to a
    development step where we **grow the contract** of the
    `fibonnacci` function one test at a time.

    You can run the tests in two ways:

    1. **Inside marimo**: cells whose name starts with `test_`
       are automatically detected and run by pytest.
    2. **From the command line**:
       ```bash
       uv run pytest tdd_fizzbuzz_marimo_en.py
       ```
    """)
    return


@app.function
def fibonacci(n):
    """
    Returns the fibonacci number for the integer n
    Input : an integer n >= 0
    Output : fibonacci number of n
    """
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    app.run()
