import pytest
from tasks.quick_sort import quick_sort


@pytest.mark.parametrize("value, rez", [
    ([0, 2, 5, 6, -1], [-1, 0, 2, 5, 6]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    ([], [])
])
def test_quick_sort_good(value, rez):
    assert rez == quick_sort(value)

