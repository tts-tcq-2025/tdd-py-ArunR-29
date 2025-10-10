from string_calculator import string_calculator

def test_empty_string_returns_zero():
    assert string_calculator("") == 0

def test_multiple_numbers():
    assert string_calculator("1,2,3") == 6

def test_newline_and_comma_delimiters():
    assert string_calculator("1\n2,3") == 6

def test_custom_delimiter_semicolon():
    assert string_calculator("//;\n1;2") == 3

def test_negative_numbers_raise_exception():
    try:
        string_calculator("1,-2,-3")
    except Exception as e:
        assert str(e) == "negatives not allowed: -2, -3"

def test_ignore_numbers_greater_than_1000():
    assert string_calculator("2,1001") == 2

def test_custom_delimiter_any_length():
    assert string_calculator("//[***]\n1***2***3") == 6

test_empty_string_returns_zero()
test_multiple_numbers()
test_newline_and_comma_delimiters()
test_custom_delimiter_semicolon()
test_negative_numbers_raise_exception()
test_ignore_numbers_greater_than_1000()
test_custom_delimiter_any_length()
coverage run --branch import pytest.py
