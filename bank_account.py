from abstract import AbstractAccount
from ENUM import AccountStatus, Currency
from exception import AccountFrozenError, AccountClosedError, InvalidOperationError, InsufficientFundsError

class BankAccount(AbstractAccount):
    def __init__(self, owner, balance, currency):
        super().__init__(owner, balance)
        
        if not isinstance(currency, Currency):
            raise ValueError("валюта должна быть другим типом")
        self._currency = currency
    
    def _validate_amount(self, amount):
        if not isinstance(amount, (int, float)):
            raise InvalidOperationError("сумм должн быть числом")
        if amount <= 0:
            raise InvalidOperationError("сумм должн быть положительной")
        return True
    
    def _validate_status(self):
        if self._status == AccountStatus.FROZEN:
            raise AccountFrozenError(f"Счет {self._account_id} заморожен")
        if self._status == AccountStatus.CLOSED:
            raise AccountClosedError(f"Счет {self._account_id} закрыт")
        return True
    
    def deposit(self, amount):
        self._validate_amount(amount)
        self._validate_status()
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount):
        self._validate_amount(amount)
        self._validate_status()
        
        if amount > self._balance:
            raise InsufficientFundsError(f"недостаточно средств доступно: {self._balance}")
        
        self._balance -= amount
        return self._balance
    
    def get_account_info(self):
        return {
            "account_id": self._account_id,
            "owner": self.owner,
            "balance": self._balance,
            "status": self._status.value,
            "currency": self._currency.value
        }
    
    def __str__(self):
        last_four = self._account_id[-4:] if len(self._account_id) >= 4 else self._account_id
        return (f"{self.__class__.__name__}"
                f"Client: {self.owner}"
                f"ID: {last_four}"
                f"Status: {self._status.value}"
                f"Balance: {self._balance} {self._currency.value}")