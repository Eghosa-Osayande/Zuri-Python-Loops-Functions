from datetime import datetime
import random, dill, os


user_database = []

if os.path.exists("database.pkl"):
    with open("database.pkl", "rb") as fd:
        user_database = dill.load(fd)
else:
    with open("database.pkl", "wb") as fd:
        dill.dump(user_database, fd)

def save_to_database(database):
    with open("database.pkl", "wb") as fd:
        dill.dump(database, fd)
    return database

class User():

    def __init__(self, account_number, first_name, last_name, email, password, account_balance):
        self.account_number= account_number
        self.first_name= first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.account_balance = account_balance

def init():
    print('\n\nWELCOME TO ZURI BANK LTD\nWhat do you want to do\n1. Login\n2.New User? Register here')
    actions = { 1: login, 2: register }

    has_account = input("Enter option --->")
    _has_account = None

    if has_account.isnumeric():
        _has_account = int(has_account)
    if _has_account in actions.keys():
        actions.get(_has_account)()
    else:
        print("\nYou have selected an invalid option")
        init()
    
def login():
    print("LOGIN")
    _account_number_from_user = input("What is your account number? ---> ")
    account_number_from_user = None
    password = input("What is your password --->")

    if _account_number_from_user.isnumeric():
        account_number_from_user = int(_account_number_from_user )
    else:
        print("Invalid Amount")
        return

    for user in user_database:
        if account_number_from_user == user.account_number and password == user.password:
            bank_operation(user)
            return

    print('Invalid account or password')
    login()
    
def logout(*args):
    print("Logged Out")
    login()

def register():
    print('Register')
    email = input("What is your email address?\n")
    first_name =input("What is your first name?\n")
    last_name =input("What is your last name?\n")
    password =input("create a password for yourself\n")
    account_balance = 0

    account_number = generate_account_number()
    
    user_database.append(User(account_number, first_name, last_name, email, password, account_balance))
    save_to_database(user_database)

    print("Your Account has been created")
    print(f"Your Account number is {account_number}")
 
    login()

def bank_operation(user):
    print(datetime.now().ctime())
    print(f"Welcome {user.first_name} {user.last_name}")
    operations = { 1: deposit_operation, 2: withdrawal_operation, 3: complaint, 4: logout, 5: exit }
    selected_option = input("What would you like to do? 1. Cash Deposit  2. Withdrawal  3.Complaint  4.Logout 5.exit \n--->")
    _selected_option = None

    if selected_option.isnumeric():
        _selected_option = int(selected_option)
    if _selected_option in operations.keys():
        operations.get(_selected_option)(user)
    else:
        print("Invalid option selected")
    bank_operation(user)
    
def withdrawal_operation(user):
    _amount= input('How much would you like to withdraw? \n')
    amount = None
    if _amount.isnumeric():
        amount = int(_amount)
    else:
        print("Invalid Amount")
        return
        
    account_balance = user.account_balance
    if amount > account_balance:
        print('Insufficient Balance\n')
    else:
        user.account_balance -= amount
        print(f"take your cash ${amount}\n")

def deposit_operation(user):
    print("Deposit Operation")
    _amount = input('How much would you like to deposit? \n')
    amount = None
    
    if _amount.isnumeric():
        amount = int(_amount)
    else:
        print("Invalid Amount")
        return
    user.account_balance += amount
    print(f'Current Balance: ${user.account_balance}')

def complaint(*args):
    input('What issue will you like to report? \n')
    print("Thank you for contacting us \n") 

def generate_account_number():

    print("Generating Account Number")
    account_numbers = [user.account_number for user in user_database ]
    while True:
        account_number = random.randrange(1111111111,9999999999)
        if account_number not in account_numbers:
            break
    return account_number

init()
     





