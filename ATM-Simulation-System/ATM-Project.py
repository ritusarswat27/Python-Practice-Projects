from getpass import getpass
class Atm:
    def __init__(self):
        self.__pin = ""
        self.__bankBalance = 0
        self.transactions = []
    
    def generatePin(self):
        self.__pin = getpass("Enter Pin: ")
        print("Successfully!! You have created Pin")
    
    def addTransaction(self, message):
        self.transactions.append(message)

    def deposit(self):
        if not self.__pin:
            print("First Generate Pin then deposit!")
            self.generatePin()
            print("Now you can deposit amount")
        temp = getpass("Enter Pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount to deposit: "))
            self.__bankBalance = self.__bankBalance + amount
            print(f"You have succesfully deposit ₹{amount} in you account")
            self.addTransaction(f"Deposit ₹{amount}")
        else:
            print("Invalid Pin")

    def withdraw(self):
        if not self.__pin:
            print("First Generate Pin then deposit!")
            self.generatePin()
            print("Now you can withdraw amount")
        temp = getpass("Enter Pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount to withdraw: "))
            if amount > 10000:
                print("You reached the withdrawal limit. Please withdraw less than ₹10,000")
                return
            if self.__bankBalance - amount > 3000:
                    self.__bankBalance = self.__bankBalance - amount
                    print(f"You have succesfully withdraw ₹{amount} from your account")
                    self.addTransaction(f"Withdrawn ₹{amount}")
            else: print("Insufficient bank balance. Maintain ₹3000 minimum balance.")
        else:
            print("Invalid Pin")

    def checkBalance(self):
        if not self.__pin:
            print("First Generate Pin then deposit!")
            self.generatePin()
            print("Now you can check bank balance")
        temp = getpass("Enter Pin: ")
        if temp == self.__pin:
            print(f"Bank Balance: {self.__bankBalance}")
        else: print("Invalid Pin")
    
    def showTransactionHistory(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for t in self.transactions:
                print("-", t)

    def changePin(self):
        old = getpass("Enter old PIN: ")
        if old == self.__pin:
           self.__pin = input("Enter new PIN: ")
           print("PIN successfully changed")
        else:
           print("Incorrect old PIN")



   

accounts = {}  

while True:

    acc_no = input("Enter your account number: ")
    if acc_no not in accounts:
       print("New user detected, creating account...")
       accounts[acc_no] = Atm()
    user = accounts[acc_no]
    print("\n===Option for User===")
    print("Enter 1 to Generate Pin: ")
    print("Enter 2 to deposit amount: ")
    print("Enter 3 to withdraw amount: ")
    print("Enter 4 to check bank balance: ")
    print("Enter 5 to show transaction history: ")
    print("Enter 6 to change Pin: ")

    print("Enter 7 to Exit: ")

    choice = int(input("Enter your Choice:"))
    if choice == 1:
       user.generatePin()
    if choice == 2:
       user.deposit()
    if choice == 3:
       user.withdraw() 
    if choice == 4:
       user.checkBalance() 
    if choice == 5:
        user.showTransactionHistory()
    if choice == 6:
        user.changePin()
    if choice == 7:
       print("Thank you! Visit Again...")
       break