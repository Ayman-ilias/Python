from random import randint

class Bank:
    def __init__(self):
        self.users = []
        self.admins = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_user_account(self, name, email, address, account_type):
        account_number = randint(10000000, 99999999)
        user = User(name, email, address, account_number, account_type)
        self.users.append(user)

    def delete_user_account(self, user):
        if user in self.users:
            self.users.remove(user)

    def get_all_user_accounts(self):
        return self.users

    def get_total_available_balance(self):
        return self.total_balance

    def get_total_loan_amount(self):
        return self.total_loan_amount

    def enable_loan_feature(self):
        self.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.loan_feature_enabled = False


class User:
    def __init__(self, name, email, address, account_number, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0
        self.transaction_history = []
    
    def deposit(self, amount):
         if amount > 0:
            self.balance += amount
            Bank.total_balance += amount
            transaction_info = f"Deposited ${amount}. New balance: ${self.balance}"
            print(transaction_info)
            self.transaction_history.append(transaction_info)
         else:
             print("Invalid deposit amount")

    def withdraw(self, amount):
         if amount > 0 and amount <= self.balance:
            self.balance -= amount
            Bank.total_balance -= amount
            transaction_info = f"Withdrew ${amount}. New balance: ${self.balance}"
            print(transaction_info)
            self.transaction_history.append(transaction_info)
         else:
             print("Invalid withdrawal amount or insufficient balance")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if Bank.loan_feature_enabled and len(self.transaction_history) < 2:
            self.balance += amount
            Bank.total_balance += amount
            Bank.total_loan_amount += amount
            transaction_info = f"Took a loan of ${amount}. New balance: ${self.balance}"
            print(transaction_info)
            self.transaction_history.append(transaction_info)
        elif not Bank.loan_feature_enabled:
            print("Loan feature is currently disabled")
        else:
            print("You have already taken the maximum number of loans")

    def transfer_amount(self, recipient_account_number, amount):
        recipient = None
        for user in bank.users:
            if user.account_number == recipient_account_number:
                recipient = user
                break
        
        if recipient is None:
            print("Account does not exist")
        elif amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient.deposit(amount)
            
    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nAccount Number: {self.account_number}\nAccount Type: {self.account_type}"


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def create_user_account(self, bank, name, email, address, account_type):
        bank.create_user_account(name, email, address, account_type)

    def delete_user_account(self, bank, user):
        bank.delete_user_account(user)

    def get_all_user_accounts(self, bank):
        return bank.get_all_user_accounts()

    def check_total_available_balance(self, bank):
        return bank.get_total_available_balance()

    def check_total_loan_amount(self, bank):
        return bank.get_total_loan_amount()

    def enable_loan_feature(self, bank):
        bank.enable_loan_feature()

    def disable_loan_feature(self, bank):
        bank.disable_loan_feature()