import smtplib
import pytest
from unittest import mock

def send_email(email_address, message):
    """
    Sends an email to the specified address with the given message.
    Uses the smtplib module and SMTP protocol.
    """
    smtp_server = smtplib.SMTP("smtp.example.com", 587)  # Replace with actual SMTP server details
    smtp_server.starttls()
    smtp_server.login("username", "password")  # Replace with actual login credentials
    smtp_server.sendmail("from@example.com", email_address, message)
    smtp_server.quit()

def notify_user(email_address, message):
    """
    Calls send_email to send an email to the specified address with the given message.
    Returns "Email sent successfully" if the email is sent successfully,
    otherwise "Failed to send email" if an exception occurs.
    """
    try:
        send_email(email_address, message)
        return "Email sent successfully"
    except Exception:
        return "Failed to send email"

def test_notify_user():
    """
    Unit test for notify_user function.
    Uses mock.patch to mock smtplib.SMTP and test different scenarios.
    """
    with mock.patch('smtplib.SMTP') as mock_smtp:
        instance = mock_smtp.return_value  # Mock the SMTP instance
        instance.sendmail.return_value = {}  # Set the return value for sendmail method

        # Test case: Successful email sending
        result = notify_user("test@example.com", "Hello, World!")
        assert result == "Email sent successfully"
        instance.sendmail.assert_called_once_with("from@example.com", "test@example.com", "Hello, World!")

        # Test case: Failed email sending (SMTP error)
        instance.sendmail.side_effect = Exception("SMTP error")
        result = notify_user("test@example.com", "Hello, World!")
        assert result == "Failed to send email"

test_notify_user()
