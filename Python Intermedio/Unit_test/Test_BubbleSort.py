import pytest
from BubbleSort import bubble_sort


def test_bubble_sort_samll_list():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert bubble_sort([1]) == [1]

def test_bubble_sort_large_list():
    assert bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert bubble_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert bubble_sort([5, 1, 9, 3, 7, 2, 8, 4, 6, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert bubble_sort([10, 8, 6, 4, 2, 9, 7, 5, 3, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert bubble_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []

def test_bubble_sort_not_a_list():
    with pytest.raises(TypeError):
        bubble_sort("not a list")
    with pytest.raises(TypeError):
        bubble_sort(123)
    with pytest.raises(TypeError):
        bubble_sort(None)

