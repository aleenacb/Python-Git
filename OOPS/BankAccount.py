class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    def show_balance(self):
        print(self._balance)
account = BankAccount(50000)
account.show_balance()

#__balance is a private style attribute
#__init__() initializes the object's data
#show_balance() provudes a method to access the balance