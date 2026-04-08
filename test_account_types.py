from savings_account import SavingsAccount
from premium_account import PremiumAccount
from investment_account import InvestmentAccount
from ENUM import Currency, AccountStatus

def test_savings_account():
    print("тестирование SavingsAccount")
    savings = SavingsAccount("321321312", 50000, Currency.RUB, 10000, 5.0)
    print(f"создан: {savings}")
    print(f"месячная прибыль: {savings.calculate_monthly_profit()} RUB")
    
    try:
        print("\nпопытка снять 45000 (останется 5000, а min_balance=10000):")
        savings.withdraw(45000)
    except Exception as e:
        print(f"ошибка: {e}")
    
    print("\nснятие 30000 (останется 20000):")
    savings.withdraw(30000)
    print(f"после снятия: {savings.balance}")
    
    info = savings.get_account_info()
    print(f"\nинформация о счете: {info}")

def test_premium_account():
    print("\nтестирование PremiumAccount")
    premium = PremiumAccount("321312321312", 1000, Currency.USD, 5000, 100)
    print(f"создан: {premium}")
    
    print("\nснятие 3000:")
    premium.withdraw(3000)
    print(f"баланс после снятия: {premium.balance}")
    
    try:
        print("\nснять 4000:")
        premium.withdraw(4000)
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\nсписание комиссии 100:")
    premium.apply_monthly_fee()
    print(f"баланс после комиссии: {premium.balance}")

def test_investment_account():
    print("\nтестирование InvestmentAccount")
    portfolio = {"stocks": 100000, "bonds": 50000, "etf": 25000}
    investment = InvestmentAccount("413413231", 50000, Currency.RUB, portfolio)
    print(f"создан: {investment}")
    
    growth_rates = {"stocks": 12.0, "bonds": 5.0, "etf": 8.0}
    yearly_growth = investment.project_yearly_growth(growth_rates)
    print(f"\nпрогнозируемый годовой доход: {yearly_growth} RUB")
    
    info = investment.get_account_info()
    print(f"\nинформация о счете: {info}")

if __name__ == "__main__":
    test_savings_account()
    test_premium_account()
    test_investment_account()