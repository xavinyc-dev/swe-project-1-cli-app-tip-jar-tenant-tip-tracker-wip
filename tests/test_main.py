from datetime import datetime
import pytest
from src.main import (
    validate_amnt,
    total_tips_math,
    return_amount,
    return_date,
    sort_amount,
    sort_date,
    transform_date,
)

tips_jar = [
    {
        "ID": 1,
        "Tenant": "Xavi",
        "Apartment": "1202",
        "Amount": 25.00,
        "Tip Type": "Cash",
        "Description": "",
        "Date": "12-25-2025",
    },
    {
        "ID": 2,
        "Tenant": "Elisa",
        "Apartment": "1203",
        "Amount": 55.25,
        "Tip Type": "Cash",
        "Description": "",
        "Date": "12-26-2025",
    },
    {
        "ID": 3,
        "Tenant": "Michael",
        "Apartment": "1204",
        "Amount": 33.25,
        "Tip Type": "Cash",
        "Description": "",
        "Date": "01-26-2026",
    },
]


def test_validate_amnt_is_positive():
    """Testing amount value is positive money amount or 0"""

    assert validate_amnt(20) is True
    assert validate_amnt(0) is True
    assert validate_amnt(-1) is False


def test_validate_amnt_is_digit():
    """Test if Amount value is digit"""
    assert validate_amnt("abc") is False
    assert validate_amnt("") is False


def test_total_tips_math():
    """Adds all the tips amounts to one value"""
    assert total_tips_math(tips_jar) == 113.5


def test_return_amount():
    """Returns the amount value of one tip"""
    assert return_amount(tips_jar[0]) == 25.00
    assert return_amount(tips_jar[1]) == 55.25
    assert return_amount(tips_jar[2]) == 33.25


def test_return_date():
    """Turns date stored as string into date format then returns"""
    assert return_date(tips_jar[0]) == datetime(2025, 12, 25)
    assert return_date(tips_jar[1]) == datetime(2025, 12, 26)
    assert return_date(tips_jar[2]) == datetime(2026, 1, 26)


def test_sort_amount():
    """sorts the tips high to low or low to high based on selection"""
    # High to low
    assert sort_amount(1, tips_jar) == [
        {
            "ID": 2,
            "Tenant": "Elisa",
            "Apartment": "1203",
            "Amount": 55.25,
            "Tip Type": "Cash",
            "Description": "",
            "Date": "12-26-2025",
        },
        {
            "ID": 3,
            "Tenant": "Michael",
            "Apartment": "1204",
            "Amount": 33.25,
            "Tip Type": "Cash",
            "Description": "",
            "Date": "01-26-2026",
        },
        {
            "ID": 1,
            "Tenant": "Xavi",
            "Apartment": "1202",
            "Amount": 25.00,
            "Tip Type": "Cash",
            "Description": "",
            "Date": "12-25-2025",
        },
    ]
    # Low to High
    assert sort_amount(2, tips_jar) == [
        {
            "ID": 1,
            "Tenant": "Xavi",
            "Apartment": "1202",
            "Amount": 25.00,
            "Tip Type": "Cash",
            "Description": "",
            "Date": "12-25-2025",
        },
        {
            "ID": 3,
            "Tenant": "Michael",
            "Apartment": "1204",
            "Amount": 33.25,
            "Tip Type": "Cash",
            "Description": "",
            "Date": "01-26-2026",
        },
        {
            "ID": 2,
            "Tenant": "Elisa",
            "Apartment": "1203",
            "Amount": 55.25,
            "Tip Type": "Cash",
            "Description": "",
            "Date": "12-26-2025",
        },
    ]


def test_sort_date():
    """sorts the tips most recent to furthest date based on selection"""
    # Most recent to furthest
    assert sort_date(3, tips_jar) == [
        {
            "ID": 3,
            "Tenant": "Michael",
            "Apartment": "1204",
            "Amount": 33.25,
            "Tip Type": "Cash",
            "Description": "",
            "Date": "01-26-2026",
        },
        {
            "ID": 2,
            "Tenant": "Elisa",
            "Apartment": "1203",
            "Amount": 55.25,
            "Tip Type": "Cash",
            "Description": "",
            "Date": "12-26-2025",
        },
        {
            "ID": 1,
            "Tenant": "Xavi",
            "Apartment": "1202",
            "Amount": 25.00,
            "Tip Type": "Cash",
            "Description": "",
            "Date": "12-25-2025",
        },
    ]
    # Furthest to most recent
    assert sort_date(4, tips_jar) == [
        {
            "ID": 1,
            "Tenant": "Xavi",
            "Apartment": "1202",
            "Amount": 25.00,
            "Tip Type": "Cash",
            "Description": "",
            "Date": "12-25-2025",
        },
        {
            "ID": 2,
            "Tenant": "Elisa",
            "Apartment": "1203",
            "Amount": 55.25,
            "Tip Type": "Cash",
            "Description": "",
            "Date": "12-26-2025",
        },
        {
            "ID": 3,
            "Tenant": "Michael",
            "Apartment": "1204",
            "Amount": 33.25,
            "Tip Type": "Cash",
            "Description": "",
            "Date": "01-26-2026",
        },
    ]


def test_transform_date():
    """Transforms date into correct format"""
    assert transform_date("12-25-2025") == "12-25-2025"
    assert transform_date("1-2-2025") == "01-02-2025"
