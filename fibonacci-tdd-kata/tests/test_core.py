# tests/test_core.py

from fibonacci_tdd_kata.core import fibonacci


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(8) == 21
    assert fibonacci(12) == 144
    assert fibonacci(15) == 610
    # This time the result is almost immediate for more larger than 100 value of n !
    assert fibonacci(100) == 3736710778780434371
    assert fibonacci(500) == 2171430676560690477
    assert fibonacci(1000) == 817770325994397771
    assert fibonacci(5000) == 535601498209671957
