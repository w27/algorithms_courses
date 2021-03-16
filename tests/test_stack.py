# import pytest
# from tasks.stack import *
#
#
# def test_empty_good():
#     assert pop() is None, "stack is not empty"
#
#
# def test_clear_good():
#     push(8)
#     clear()
#     assert pop() is None, "clear the stack"
#
#
# @pytest.mark.parametrize("value", [3, 5, 6, 7, 9])
# def test_push_pop_good1(value):
#     push(value)
#     assert value == pop()
#
#
# def test_push_pop_good2():
#     push(1)
#     push(2)
#     push(3)
#     push(4)
#     assert 4 == pop()
#     assert 3 == pop()
#     assert 2 == pop()
#     assert 1 == pop()
#     assert pop() is None
#
#
# def test_peek_good():
#     push(1)
#     push(2)
#     push(3)
#     push(4)
#     assert 4 == peek(0)
#     assert 3 == peek(1)
#     assert 2 == peek(2)
#     assert 1 == peek(3)
#     assert peek(4) is None
