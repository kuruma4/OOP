from bank_account import BankAccount
from exception import InvalidOperationError

class PremiumAccount(BankAccount):
    def __init__(self, owner, balance, currency, overdraft_limit, fixed_fee):
        super().__init__(owner, balance, currency)
        self.overdraft_limit = overdraft_limit
        self.fixed_fee = fixed_fee
    
    def withdraw(self, amount):
        self._validate_amount(amount)
        self._validate_status()
        
        if self._balance - amount < -self.overdraft_limit:
            raise InvalidOperationError(
                f"превышен овердрф лимит: {self.overdraft_limit}, "
                f"попытка уйти на {abs(self._balance - amount)}"
            )
        
        self._balance -= amount
        return self._balance
    
    def apply_monthly_fee(self):
        if self._balance - self.fixed_fee < -self.overdraft_limit:
            raise InvalidOperationError("недостаточно для списание комки")
        self._balance -= self.fixed_fee
        return self._balance
    
    def get_account_info(self):
        info = super().get_account_info()
        info.update({
            "account_type": "PremiumAccount",
            "overdraft_limit": self.overdraft_limit,
            "fixed_fee": self.fixed_fee
        })
        return info
    
    def __str__(self):
        last_four = self._account_id[-4:] if len(self._account_id) >= 4 else self._account_id
        return (f"PremiumAccount  Client: {self.owner}  ID: {last_four}  "
                f"Status: {self._status.value}  Balance: {self._balance} {self._currency.value}  "
                f"Overdraft: {self.overdraft_limit}  Fee: {self.fixed_fee}")