import sys
import os

sys.path.append(os.path.abspath("Python Intermedio\\Unit_test\\Functions"))

from count_vowels import count_vowels
from Count_words_longerthan import Count_words_longerthan
from find_word import find_word
from function_adder_listed import function_adder_listed
from function_counter_lowercase_uppercase import function_counter_lowercase_uppercase
from function_reverse_string import function_reverse_string
from function_find_prime import function_find_prime
from function_sort_words import function_sort_words


# Test cases for the imported functions

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("world") == 1
    assert count_vowels("Python") == 1
    assert count_vowels("") == 0

def test_Count_words_longerthan():
    assert Count_words_longerthan("hello world", 4) == 2
    assert Count_words_longerthan("hello world", 5) == 1
    assert Count_words_longerthan("hello world", 6) == 0
    assert Count_words_longerthan("", 1) == 0

def test_find_word():
    assert find_word("hello world", "hello") == True
    assert find_word("hello world", "world") == True
    assert find_word("hello world", "Python") == False
    assert find_word("", "hello") == False

def test_function_adder_listed():
    assert function_adder_listed([1, 2, 3]) == 6
    assert function_adder_listed([0, 0, 0]) == 0
    assert function_adder_listed([-1, 1, 0]) == 0
    assert function_adder_listed([]) == 0

def test_function_counter_lowercase_uppercase():
    assert function_counter_lowercase_uppercase("Hello World") == (8, 2)
    assert function_counter_lowercase_uppercase("PYTHON") == (0, 6)
    assert function_counter_lowercase_uppercase("python") == (6, 0)
    assert function_counter_lowercase_uppercase("") == (0, 0)

def test_function_reverse_string():
    assert function_reverse_string("hello") == "olleh"
    assert function_reverse_string("world") == "dlrow"
    assert function_reverse_string("") == ""

def test_function_find_prime():
    assert function_find_prime(2) == True
    assert function_find_prime(3) == True
    assert function_find_prime(4) == False
    assert function_find_prime(1) == False

def test_function_sort_words():
    assert function_sort_words("hello world") == ["hello", "world"]
    assert function_sort_words("Python is fun") == ["Python", "fun", "is"]
    assert function_sort_words("") == []
