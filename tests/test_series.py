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
    expected = "please enter positive nth-term"
    assert expected == actual


def test_fibonacci_not_integer():
    actual = math_series.fibonacci("ahmad")
    expected = "wrong input,please Enter integer value"
    assert expected == actual


def test_lucas_one():
    actual = math_series.lucas(1)
    expected = 2
    assert expected == actual


def test_lucas_eight():
    actual = math_series.lucas(8)
    expected = 29
    assert expected == actual


def test_lucas_negative():
    actual = math_series.lucas(-8)
    expected = "please enter positive nth-term"
    assert expected == actual


def test_lucas_not_integer():
    actual = math_series.lucas("blablabla")
    expected = "wrong input,please Enter integer value"
    assert expected == actual
