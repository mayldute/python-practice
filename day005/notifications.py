"""
Task:
Create an abstract notification system.

Requirements:
- Create an abstract base class Notification.
- Notification must define an abstract method send().
- Create EmailNotification and SMSNotification classes.
- Each subclass must implement send().
- EmailNotification should store a recipient email.
- SMSNotification should store a phone number.
- send() should return a string describing the notification.
- Do not allow creating a Notification object directly.
"""

import re
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self) -> str:
        pass


class EmailNotification(Notification):
    def __init__(self, email: str):
        self.email = email.strip()

        if not re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$").match(
            self.email
        ):
            raise ValueError("Incorrect email format.")

    def send(self) -> str:
        return f"Sending email to {self.email}"


class SMSNotification(Notification):
    def __init__(self, phone: str):
        self.phone = re.sub(r"[\s\-\(\)]", "", phone)

        if not re.compile(r"^\+?[1-9]\d{1,14}$").match(self.phone):
            raise ValueError("Incorrect phone format.")

    def send(self) -> str:
        return f"Sending SMS to {self.phone}"
