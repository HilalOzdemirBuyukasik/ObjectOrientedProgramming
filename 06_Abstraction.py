# Create an abstract class AbstractAccount using the abc module.
# Define the following abstract methods:
# - get_balance()
# - set_balance(new_balance)
# - deposit(amount)
# - withdraw(amount)
# - transfer(amount, target_account)

# Create a BankAccount class that inherits from AbstractAccount.

# Define a private attribute __balance to store the account balance.

# Provide a getter method get_balance() to access the current balance.

# Create a setter method set_balance(new_balance) to update the balance,
# with validation to ensure the balance cannot be negative.

# Implement a deposit(amount) method to add funds to the account,
# ensuring the deposit amount is positive.

# Implement a withdraw(amount) method to subtract funds from the account,
# ensuring the withdrawal amount is positive and there are sufficient funds.

# Create a transfer(amount, target_account) method to transfer funds
# between two accounts, ensuring there are sufficient funds in the source account.

# Finally, demonstrate the functionality by creating two BankAccount instances,
# performing deposits, withdrawals, and transfers, and printing their balances.

from abc import ABC, abstractmethod

class AbstractAccount(ABC):
    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def set_balance(self, new_balance):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def transfer(self, amount, target_account):
        pass


class BankAccount(AbstractAccount):
    def __init__(self, initial_balance=0.0):
        self.initial_balance = initial_balance
        self.set_balance(initial_balance)

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if new_balance < 0:
            raise ValueError('Balance cannot be negative.')
        self.__balance = new_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive.')
        self.__balance += amount
        print(f'Deposit ${amount: .2f}')

    def withdraw(self, amount):
        if amount <=0:
            raise ValueError('Withdrawal amount must be positive.')
        if amount > self.__balance:
            raise  ValueError('Insufficient funds.')
        self.__balance -= amount
        print(f'Withdrew ${amount:.2f}')

    def transfer(self, amount, target_account):
        if amount <=0:
            raise ValueError('Transfer amount must be positive.')
        if amount > self.__balance:
            raise ValueError('Insufficient funds for transfer')
        self.withdraw(amount)
        target_account.deposit(amount)
        print(f'Transferred ${amount:.2f} to target account.')

if __name__ =='__main__':
    account1 = BankAccount(1000)
    account2 = BankAccount(500)

    print('Initial Balances:')
    print(f'Account 1: ${account1.get_balance():.2f}')
    print(f'Account 2: ${account2.get_balance():.2f}')

    print('\nPerforming operations...')
    account1.deposit(300)
    account1.withdraw(200)
    account1.transfer(250, account2)

    print('\nFinal Balances:')
    print(f'Account 1: ${account1.get_balance():.2f}')
    print(f'Account 2: ${account2.get_balance():.2f}')
        