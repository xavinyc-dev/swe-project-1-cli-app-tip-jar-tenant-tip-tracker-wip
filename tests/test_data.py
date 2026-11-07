from datetime import datetime
import pytest
from src.data import (
    validate_amnt,
    total_tips_math,
    return_amount,
    return_date,
    sort_amount,
    sort_date,
    transform_date,
    search_year,
    validate_date,
    validate_year,
    return_tip_from_id,
    remove_tip,
    build_tip,
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


def test_search_year():
    """Returns list of tips in inputted year"""
    assert search_year("2025", tips_jar) == [
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
    ]
    assert search_year("2026", tips_jar) == [
        {
            "ID": 3,
            "Tenant": "Michael",
            "Apartment": "1204",
            "Amount": 33.25,
            "Tip Type": "Cash",
            "Description": "",
            "Date": "01-26-2026",
        }
    ]


def test_validate_date():
    """Validate its a valid date using datetime library"""
    assert validate_date("12-25-2025") is True
    assert validate_date("1-25-2025") is True
    assert validate_date("00-24-2020") is False
    assert validate_date("") is False


def test_validate_year():
    """Validates input is a valid year"""
    assert validate_year("2026") is True
    assert validate_year("2023") is True
    assert validate_year("-2026") is False
    assert validate_year("") is False


def test_return_tip_from_id():
    """Returns dictionary of tip from tips_jar with inputted id"""
    assert return_tip_from_id(2, tips_jar) == {
        "ID": 2,
        "Tenant": "Elisa",
        "Apartment": "1203",
        "Amount": 55.25,
        "Tip Type": "Cash",
        "Description": "",
        "Date": "12-26-2025",
    }
    assert return_tip_from_id(99, tips_jar) is None


def test_build_tip():
    assert build_tip(
        tip_id=1,
        tenant="xavi",
        apt="1202W",
        amnt=25.00,
        tip_type="zelle",
        desc="",
        date="12-25-2025",
    ) == {
        "ID": 1,
        "Tenant": "Xavi",
        "Apartment": "1202W",
        "Amount": 25.00,
        "Tip Type": "Zelle",
        "Description": "",
        "Date": "12-25-2025",
    }


# Only add tests above this to not accidentally delete anything until I learn about shallow and deep
def test_remove_tip():
    """Test remove tip from tips_jar list"""
    copy_tips_jar = list(tips_jar)
    assert remove_tip(2, copy_tips_jar) == [
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
    ]
