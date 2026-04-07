from enum import Enum

class AccountStatus(Enum):
    ACTIVE = "active"
    FROZEN = "frozen"
    CLOSED = "closed"

class Currency(Enum):
    RUB = "rub"
    USD = "usdt"
    EUR = "eur"
    KZT = "kzt"
    CNY = "cny"