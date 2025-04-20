# Create a BankAccount class.
# Define a private attribute __balance to store the account balance.
# Provide a getter method get_balance() to access the current balance.
# Create a setter method set_balance(new_balance) to update the balance, with validation to ensure the balance cannot be negative.
# Implement a deposit(amount) method to add funds to the account, ensuring the deposit amount is positive.
# Implement a withdraw(amount) method to subtract funds from the account, ensuring the withdrawal amount is positive and there are sufficient funds.
# Create a transfer(amount, target_account) method to transfer funds between two accounts, ensuring there are sufficient funds in the source account.
# Finally, demonstrate the functionality by creating two BankAccount instances, performing deposits, withdrawals, and transfers, and printing their balances.

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.__balance = initial_balance
        self.owner = owner

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if new_balance < 0:
            print('Error: Balance cannot be negative.')
        else:
            self.__balance = new_balance
            print(f'Balance updated to {self.__balance} TL.')

    def deposit(self, amount):
        if amount >0:
            self.__balance += amount
            print(f'{amount} TL deposited into {self.owner}s account.')
        else:
            print('Error: Deposit amount must be positive.')

    def withdraw(self, amount):
        if amount <= 0:
            print('Error: Withdrawal amount must be positive.')
        elif amount > self.__balance:
            print('Error: Insufficient funds.'),
        else:
            self.__balance -= amount
            print(f'{amount} TL withdrawn from {self.owner}\'s account. ')

    def transfer(self, amount, target_account):
        if amount <= 0:
            print('Error: Transfer amount must be positive.')
        elif amount > self.__balance:
            print('Error: Insufficient funds for transfer.')
        else:
            self.__balance -= amount
            target_account.deposit(amount)
            print(f'{amount} TL transferred from {self.owner} to {target_account.owner}.')

account1 = BankAccount('Hilal', 1500)
account2 = BankAccount('Ali', 2000)

account1.deposit(500)
account1.withdraw(300)
account1.set_balance(2500)
account1.transfer(600, account2)

print(f'{account1.owner}s Final Balance: {account1.get_balance()}TL.')
print(f'{account2.owner}s Final Balance: {account2.get_balance()} TL.')
    