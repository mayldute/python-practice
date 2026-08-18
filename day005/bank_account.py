"""
Task:
Create a BankAccount class that manages a customer's bank balance.

Requirements:
- Store the account owner's name.
- Store the balance internally.
- Allow money to be deposited.
- Allow money to be withdrawn.
- Do not allow withdrawing more money than the current balance.
- Do not allow depositing or withdrawing a negative amount.
- Expose the balance through a read-only property.
- Raise ValueError for invalid operations.
"""

class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner

        if balance < 0:
            raise ValueError("Balance can not be less than 0.")
        
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount can not be less or equal 0.")

        self._balance += amount 

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount can not be less or equal 0.")

        if self._balance - amount < 0:
            raise ValueError("Balance can not be less than 0.")

        self._balance -= amount

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(owner={self.owner}, balance={self.balance})"
