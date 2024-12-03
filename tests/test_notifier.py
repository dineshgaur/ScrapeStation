import unittest
from unittest.mock import patch
from app.services.notifier import ConsoleNotifier


class TestConsoleNotifier(unittest.TestCase):
    @patch("builtins.print")
    def test_notify(self, mock_print):
        """
        Test that the notify method prints the correct message.
        """
        notifier = ConsoleNotifier()
        test_message = "Scraping completed: 10 products scraped."
        notifier.notify(test_message)

        # Assert that print was called with the correct message
        mock_print.assert_called_once_with(f"[Notification] {test_message}")


if __name__ == "__main__":
    unittest.main()
