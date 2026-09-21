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
    if not isinstance(n, int) or n<0:
        raise ValueError("n must be an integer an positive")
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


@app.function
def test_v1_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(8) == 21
    assert fibonacci(12) == 144
    assert fibonacci(15) == 610
    return


@app.function
@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (5, 5),
        (6, 8),
        (10, 55),
        (15, 610),
    ],
)
def test_cases(n, expected):
    assert fibonacci(n) == expected


@app.function
def test_fibonacci_rejects_invalid_input():
    with pytest.raises(ValueError):
        fibonacci(-5)
    with pytest.raises(ValueError):
        fibonacci(-9)
    return


@app.cell
def _():
    n_input = mo.ui.number(start=1, stop=1000, step=1, value=15, label="n")
    n_input
    return (n_input,)


@app.cell
def _(n_input):
    try:
        result = fibonacci(n_input.value)
        output = mo.md(f"`fibonacci({n_input.value})` → **{result}**")
    except ValueError as e:
        output = mo.md(f"⚠️ Error: {e}")
    output
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
