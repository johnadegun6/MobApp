import pandas as pd
import os
import random
class Bank:

    def __init__(self, name, acc_num):
        self.name = name
        self.acc_num = acc_num

    def withdraw(self, amount):
        self.amount = amount
        self.column = name + "-" + str(self.acc_num)
        self.accounts_df = pd.read_excel(os.getcwd() + "/accounts.xlsx")
        self.accounts_df[self.column] = self.accounts_df[self.column].loc[0] - amount
        self.accounts_df.to_excel(os.getcwd() + "/accounts.xlsx", index=False)

    def deposit(self, amount):
        self.amount = amount
        self.column = name + "-" + str(self.acc_num)
        self.accounts_df = pd.read_excel(os.getcwd() + "/accounts.xlsx")
        self.accounts_df[self.column] = self.accounts_df[self.column].loc[0] + amount
        self.accounts_df.to_excel(os.getcwd() + "/accounts.xlsx", index=False)

    def display_balance(self):
        self.column = self.name + "-" + str(self.acc_num)
        self.accounts_df = pd.read_excel(os.getcwd() + "/accounts.xlsx")
        print(self.accounts_df[self.column].loc[0])

    def transfer(self, from_account_number, to_account_number, amount):
        # Check if both accounts exist and if the balance is sufficient for the transfer
        if from_account_number not in self.accounts or to_account_number not in self.accounts:
            print("One or both accounts do not exist.")
            return

        if self.accounts[from_account_number].balance < amount:
            print("Insufficient balance.")
            return

        # Update the account balances and create a new Transaction object
        self.accounts[from_account_number].balance -= amount
        self.accounts[to_account_number].balance += amount
        transaction = Transaction(from_account_number, to_account_number, amount, datetime.now())
        self.transactions.append(transaction)

        print("Transfer successful.")

    def get_transaction_history(self, account_number):
        # Check if the account exists and filter transactions by account number
        if account_number not in self.accounts:
            print("Account does not exist.")
            return

        account_transactions = filter(lambda transaction: transaction.from_account == account_number or transaction.to_account == account_number, self.transactions)

        # Print the transaction history for the account
        print("Transaction history for account ", account_number)
        for transaction in account_transactions:
            print("From account ", transaction.from_account, " to account ", transaction.to_account, " amount ", transaction.amount, " date ", transaction.date)


class User():

    def __init__(self, name):
        self.name = name

    def create_new_user(self, int_dep):
        self.int_dep = int_dep
        self.account_num = random.randint(10000, 99999)

        if not os.path.exists(os.getcwd() + "/accounts.xlsx"):
            data = {
                self.name + "-" + str(self.account_num): [self.int_dep]
            }
            self.int_dep_df = pd.DataFrame(data)
        else:
            self.int_dep_df = pd.read_excel(os.getcwd() + "/accounts.xlsx", index=False)
            print(self.account_num)
            print('bfor')
            while True:
                if self.name + "-" + str(self.account_num) in self.int_dep_df.columns:
                    self.account_num = random.randint(10000, 99999)
                else:
                    break

            self.int_dep_df[self.name + "-" + str(self.account_num)] = self.int_dep
        self.int_dep_df.to_excel(os.getcwd() + "/accounts.xlsx", index=False)
        return 'Your account has been created you can now login with your name: ' + self.name + ' and account number: '\
               + str(self.account_num)

    def existing_user(self, account_num):
        self.account_num = account_num
        ex_user_df = pd.read_excel(os.getcwd() + "/accounts.xlsx")
        if self.name + "-" + str(self.account_num) in ex_user_df.columns:
            return 'ok'
        else:
            return 'no user with these credentials, please enter again'


while True:
    print('enter 1 if existing user')
    print('enter 2 to new user')
    user_input = int(input())
    if user_input == 1:
        while True:
            name = input('Enter your name')
            acc_number = int(input('Enter your account number'))
            u = User(name)
            check_ex_user = u.existing_user(acc_number)
            if 'ok' in check_ex_user:
                while True:
                    print('enter 4 to deposit')
                    print('enter 5 to withdraw')
                    print('enter 6 to display')
                    print('enter 7 to transfer')
                    print('enter 8 to view transaction history')
                    print('enter 9 to exit')
                    bank_actions = int(input())
                    bank_ob = Bank(name, acc_number)
                    if bank_actions == 4:
                        print('Enter amount to deposit')
                        dep = int(input())
                        bank_ob.deposit(dep)
                    elif bank_actions == 5:
                        print('Enter amount to withdraw')
                        withdraw_am = int(input())
                        bank_ob.withdraw(withdraw_am)
                    elif bank_actions == 6:
                        print('Your current balance is;')
                        bank_ob.display_balance()
                    elif bank_actions == 7:
                        print("Transfer successful.")
                        bank_ob.display_balance()
                    elif bank_actions == 8:
                        print("From account ", transaction.from_account, " to account ", transaction.to_account, " amount ", transaction.amount, " date ", transaction.date)
                        bank_ob.display_balance()
                    elif bank_actions == 9:
                        break
                break
            else:
                print(check_ex_user)
                continue
    elif user_input == 2:
        name = input('Enter your name')
        int_dep = int(input('Enter your initial deposit'))
        u = User(name)
        u.create_new_user(int_dep)
        continue