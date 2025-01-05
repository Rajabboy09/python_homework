import os
import json

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance} \n"
    
class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    def generate_account_number(self):
        return str(len(self.accounts) + 1)
    
    def create_account(self, name, initial_deposit):
        account_number = self.generate_account_number()
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")
    
    def deposit(self, account_number, amount):
        cheking = True
        while cheking:
            if amount <= 0:
                print("Deposit amount must be positive.")
            else:
                account = self.accounts.get(account_number)
                if account:
                    account.balance += amount
                    self.save_to_file()
                    print(f"Deposited {amount}. New balance: {account.balance}")
                else:
                    print("Account not found.")
                cheking = False

    def withdraw(self, account_number, amount):
        cheking = True
        account = self.accounts.get(account_number)
        while cheking:
            if amount <= 0:
                print("Deposit amount must be positive.")
            elif amount > account.balance:
                print("Insufficient funds")
            else:
                if account:
                    account.balance -= amount
                    self.save_to_file()
                    print(f"Deposited {amount}. New balance: {account.balance}")
                    cheking = False
                else:
                    print("Account not found.")
                
    
    def save_to_file(self):
        with open('accounts.txt', 'w') as f:
            json.dump({k: vars(v) for k , v in self.accounts.items()}, f)

    def load_from_file(self):
        if os.path.exists('accounts.txt'):
            with open('accounts.txt', 'r') as f:
                accounts_data = json.load(f)
                for account_number, account_info in accounts_data.items():
                    self.accounts[account_number] = Account(**account_info)
def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Banking Application")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(name, initial_deposit)

        elif choice == '2':
            account_number = input("Enter account number: ")
            bank.view_account(account_number)

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(account_number, amount)

        elif choice == '4':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(account_number, amount)

        elif choice == '5':
            print("Thank you for using the Banking Application!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()