class Bank:

    Account_number = 100

    def __init__(self,Account_name, Balance, Branch):

        Bank.Account_number += 1
        
        self.Account_name = Account_name
        self.Account_number = Bank.Account_number
        self.Balance = Balance
        self.Branch = Branch


    
    def Deposit(self, Amount):

        if Amount > 0:
            print(f"You successfully Deposited ₱: {Amount} Current Balance: {self.Balance} ")

            self.Balance += Amount
    

    def Withdraw(self, Amount):

        if Amount <= self.Balance:
            print(f"You Withdraw ₱: {Amount}")
        
            self.Balance -= Amount

    def display(self):
        
            print("----------------------BANK---------------------------")
            print(f"Account name : {self.Account_name}")
            print(f"Account number: {self.Account_number}")
            print(f"Branch: {self.Branch}")
            print(f"Balance: {self.Balance}")
            print("-------------------------------------------------------")


accounts = {}

# User can create accounts
def create_accounts():
        
    Account_name = input("Enter a name: ")
    Branch = input("Enter your chosen branch: ")

    


    while True:
        try:
            Balance = int(input("Inital Deposit: "))
                
            if Balance < 0:
                print("Not negative numbers")
                continue
            
            
            break
            
        except ValueError:   
            print("Real numbers only")

    account = Bank(Account_name, Balance, Branch)
    accounts[account.Account_number] = account

    print("You successfully created your account!!!")
    print(f"Your Account number: {account.Account_number}")


#User can deposit 
def deposit():

        Account_number = int(input("Enter a Account number:  "))

        if Account_number not in accounts:
            print("Account not found")
            return
        

        while True:
            try:
                Amount = int(input("Enter a Amount: "))
                break
            
            except ValueError:
                print("REAL NUMBERS ONLYYY")
            

        accounts[Account_number].Deposit(Amount)


# User can withdraw
def withdraw():

        Account_number = int(input("Enter a Account number: "))

        if Account_number not in accounts:
            print("Account not found")
            return
        
        Amount = int(input("Enter a Amount: "))
        
        accounts[Account_number].Withdraw(Amount)


# User can view account
def view_account():
        
    Account_number = int(input("Enter a Account number: "))

    if Account_number not in accounts:
        print("No Account found")
        return


    accounts[Account_number].display()


#User can view all account
def view_all():
     
    if len(accounts) == 0:
        print("-------------------------NO ACCOUNTS TO BE SHOWED------------------------------")
    for account in accounts.values():
        account.display()


# Choices

    while True:
        print("""
=============================
BANK MANAGEMENT SYSTEM
=============================

1. Create Account
2. Deposit
3. Withdraw
4. View Account
5. View All Accounts
6. Exit
""")

        try:
            choices = int(input("Enter a number: "))
        except ValueError:
            print("NUMBERS ONLY")
            continue

        if choices == 1:
            create_accounts()
        elif choices == 2:
            deposit()
        elif choices == 3:
            withdraw()
        elif choices == 4:
            view_account()
        elif choices == 5:
            view_all()
        elif choices == 6:
            break
        else:
            print("Invalid Choice")



                




        
