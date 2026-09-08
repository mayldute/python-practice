"""
Implement a notification system using abstraction, polymorphism,
dependency injection, and the Template Method pattern.

Requirements:
- Create a User class that stores a name, email, and phone number.
- Validate that all User fields are strings.
- Validate that name and phone are not empty or whitespace-only.
- Validate that email contains the '@' character.
- Create an abstract NotificationSender class.
- Define a public send() method with shared user and message validation.
- Define an abstract _send() method for concrete notification senders.
- Implement EmailSender, SmsSender, and PushSender.
- Each sender must format and return its own notification message.
- Create NotificationService that receives a NotificationSender
  through dependency injection.
- NotificationService must delegate notification delivery to the sender.
- Do not use conditional logic to select a concrete sender.
- Adding a new sender must not require changing NotificationService.
"""

from abc import ABC, abstractmethod


class User:
    def __init__(self, name: str, email: str, phone: str):
        if (
            not isinstance(name, str)
            or not isinstance(email, str)
            or not isinstance(phone, str)
        ):
            raise TypeError("Name, email, and phone must be strings.")

        if "@" not in email:
            raise ValueError("Email must contain @.")

        if not name.strip() or not phone.strip():
            raise ValueError("Fields name and phone can not be empty.")

        self.name = name
        self.email = email
        self.phone = phone


class NotificationSender(ABC):
    def send(self, user: User, message: str) -> str:
        if not isinstance(user, User):
            raise TypeError("User must be an instance of User.")

        if not isinstance(message, str):
            raise TypeError("Message must be a string.")

        if not message.strip():
            raise ValueError("Message cannot be empty.")

        return self._send(user, message)

    @abstractmethod
    def _send(self, user: User, message: str) -> str: ...


class EmailSender(NotificationSender):
    def _send(self, user: User, message: str) -> str:
        return f"Email sent to {user.email}: {message}"


class SmsSender(NotificationSender):
    def _send(self, user: User, message: str) -> str:
        return f"SMS sent to {user.phone}: {message}"


class PushSender(NotificationSender):
    def _send(self, user: User, message: str) -> str:
        return f"Push notification sent to {user.name}: {message}"


class NotificationService:
    def __init__(self, sender: NotificationSender) -> None:
        if not isinstance(sender, NotificationSender):
            raise TypeError("Sender must be an instance of NotificationSender.")

        self.sender = sender

    def notify(self, user: User, message: str) -> str:
        return self.sender.send(user, message)
