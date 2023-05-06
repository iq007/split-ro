import pytest
from split import split2 as split


def test_should_split_letters_digits():
    # arrange
    my_ro = "RO12345"

    # act
    a, b = split(my_ro)

    # assert
    assert a == "RO"
    assert b == "12345"


def test_should_split_letters_digits_2():
    # arrange
    my_ro = "RO62345"

    # act
    a, b = split(my_ro)

    # assert
    assert a == "RO"
    assert b == "62345"


def test_should_split_unordered_letter_digits():
    # arrange
    my_ro = "1A23RO456"

    # act
    a, b = split(my_ro)

    # assert
    assert a == "ARO"
    assert b == "123456"
