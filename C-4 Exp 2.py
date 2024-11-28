print("Name : Niranjana S Nair")
print("Admission No: A24MCA047")
print("Experiment No: 2")

class BAccount:
    def __init__(self, accno, accname, acctype):
        self.accno = accno
        self.accname = accname
        self.acctype = acctype
        self.balance = 0.0

    def deposit(self,amt):
        self.balance=self.balance+amt
        print(f"Rs.{amt} is credited to your bank account!")

    def withdraw(self,amt):
        if self.balance < amt:
            print("Insufficient Balance!")
        else:
            self.balance=self.balance-amt
            print(f"Rs.{amt} is debited from your bank account!")

    def showBalance(self):
        print(f"Your balance is : Rs.{self.balance}")

print("Bank Operations")
accname=input("Enter your name : ")
accno=int(input("Enter account number : "))
acctype=input("Enter account type : ")
user=BAccount(accno,accname,acctype)

while 1:
    print("Select an Operation ")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Balance")
    print("4.Exit")
    c=int(input("Enter your choice : "))

    if c == 1:
        amt=int(input("Enter the amount to be deposited : "))
        user.deposit(amt)
    elif c == 2:
        amt=int(input("Enter the amount to be Withdraw : "))
        user.withdraw(amt)
    elif c == 3:
        user.showBalance()
    elif c == 4:
        exit(0)
    else:
        print("Invalid choice!!")