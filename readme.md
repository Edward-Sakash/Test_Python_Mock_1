# Exercise 1 (Mock - random):
Write a function called get_random_number that uses the random module to generate a random number between 1 and 10.
In your unit test, you need to mock the random.randint function to return a predefined value and ensure that your function handles it correctly.
import random

def get_random_number():
    return random.randint(1, 10)

# The function to test
def check_random_number():
    number = get_random_number()
    if number > 5:
        return "Greater than 5"
    else:
        return "Less than or equal to 5"

# Unit test using pytest and mocking
import pytest
from unittest import mock

def test_check_random_number():
    with mock.patch('random.randint') as mock_randint:
        mock_randint.return_value = 7
        result = _______
        assert result == ________

        mock_randint.return_value = 3
        result = _________
        assert result == _______


# Bonus - Exercise (Mock -emails):
Write a function called send_email that takes two parameters: email_address (string) and message (string).
The function should use the smtplib module to send an email to the specified address with the given message.
In your unit test, you need to mock the smtplib.SMTP class to ensure that your function is called with the correct parameters and that the email is sent successfully.
