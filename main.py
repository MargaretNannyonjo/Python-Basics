#!/usr/bin/python3
class BankAccount:
    def __init__(self, accNum, accName, accBal):
        self.accNum = accNum
        self.accName = accName
        self.accBal = int(accBal)
my_bankAccount = BankAccount("012202020", "Maggie", 202000)
print("Account Number:", my_bankAccount.accNum)
print("Account Name:", my_bankAccount.accName)
print("Account Balance:", my_bankAccount.accBal)


action = input("Do you want to deposit or withdraw money? ")
if action.lower() == "deposit":
    method = input("What method would you like to use?\n Paypal\n Easy Deposit\n Credit card")
    amount = int(input("Enter Amount: "))
    my_bankAccount.accBal += amount
    print(f"You have deposited {amount} and you have {my_bankAccount.accBal} balance")
elif action.lower() == "withdraw":
    method = input("What method would you like to use?\n Paypal\n Easy Withdraw\n Credit card\n : ")
    amount = int(input("Enter Amount: "))
    if amount <= my_bankAccount.accBal:
        my_bankAccount.accBal -= amount
        print(f"You have withdrawn {amount} and you have {my_bankAccount.accBal} balance")
    else:
        print("Insufficient funds")
else:
    exit()
print("Thank you for using Main Bank")
