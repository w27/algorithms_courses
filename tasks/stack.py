"""
Stack
"""
from typing import Any


def push(data: Any) -> None:
    """
    Add element to stack
    :param data: element to be pushed
    """
    print(data)


def pop() -> Any:
    """
    Pop element from the stack. If not elements return None.
    :return: popped element
    """
    pass


def peek(index: int) -> Any:
    """
    See the element in the stack without popping it.
    :param index: index of element
    :return: peeked element
    """
    print(index)


def clear() -> None:
    """
    Clear stack
    """
    pass
