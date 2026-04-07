from bank_account import BankAccount
from ENUM import AccountStatus, Currency
from exception import AccountFrozenError, InsufficientFundsError

def main():
    print("1 создание активного и замороженного счета")

    active_account = BankAccount("аыфрпыврыр", 10000, Currency.RUB)
    print(f"активный счет создан: {active_account}")

    frozen_account = BankAccount("еукправрвр", 5000, Currency.USD)
    frozen_account.status = AccountStatus.FROZEN
    print(f"замороженный счет создан: {frozen_account}")

    print("2 п1 операций над замороженным счетом")

    try:
        print("п2 пополнения замороженного счета")
        frozen_account.deposit(1000)
    except AccountFrozenError as e:
        print(f"ошибка: {e}")

    try:
        print("попытка снятия с замороженного")
        frozen_account.withdraw(500)
    except AccountFrozenError as e:
        print(f"ошибка: {e}")

    print("3 валидное пополнение и снятие")

    print(f"начальный баланс: {active_account.balance} {active_account._currency.value}")

    active_account.deposit(5252)
    print(f"после пополнения на 5252: {active_account.balance}")

    active_account.withdraw(3333)
    print(f"после снятия 3333: {active_account.balance}")

    try:
        print("п1 снять 20000")
        active_account.withdraw(20000)
    except InsufficientFundsError as e:
        print(f"ошибка: {e}")

    print("4 проверка")

    print(active_account)
    print(frozen_account)

    print("5 информация о счете")

    info = active_account.get_account_info()
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()