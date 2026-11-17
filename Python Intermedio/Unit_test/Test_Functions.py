import sys
import os
import pytest


functions_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Functions")
sys.path.append(functions_dir)

from Functions.count_vowels import count_vowels
from Functions.count_words_longerthan import count_letters
from Functions.find_word import find_word
from Functions.function_adder_listed import adder
from Functions.function_counter_lowercase_uppercase import counter_lowercase_uppercase
from Functions.function_reverse_string import reverse_string
from Functions.function_find_prime import find_prime
from Functions.function_sort_words import sort_words_by_hyphen

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("world") == 1
    assert count_vowels("Python") == 1
    assert count_vowels("") == 0

def test_count_letters():
    assert count_letters(["hello", "world", "hi"], 4) == ["hello", "world"]
    assert count_letters(["hello", "world"], 5) == []
    assert count_letters(["hello", "world"], 6) == []
    assert count_letters([], 1) == []

def test_find_word():
    assert find_word("hello world", "hello") == 1
    assert find_word("world peace, world news, world travel, world history, world culture, and world music", "world") == 6
    assert find_word("hello hello", "hello") == 2
    assert find_word("aaaa", "a") == 4
    assert find_word("hello world", "Python") == 0
    assert find_word("", "hello") == 0

def test_adder():
    assert adder([1, 2, 3]) == 6
    assert adder([0, 0, 0]) == 0
    assert adder([-1, 1, 0]) == 0
    assert adder([]) == 0

def test_counter_lowercase_uppercase():
    assert counter_lowercase_uppercase("Hello World") == (8, 2)
    assert counter_lowercase_uppercase("PYTHON") == (0, 6)
    assert counter_lowercase_uppercase("python") == (6, 0)
    assert counter_lowercase_uppercase("") == (0, 0)

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("world") == "dlrow"
    assert reverse_string("") == ""

def test_find_prime():
    assert find_prime([10, 2, 3, 4, 5, 7]) == [2, 3, 5, 7]
    assert find_prime([2, 2, 3]) == [2, 2, 3]
    assert find_prime([-1, 0, 1, 4]) == []
    assert find_prime([]) == []

def test_sort_words_by_hyphen():
    assert sort_words_by_hyphen("world-hello") == "hello-world"
    assert sort_words_by_hyphen("Python-is-fun") == "Python-fun-is"
    assert sort_words_by_hyphen("") == ""
