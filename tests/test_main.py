import pytest
from src.main import (
    validate_amnt,
    total_tips_math,
    return_amount,
    return_date,
    sort_amount,
)


def test_validate_amnt_is_positive():
    """Testing amount value is positive money amount or 0"""

    assert validate_amnt(20) is True
    assert validate_amnt(0) is True
    assert validate_amnt(-1) is False


def test_validate_amnt_is_digit():
    """Test if Amount value is digit"""
    assert validate_amnt("abc") is False
    assert validate_amnt("") is False


# def test_total_tips_math():

# def test_return_amount():

# def test_return_date():

# def test_sort_amount():
