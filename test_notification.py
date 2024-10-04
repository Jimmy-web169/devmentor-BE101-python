import unittest
from unittest.mock import patch
from notification import Email, SMS, Telegram, Line
from user import User

class TestNotification(unittest.TestCase):

    def setUp(self):
        self.user = User(id="A0001", email="jimmy@example.com", phone="0912345678", prefers_language="zh-TW")

    @patch('builtins.print')
    def test_email_notification(self, mock_print):
        email = Email()
        email.send_message("Test Email", self.user)
        mock_print.assert_called_with("Sending Email to jimmy@example.com: Test Email")

    @patch('builtins.print')
    def test_sms_notification(self, mock_print):
        sms = SMS()
        sms.send_message("Test SMS", self.user)
        mock_print.assert_called_with("Sending SMS to 0912345678: Test SMS")

    @patch('builtins.print')
    def test_telegram_notification(self, mock_print):
        telegram = Telegram()
        telegram.send_message("Test Telegram", self.user)
        mock_print.assert_called_with("Sending Telegram message to A0001: Test Telegram")

    @patch('builtins.print')
    def test_line_notification(self, mock_print):
        line = Line()
        line.send_message("Test Line", self.user)
        mock_print.assert_called_with("Sending Line message to A0001: Test Line")
    
    @patch('builtins.print')
    def test_email_notification_failure(self, mock_print):
        email = Email()
        email.send_message("Test Email", self.user)
        with self.assertRaises(AssertionError):
            mock_print.assert_called_with("Sending Email to jimmy@example.com: Test Email failed")
    @patch('builtins.print')
    def test_sms_notification_failure(self, mock_print):
        sms = SMS()
        sms.send_message("Test SMS", self.user)
        with self.assertRaises(AssertionError):
            mock_print.assert_called_with("Sending SMS to 0912345678: Test SMS failed")
    @patch('builtins.print')
    def test_telegram_notification_failure(self, mock_print):
        telegram = Telegram()
        telegram.send_message("Test Telegram", self.user)
        with self.assertRaises(AssertionError):
            mock_print.assert_called_with("Sending Telegram message to A0001: Test Telegram failed")
    @patch('builtins.print')
    def test_line_notification_failure(self, mock_print):
        line = Line()
        line.send_message("Test Line", self.user)
        with self.assertRaises(AssertionError):
            mock_print.assert_called_with("Sending Line message to A0001: Test Line failed")

if __name__ == '__main__':
    unittest.main()