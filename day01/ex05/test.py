from the_bank import Bank, Account

# TEST Normal Account
print("\n-----Test Good Account----\n")
Musk = Account("Elon Musk", value=1000, zipcode="USA", other="Tesla")
Gates = Account("Bill Gates", value=100, zipcode="China", other="Ford")
bank = Bank()
print(Musk.__dict__)
print(Gates.__dict__)

bank.add(Musk)
bank.add(Gates)

# Test Corrupted Account
print("\n-----Test Corrupted Account----\n")
broken = Account("Broke",  zipcode="USA")
print(broken.__dict__)
bank.add(broken)
bank.fix_account(broken)
bank.add(broken)
print(broken.__dict__)
