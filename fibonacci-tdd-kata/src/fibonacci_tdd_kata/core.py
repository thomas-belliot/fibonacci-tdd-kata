import numpy as np


# Rule about annotation : https://typing.python.org/en/latest/spec/annotations.html
def fibonacci(n: int) -> int:
    """
    Returns the fibonacci number for the integer n
    Input : an integer n >= 0
    Output : fibonacci number of n
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be an integer an positive")
    if n == 0:
        return 0
    matrix = np.array([[1, 1], [1, 0]])
    result = np.linalg.matrix_power(matrix, n - 1)
    return int(result[0][0])
