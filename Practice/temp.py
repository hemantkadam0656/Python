# class BankAccount:
#     def __init__(self, account_number, account_holder):
#         self.account_number = account_number           # Public attribute
#         self.account_holder = account_holder           # Public attribute
#         self.__balance = 0.0                           # Private attribute
#         self.__transaction_history = []                # Private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             self.__add_transaction("Deposit", amount)
#         else:
#             print("Invalid deposit amount")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             self.__add_transaction("Withdrawal", amount)
#         else:
#             print("Invalid withdrawal amount or insufficient funds")

#     def get_balance(self):
#         return self.__balance

#     def get_transaction_history(self):
#         return self.__transaction_history

#     def __add_transaction(self, transaction_type, amount):
#         """Private method to log a transaction"""
#         transaction = {
#             'type': transaction_type,
#             'amount': amount,
#             'balance': self.__balance
#         }
#         self.__transaction_history.append(transaction)

# # Example usage of the BankAccount class
# account = BankAccount("123456789", "John Doe")

# # Deposit money
# account.deposit(500)
# print(f"Balance after deposit: ${account.get_balance()}")

# # Withdraw money
# account.withdraw(200)
# print(f"Balance after withdrawal: ${account.get_balance()}")

# # Attempting to directly access private attributes (will raise an AttributeError)
# try:
#     print(account.__balance)
# except AttributeError:
#     print("Cannot access private attribute __balance directly!")

# # Accessing transaction history through a public method
# print("Transaction History:", account.get_transaction_history())
# print(account.get_transaction_history())




class Animal:
    def eat(self):
        return "Eating"

class Mammal(Animal):
    def walk(self):
        return "Walking"

class Bird(Animal):
    def fly(self):
        return "Flying"

class Bat(Mammal, Bird):
    def sound(self):
        return "Screeching"

# Usage
bat = Bat()
print(bat.eat())  # In
