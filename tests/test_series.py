import pytest
from math_series import math_series


def test_fibonacci_one():
    actual = math_series.fibonacci(1)
    expected = 1
    assert expected == actual


def test_fibonacci_two():
    actual = math_series.fibonacci(2)
    expected = 1
    assert expected == actual


def test_fibonacci_zero():
    actual = math_series.fibonacci(0)
    expected = 0
    assert expected == actual


def test_fibonacci_ten():
    actual = math_series.fibonacci(10)
    expected = 55
    assert expected == actual


def test_fibonacci_minus_five():
    actual = math_series.fibonacci(-5)
    expected = "please enter positive term"
    assert expected == actual


def test_fibonacci_string():
    actual = math_series.fibonacci("ahmad")
    expected = "wrong input,please Enter integer value"
    assert expected == actual
