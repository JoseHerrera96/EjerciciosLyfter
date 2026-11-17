import pytest
import random

from bubble_sort import bubble_sort


def test_bubble_sort_samll_list():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert bubble_sort([1]) == [1]

def test_bubble_sort_large_list():
    expected = list(range(1, 101))

    # Reversed
    assert bubble_sort(list(range(100, 0, -1))) == expected
    # Already sorted
    assert bubble_sort(list(range(1, 101))) == expected
    # Odds followed by evens
    assert bubble_sort(list(range(1, 101, 2)) + list(range(2, 101, 2))) == expected
    # Random shuffles
    for seed in range(5):
        data = list(range(1, 101))
        random.Random(seed).shuffle(data)
        assert bubble_sort(data) == expected
    # Random values with duplicates
    rng = random.Random(42)
    data = [rng.randint(0, 50) for _ in range(100)]
    assert bubble_sort(data.copy()) == sorted(data)

def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []

def test_bubble_sort_not_a_list():
    with pytest.raises(AttributeError):
        bubble_sort("not a list")
    with pytest.raises(AttributeError):
        bubble_sort(123)
    with pytest.raises(AttributeError):
        bubble_sort(None)

