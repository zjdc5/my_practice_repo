from bank_account import BankAccount

account1 = BankAccount("1234", 1000)
print(account1)

account1.withdraw(500)
print(account1.get_balance())

account1.deposit(300)
print(account1.get_balance())

account2 = BankAccount("5678")
