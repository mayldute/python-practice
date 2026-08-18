"""
Task:
Create an abstract payment system.

Requirements:
- Create an abstract Payment class.
- Payment must define an abstract method pay().
- Create CardPayment and CashPayment subclasses.
- CardPayment should store the last 4 digits of the card.
- CashPayment should store the amount of cash received.
- pay() should return a string describing the payment.
- A payment amount must be greater than 0.
- Do not allow creating a Payment object directly.
- Use type hints.
"""

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self) -> str:
        pass


class CardPayment(Payment):
    def __init__(self, amount_due: float, card_number: str):
        if amount_due <= 0:
            raise ValueError("Amount due can not be less or equal 0. ")

        card_number = card_number.replace(" ", "").replace("-", "")

        if not card_number.isdigit() or not (15 <= len(card_number) <= 19):
            raise ValueError(
                "Wrong card number. Must contain only numbers and count of numbers from 15 to 19."
            )
        
        self.amount_due = amount_due
        self.last_four = card_number[-4:]

    def pay(self) -> str:
        return f"Paid {self.amount_due} using card ending in {self.last_four}"


class CashPayment(Payment):
    def __init__(self, amount_due: float, cash_received: float):
        if amount_due <= 0 or cash_received <= 0:
            raise ValueError(
                "Amount due and received cash must be greater than 0."
            )

        self.amount_due = amount_due
        self.cash_received = cash_received

    def pay(self) -> str:
        if self.cash_received < self.amount_due:
            raise ValueError(
                "Received cash cannot be less than amount due."
            )

        change = self.cash_received - self.amount_due

        return f"Paid {self.amount_due} in cash. Change: {change}"
