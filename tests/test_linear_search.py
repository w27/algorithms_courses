# import pytest
# from tasks.linear_search import linear_search
#
# arr = [i for i in range(100)] + [101]
#
#
# @pytest.mark.parametrize("value, rez", [
#     (1, 1),
#     (0, 0),
#     (101, 100),
#
# ])
# def test_binary_search_good1(value, rez):
#     assert rez == linear_search(value, arr)
#
#
# def test_binary_search_good2():
#     assert 2 == linear_search(2, [0, 1, 2, 2, 2, 2]), "need first occurrence element in list"
#
#
# def test_binary_search_bad():
#     with pytest.raises(ValueError):
#         linear_search(100, arr), "Need reise ValueError"
#
#
#
