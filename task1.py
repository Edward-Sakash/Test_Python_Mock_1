import random
import pytest
from unittest import mock


def get_random_number():
    """
    Generates a random number between 1 and 10 using random.randint.
    """
    return random.randint(1, 10)


def check_random_number():
    """
    Calls get_random_number and checks if the number is greater than 5.
    Returns "Greater than 5" if the number is greater than 5, otherwise "Less than or equal to 5".
    """
    number = get_random_number()
    if number > 5:
        return "Greater than 5"
    else:
        return "Less than or equal to 5"


def test_check_random_number():
    """
    Unit test for check_random_number function.
    Uses mock.patch to mock random.randint and test different scenarios.
    """
    with mock.patch("random.randint") as mock_randint:
        # Mock random.randint to return 7
        mock_randint.return_value = 7
        result = check_random_number()
        assert result == "Greater than 5"

        # Mock random.randint to return 3
        mock_randint.return_value = 3
        result = check_random_number()
        assert result == "Less than or equal to 5"


test_check_random_number()

"""
In the code provided, return_value is an attribute of the Mock object
returned by mock.patch when used as a context manager (with statement).

In the context of mocking, return_value is used to set the value that
will be returned when the mocked function or method is called. It allows you
to specify the desired return value for the mocked function so that you can
control its behavior during testing.

In the test_check_random_number function, return_value is used to define
the return values for the random.randint function when it is called within
the check_random_number function. By setting mock_randint.return_value = 7,
it ensures that random.randint(1, 10) will always return 7 within the scope
of the with block. Similarly, mock_randint.return_value = 3 is used to set
the return value to 3.

These return values allow you to test different scenarios in
the check_random_number function. By mocking the behavior of random.randint,
you can control the random number generation and ensure predictable results
for testing purposes.
"""
