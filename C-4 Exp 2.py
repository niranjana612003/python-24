print("Name : Niranjana S Nair")
print("Admission No: A24MCA047")
print("Experiment No: 2")

class Bank:
    def __init__(self, acc_name="", acc_no="", acc_balance=0):
        self.__acc_name = acc_name
        self.__acc_no = acc_no
        self.__acc_balance = acc_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        print(f"Initial balance is: {self.__acc_balance}")
        print(f"Deposit is: {amount}")
        self.__acc_balance += amount
        print(f"Current balance is: {self.__acc_balance}")

    def withdraw(self):
        print(f"Current balance is: {self.__acc_balance}")
        try:
            amt = int(input("How much amount do you want to withdraw: "))
            if amt <= 0:
                print("Withdrawal amount must be positive!")
                return
            if amt > self.__acc_balance:
                print("Insufficient balance!")
                print(f"Current balance is: {self.__acc_balance}")
            else:
                print(f"{amt} is withdrawn.")
                self.__acc_balance -= amt
                print(f"Current balance is: {self.__acc_balance}")
        except ValueError:
            print("Enter a valid integer amount!")

    def acc_info(self):
        print("\n---- Account Details ----")
        print(f"Account holder name: {self.__acc_name}")
        print(f"Account number: {self.__acc_no}")
        print(f"Account Balance: {self.__acc_balance}")


def fetch_balance():
    while True:
        try:
            b = int(input("Enter Account initial balance: "))
            if b < 0:
                print("Initial balance cannot be negative!")
                continue
            return b
        except ValueError:
            print("Enter a valid amount!")

def fetch_deposit_amount():
    while True:
        try:
            d = int(input("Deposit amount: "))
            if d <= 0:
                print("Deposit amount must be positive!")
                continue
            return d
        except ValueError:
            print("Enter a valid amount!")

print("Aim: Create a BankAccount class for deposits and withdrawals.\nDate: 25-11-2024\n")

name = input("Enter Account holder name: ")
a_no = input("Enter Account number: ")
bal = fetch_balance()
holder = Bank(name, a_no,bal)
while True:
    opt = input("\n1) Deposit \n2) Withdraw \n3) Account info \n0) Exit\nChoose your option: ")
    if opt == "1":
        amount = fetch_deposit_amount()
        holder.deposit(amount)
    elif opt == "2":
        holder.withdraw()
    elif opt == "3":
        holder.acc_info()
    elif opt == "0":
        print("Exiting the banking system.")
        break
    else:
        print("Invalid Option!")