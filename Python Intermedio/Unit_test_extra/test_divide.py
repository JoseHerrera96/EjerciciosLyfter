import pytest

def divide(number1, number2):
    if number2 == 0:
        raise ValueError("No se puede dividir por cero")
    return number1 / number2

def test_divide_positive_numbers():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_divide_string_input():
    with pytest.raises(TypeError):
        divide("10", 2)
    with pytest.raises(TypeError):
        divide(10, "2")

if __name__ == "__main__":
    pytest.main()
