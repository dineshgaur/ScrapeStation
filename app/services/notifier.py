from abc import ABC, abstractmethod


class BaseNotifier(ABC):
    """
    Abstract base class for notification mechanisms.
    """
    @abstractmethod
    def notify(self, message: str):
        """
        Send a notification with the given message.

        Args:
        - message: The message to be sent.
        """
        pass


class ConsoleNotifier(BaseNotifier):
    """
    Concrete implementation of notification via console.
    """

    def notify(self, message: str):
        """
        Prints the notification message to the console.

        Args:
        - message: The message to be displayed.
        """
        print(f"[Notification] {message}")
