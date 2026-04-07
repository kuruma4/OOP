from abc import ABC, abstractmethod
from ENUM import AccountStatus
import uuid

class AbstractAccount(ABC):
    def __init__(self, owner, balance):
        self._account_id = str(uuid.uuid4())[-4:] #zfill 
        self.owner = owner
        self._balance = balance
        self._status = AccountStatus.ACTIVE
    
    @property
    def account_id(self):
        return self._account_id
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, new_status):
        if not isinstance(new_status, AccountStatus):
            raise ValueError("ошибка статуса")
        self._status = new_status
    
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def get_account_info(self):
        pass
    
    def __str__(self):
        last_numbers = self._account_id[-4:] if len(self._account_id) >= 4 else self._account_id
        return f"Client: {self.owner}  ID: {last_numbers}  Status: {self._status.value}"