from bank_account import BankAccount
from exception import InvalidOperationError

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, currency, min_balance, monthly_interest_rate):
        super().__init__(owner, balance, currency)
        self.min_balance = min_balance
        self.monthly_interest_rate = monthly_interest_rate
    
    def calculate_monthly_profit(self):
        profit = self._balance * (self.monthly_interest_rate / 100)
        return profit
    
    def withdraw(self, amount):

        self._validate_amount(amount)
        self._validate_status()
        
        if self._balance - amount < self.min_balance:
            raise InvalidOperationError(
                f"нельзя снять {amount}. мин остаток должен быть {self.min_balance}"
            )
        
        if amount > self._balance:
            from exception import InsufficientFundsError
            raise InsufficientFundsError(f"нельзя доступно: {self._balance}")
        
        self._balance -= amount
        return self._balance
    
    def get_account_info(self):
        info = super().get_account_info()
        info.update({
            "account_type": "SavingsAccount",
            "min_balance": self.min_balance,
            "monthly_interest_rate": self.monthly_interest_rate,
            "monthly_profit": self.calculate_monthly_profit()
        })
        return info
    
    def __str__(self):
        last_four = self._account_id[-4:] if len(self._account_id) >= 4 else self._account_id
        return (f"SavingsAccount Client: {self.owner} ID: {last_four}"
                f"Status: {self._status.value} Balance: {self._balance} {self._currency.value} "
                f"Min balance: {self.min_balance} Rate: {self.monthly_interest_rate}%")