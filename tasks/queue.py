"""
Queue
"""
from typing import Any


def enqueue(data: Any) -> None:
    """
    Add element to the queue
    :param data: element to be added
    """
    print(data)


def dequeue() -> Any:
    """
    Return element and remove it.
    :return: dequeued element
    """
    pass


def peek(index: int) -> Any:
    """
    See the element in the queue
    :param index: index of element
    :return: peeked element
    """
    print(index)


def clear() -> None:
    """
    Clear queue
    """
    pass
