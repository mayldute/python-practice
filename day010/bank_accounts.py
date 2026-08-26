"""
Task:
Implement a simple banking system using object-oriented programming.

Requirements:
- Create a `BankAccount` class.
- Create a `Bank` class.
- A BankAccount has an account number, owner, and balance.
- Account number and owner cannot be empty.
- Initial balance cannot be negative.
- `deposit()` adds money to the account.
- `withdraw()` removes money from the account.
- Deposit and withdrawal amounts must be greater than 0.
- An account cannot withdraw more than its current balance.
- Bank stores multiple BankAccount objects.
- `add_account()` adds an account.
- Duplicate account numbers must raise `ValueError`.
- `find_account()` finds an account by account number.
- `transfer()` moves money between two existing accounts.
- Sender and receiver must be different accounts.
- Transfer amount must be greater than 0.
- Sender must have sufficient funds.
- Invalid transfers must raise `ValueError`.
- `richest_account()` returns the account with the highest balance.
- If there are no accounts, return `None`.
- If multiple accounts have the same balance, return the first one.

Algorithm:
- Search for accounts by account number.
- Validate a transfer before modifying balances.
- Use the account methods to perform the actual money movement.
- Find the richest account by comparing balances.
"""


class BankAccount:
    def __init__(self, account_number: str, owner: str, balance: float) -> None:
        if not account_number:
            raise ValueError("Account number can not be empty.")

        if not owner:
            raise ValueError("Owner can not be empty.")

        if balance < 0:
            raise ValueError("Balance can not be negative.")

        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        if self.balance < amount:
            raise ValueError("You cannot withdraw more than the current balance.")

        self.balance -= amount


class Bank:
    def __init__(self) -> None:
        self.accounts: list[BankAccount] = []

    def add_account(self, account: BankAccount) -> None:
        for existing_account in self.accounts:
            if existing_account.account_number == account.account_number:
                raise ValueError("Account already exist in bank system.")

        self.accounts.append(account)

    def find_account(self, account_number: str) -> BankAccount | None:
        for account in self.accounts:
            if account.account_number == account_number:
                return account

        return None

    def transfer(self, sender_number: str, receiver_number: str, amount: float) -> None:
        sender_account = self.find_account(sender_number)
        receiver_account = self.find_account(receiver_number)

        if sender_account is None or receiver_account is None:
            raise ValueError("Both accounts must exist.")

        if sender_account is receiver_account:
            raise ValueError("Sender and receiver must be different accounts.")

        sender_account.withdraw(amount)
        receiver_account.deposit(amount)

    def richest_account(self) -> BankAccount | None:
        if not self.accounts:
            return None

        return max(self.accounts, key=lambda account: account.balance)
