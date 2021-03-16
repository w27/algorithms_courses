import pytest
from tasks.bubble_sort import bubble_sort


@pytest.mark.parametrize("value, rez", [
    ([0, 2, 5, 6, -1], [-1, 0, 2, 5, 6]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    ([], [])
])
def test_bubble_sort_good(value, rez):
    assert rez == bubble_sort(value)

