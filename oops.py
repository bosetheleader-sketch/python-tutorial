class BankAccount:
    bank_name = "Python Bank"

    def __init__(self, account_no, holder_name, balance=0):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount
        self.transactions.append(f"Withdrew ₹{amount}")
        print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def show_transactions(self):
        print("\nTransaction History:")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print("-", transaction)

    def display_account(self):
        print("\nAccount Details")
        print("Bank Name:", BankAccount.bank_name)
        print("Account No:", self.account_no)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_no, holder_name, balance=0, interest_rate=5):
        super().__init__(account_no, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        self.transactions.append(f"Interest added ₹{interest}")
        print(f"Interest ₹{interest} added successfully.")


class CurrentAccount(BankAccount):
    def __init__(self, account_no, holder_name, balance=0, overdraft_limit=5000):
        super().__init__(account_no, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance + self.overdraft_limit:
            print("Overdraft limit exceeded.")
            return

        self.balance -= amount
        self.transactions.append(f"Withdrew ₹{amount}")
        print(f"₹{amount} withdrawn successfully.")


# -------------------------------
# Main Program
# -------------------------------

accounts = []

def create_account():
    print("\n1. Savings Account")
    print("2. Current Account")

    choice = input("Choose account type: ")

    account_no = input("Enter account number: ")
    name = input("Enter account holder name: ")
    balance = float(input("Enter opening balance: "))

    if choice == "1":
        account = SavingsAccount(account_no, name, balance)
    elif choice == "2":
        account = CurrentAccount(account_no, name, balance)
    else:
        print("Invalid choice.")
        return

    accounts.append(account)
    print("Account created successfully.")


def find_account(account_no):
    for account in accounts:
        if account.account_no == account_no:
            return account
    return None


while True:
    print("\n===== Bank Account Management System =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Show Account Details")
    print("6. Show Transactions")
    print("7. Add Interest")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        acc_no = input("Enter account number: ")
        acc = find_account(acc_no)

        if acc:
            amount = float(input("Enter amount: "))
            acc.deposit(amount)
        else:
            print("Account not found.")

    elif choice == "3":
        acc_no = input("Enter account number: ")
        acc = find_account(acc_no)

        if acc:
            amount = float(input("Enter amount: "))
            acc.withdraw(amount)
        else:
            print("Account not found.")

    elif choice == "4":
        acc_no = input("Enter account number: ")
        acc = find_account(acc_no)

        if acc:
            acc.check_balance()
        else:
            print("Account not found.")

    elif choice == "5":
        acc_no = input("Enter account number: ")
        acc = find_account(acc_no)

        if acc:
            acc.display_account()
        else:
            print("Account not found.")

    elif choice == "6":
        acc_no = input("Enter account number: ")
        acc = find_account(acc_no)

        if acc:
            acc.show_transactions()
        else:
            print("Account not found.")

    elif choice == "7":
        acc_no = input("Enter account number: ")
        acc = find_account(acc_no)

        if isinstance(acc, SavingsAccount):
            acc.add_interest()
        else:
            print("Interest only applies to Savings Account.")

    elif choice == "8":
        print("Thank you for using Python Bank.")
        break

    else:
        print("Invalid choice. Try again.")
