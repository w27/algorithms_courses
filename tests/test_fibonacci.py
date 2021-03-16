import pytest
from tasks.fibonacci import fibonacci_recursive, fibonacci_iterative


@pytest.mark.parametrize("value, rez", [(8, 21), (9, 34), (1, 1), (2, 1)])
def test_factorial_iterative_good(value, rez):
    assert rez == fibonacci_iterative(value), "This is not a fibonacci!"


def test_factorial_iterative_bad():
    with pytest.raises(ValueError):
        fibonacci_iterative(-123), "Need reise ValueError"


@pytest.mark.parametrize("value, rez", [(8, 21), (9, 34), (1, 1), (2, 1)])
def test_factorial_recursive_good(value, rez):
    assert rez == fibonacci_recursive(value), "This is not a fibonacci!"


def test_factorial_recursive_bad():
    with pytest.raises(ValueError):
        fibonacci_recursive(-123)
        "Need reise ValueError"
