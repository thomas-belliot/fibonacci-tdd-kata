# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.24.2",
#     "numpy==2.5.3",
#     "pytest==9.1.1",
# ]
# ///

import marimo

__generated_with = "0.25.0"
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
       uv run pytest notebook.py
       ```
    """)


@app.function
def fibonacci(n):
    """
    Returns the fibonacci number for the integer n
    Input : an integer n >= 0
    Output : fibonacci number of n
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be an integer an positive")
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@app.function
def test_v1_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(8) == 21
    assert fibonacci(12) == 144
    assert fibonacci(15) == 610
    # For n=100, I stopped my computer at 3min of compilation,
    # without having reach the result in the mean time.


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


@app.cell
def _():
    n_input = mo.ui.number(start=1, stop=1000, step=1, value=15, label="n")
    return (n_input,)


@app.cell
def _(n_input):
    try:
        result = fibonacci(n_input.value)
        output = mo.md(f"`fibonacci({n_input.value})` → **{result}**")
    except ValueError as e:
        output = mo.md(f"⚠️ Error: {e}")
    return output


app._unparsable_cell(
    """
    # \"Refactor and optimize your code to reduce the computation time of your Fibonacci function\"
    # Examples on this website : https://www.datacamp.com/fr/tutorial/fibonacci-sequence-python
    import numpy as np

    def fibonacci_matrix(n):
        \"\"\"
        Returns the fibonacci number for the integer n
        Input : an integer n >= 0
        Output : fibonacci number of n
        \"\"\"
        if not isinstance(n, int) or n<0:
            raise ValueError(\"n must be an integer an positive\")
        def matrix_power(matrix, power):
            return np.linalg.matrix_power(matrix, power)
        if n == 0:
            return 0
        matrix = np.array([[1, 1], [1, 0]])
        result = matrix_power(matrix, n-1)
        return result[0][0]
    """,
    name="_",
)


@app.cell
def _(fibonacci_matrix):
    def test_v2_fibonacci_matrix():
        assert fibonacci_matrix(0) == 0
        assert fibonacci_matrix(1) == 1
        assert fibonacci_matrix(8) == 21
        assert fibonacci_matrix(12) == 144
        assert fibonacci_matrix(15) == 610
        # This time the result is almost immediate for more larger than 100 value of n !
        assert fibonacci_matrix(100) == 3736710778780434371
        assert fibonacci_matrix(500) == 2171430676560690477
        assert fibonacci_matrix(1000) == 817770325994397771
        assert fibonacci_matrix(5000) == 535601498209671957


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
