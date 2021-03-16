import math
import pytest
from tasks.factorial import factorial_iterative, factorial_recursive


@pytest.mark.parametrize("value", [7, 1, 12, 0])
def test_factorial_iterative_good(value):
    assert math.factorial(value) == factorial_iterative(value), "This is not a factorial!"


def test_factorial_iterative_bad():
    with pytest.raises(ValueError):
        factorial_iterative(-123)
        "Need reise ValueError"


@pytest.mark.parametrize("value", [7, 1, 12, 0])
def test_factorial_recursive_good(value):
    assert math.factorial(value) == factorial_recursive(value), "This is not a factorial!"


def test_factorial_recursive_bad():
    with pytest.raises(ValueError):
        factorial_recursive(-123), "Need reise ValueError"
