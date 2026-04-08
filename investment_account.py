from bank_account import BankAccount

class InvestmentAccount(BankAccount):
    def __init__(self, owner, balance, currency, portfolio):
        super().__init__(owner, balance, currency)
        self.portfolio = portfolio
        self.virtual_assets = portfolio
    
    def project_yearly_growth(self, growth_rates):
        total_growth = 0
        for asset_type, amount in self.portfolio.items():
            if asset_type in growth_rates:
                growth = amount * (growth_rates[asset_type] / 100)
                total_growth += growth
        return total_growth
    
    def withdraw(self, amount):
        return super().withdraw(amount)
    
    def get_account_info(self):
        info = super().get_account_info()
        info.update({
            "account_type": "InvestmentAccount",
            "portfolio": self.portfolio,
            "total_invested": sum(self.portfolio.values())
        })
        return info
    
    def __str__(self):
        last_four = self._account_id[-4:] if len(self._account_id) >= 4 else self._account_id
        total_invested = sum(self.portfolio.values())
        return (f"InvestmentAccount Client: {self.owner} ID: {last_four} "
                f"Status: {self._status.value} Balance: {self._balance} {self._currency.value} "
                f"Invested: {total_invested}")