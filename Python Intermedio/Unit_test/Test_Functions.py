import sys
import os
import pytest

sys.path.append(os.path.abspath("Python Intermedio\\Unit_test\\Functions"))

from count_vowels import count_vowels
from Count_words_longerthan import count_letters
from find_word import find_word
from function_adder_listed import adder
from function_counter_lowercase_uppercase import counter_lowercase_uppercase
from function_reverse_string import reverse_string
from function_find_prime import find_prime
from function_sort_words import sort_words_by_hyphen


# Test cases for the imported functions

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("world") == 1
    assert count_vowels("Python") == 1
    assert count_vowels("") == 0

def test_count_letters():
    assert count_letters("hello world", 4) == 2
    assert count_letters("hello world", 5) == 1
    assert count_letters("hello world", 6) == 0
    assert count_letters("", 1) == 0

def test_find_word():
    assert find_word("hello world", "hello") == True
    assert find_word("hello world", "world") == True
    assert find_word("hello world", "Python") == False
    assert find_word("", "hello") == False

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
    assert find_prime(2) == True
    assert find_prime(3) == True
    assert find_prime(4) == False
    assert find_prime(1) == False

def test_sort_words_by_hyphen():
    assert sort_words_by_hyphen("hello world") == ["hello", "world"]
    assert sort_words_by_hyphen("Python is fun") == ["Python", "fun", "is"]
    assert sort_words_by_hyphen("") == []
