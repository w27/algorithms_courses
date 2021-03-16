import pytest
from tasks.queue import *


def test_empty_good():
    assert dequeue() is None, "stack is not empty"


def test_clear_good():
    enqueue(8)
    clear()
    assert dequeue() is None, "clear the stack"


@pytest.mark.parametrize("value", [3, 5, 6, 7, 9])
def test_push_pop_good1(value):
    enqueue(value)
    assert value == dequeue()


def test_push_pop_good2():
    enqueue(1)
    enqueue(2)
    enqueue(3)
    enqueue(4)
    assert 1 == dequeue()
    assert 2 == dequeue()
    assert 3 == dequeue()
    assert 4 == dequeue()
    assert dequeue() is None


def test_peek_good():
    enqueue(1)
    enqueue(2)
    enqueue(3)
    enqueue(4)
    assert 1 == peek(0)
    assert 2 == peek(1)
    assert 3 == peek(2)
    assert 4 == peek(3)
    assert peek(4) is None
