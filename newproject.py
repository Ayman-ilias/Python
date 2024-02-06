import random
class Admin:
    def __init__(self):
        self.users_list = []
        self.allow_loan = True
    def create_account(self, name, email_address, account_type):
        user = User(name, email_address, account_type)
        self.users_list.append(user)
        print(f"Account created successfully.\n Account number: {user.account_number}")

    def delete_account(self, account_number):
        for user in self.users_list:
            if user.account_number == account_number:
                self.users_list.remove(user)
                print(f"Account Removed successfully.\n Account number{user.account_number}")
                break
            else:
                print("Account not found.")

    def see_all_accounts(self):
        for user in self.users_list:
            print(f"1. Name: {user.name}, Email: {user.email_address}, Account Number: {user.account_number} , Account Type: {user.account_type}")

    def check_total_balance(self):
        tb=0
        for user in self.users_list:
            tb += user.balance
        total_balance = tb
        print(f"Total available balance of the bank: {total_balance} Tk.")
        

    def check_total_loan_amount(self):
        tl=0
        for user in self.users_list:
            tl += user.loan_taken
        total_loan_amount = tl
        print(f"Total loan amount of the bank: {total_loan_amount} Tk.")
        # print(f"Total loan amount of the bank: {tl}")

    def on_off_loan_features(self, action):
        self.allow_loan = action
        # User.a=action
        if action:
            print("Loan feature enabled.")
        else:
            print("Loan feature disabled.")
class User(Admin):
    def __init__(self, name, email_address, account_type):
        self.name = name
        self.email_address = email_address
        # self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = random.randint(1000, 9999)
        self.transaction_history = []
        self.loan_taken = 0
        self.loan_count = 0
        # self.allow_loan = None
    
    # def create_accountt(self, name, email_address, account_type):
    #     # user = User(name, email_address, account_type)
    #     self.users_list.append(user)
    #     print(f"Account created successfully.\n Account number: {user.account_number}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited amount: {amount} Tk.")
            print(f"Congratulations...{amount} Tk deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: {amount} Tk.")
            print(f"Amount {amount} Tk. withdrawn successfully.")
        else:
            print("Withdrawal amount exceeded Or Invalid amount.")

    def check_balance(self):
        print(f"Available balance: {self.balance} Tk.")

    def check_transaction_history(self):
        print("\nTransaction history:")
        for trn in self.transaction_history:
            print(trn)

    def take_loan(self, amount):
        if self.loan_count < 2:
            self.loan_taken += amount
            self.loan_count += 1
            self.balance += amount
            print(f"Loan of {amount} Tk. taken successfully.")
            self.transaction_history.append(f"Loan of {amount} Tk. taken.")
            
        else:
            print("You have already taken the maximum number of loans-->2 times")


    def transfer_amount(self, recipient_account_number, amount):
        recipient_found = False
        
        for user in admin.users_list:
            if user.account_number == recipient_account_number:
                recipient_found = True
                
                if amount <= self.balance and user !=self:
                    self.balance -= amount
                    user.balance += amount
                    self.transaction_history.append(f"{amount} Tk. Transferred to account number {recipient_account_number}")
                    print(f"Amount {amount} Tk. transferred successfully to account number {recipient_account_number}.")
                elif user == self: #Base Case
                    print("You cannot transfer to yourself.")
                    print("please enter valid account number")
                else:
                    print("Insufficient balance.")
                break
        
        if not recipient_found:
            print("User does not exist.")



admin = Admin()
current_user=None

while True:
    print("\n1. Register User Account")
    print("2. User Login")
    print("3. Admin Login")
    print("4. Exit")

    choice = int(input("Enter Option: "))
    
    if choice == 1:
        print("\n*******************")
        print("|  USER REGISTER  |")
        print("*******************")
        name = input("Enter your name: ")
        email_address = input("Enter your email address: ")
        print("\n 1.Savings Account\n 2.Current Account")
        account_type = int(input("Enter your account type: "))
        
        if account_type == 1:
            admin.create_account(name, email_address, 'Savings Account')
        elif account_type == 2:
            admin.create_account(name, email_address, 'Current Account')
        else:
            print("Invalid account type...press 1 or 2 only")

    if choice == 2:
        print("\n********************")
        print("|    USER  LOGIN    |")
        print("********************")
        account_number = int(input("Enter your account number: "))
        user_found = False

        for user in admin.users_list:
            if user.account_number == account_number:
                user_found = True
                current_user = user
                break

        if not user_found:
            print("Account not found.")
            continue

        while True:
            print("\n1. Deposit Amount")
            print("2. Withdraw Amount")
            print("3. My Balance")
            print("4. My Transaction History")
            print("5. Take Loan")
            print("6. Transfer Money to Another Account")
            print("7. Exit")

            option = int(input("\nEnter your option: "))

            if option == 1:
                amount = float(input("Enter the amount to deposit: "))
                current_user.deposit(amount)
                
            elif option == 2:
                amount = float(input("Enter the amount to withdraw: "))
                current_user.withdraw(amount)
                
            elif option == 3:
                current_user.check_balance()
                
            elif option == 4:
                current_user.check_transaction_history()
                
            elif option == 5:
                if admin.allow_loan==True:
                    amount = float(input("Enter the loan amount: "))
                    current_user.take_loan(amount)
                else:
                    print("Sorry...Loans are not allowed")
            elif option == 6:
                recipient_account_number = int(input("Enter the recipient's account number: "))
                amount = float(input("Enter the amount to transfer: "))
                current_user.transfer_amount(recipient_account_number, amount)
                
            elif option == 7:
                break
                
    elif choice == 3:
        print("\n********************")
        print("|    ADMIN  LOGIN   |")
        print("********************")
        password = input("\nEnter admin password: ")

        if password != "admin":
            print("Invalid password.")
            continue

        while True:
            print("\n1. Create Account")
            print("2. Delete Account")
            print("3. See All Accounts")
            print("4. Check Total Balance")
            print("5. Check Total Loan Amount")
            print("6. Loan Feature")
            print("7. Logout")

            option = int(input("\nEnter your option: "))

            if option == 1:
                name = input("Enter your name: ")
                email_address = input("Enter your email address: ")
                print("\n 1.Savings Account\n 2.Current Account")
                account_type = int(input("Enter your account type: "))
                if account_type == 1:
                    admin.create_account(name, email_address, 'Savings Account')
                elif account_type == 2:
                    admin.create_account(name, email_address, 'Current Account')
                else:
                    print("Invalid account type...press 1 or 2 only")
            elif option == 2:
                account_number = int(input("Enter the account number to delete: "))
                admin.delete_account(account_number)
                
            elif option == 3:
                admin.see_all_accounts()
                
            elif option == 4:
                admin.check_total_balance()
                
            elif option == 5:
                admin.check_total_loan_amount()
                
            elif option == 6:
                action = bool(int(input("Enter 1 to enable or 0 to disable loan feature: ")))
                admin.on_off_loan_features(action)

            elif option == 7:
                break
        
    elif choice == 4:
        break