class BankAccount:
    """Base class representing a bank account."""

    # counter = 0  # Static counter to generate unique account numbers

    def __init__(self, holder_name, branch, account_type, initial_deposit=0):
        self.account_number = Utility.get_next_account_number()
        self.holder_name = holder_name
        self.branch = branch
        self.account_type = account_type
        self.balance = initial_deposit
        self.is_suspended = False
        #self.counter += 1


    def deposit(self, amount):
        """Deposits money into the account (common logic for both account types)."""
        if not self.is_suspended:
            self.balance += amount
            return True
        else:
            print("Account is suspended. Deposits are not allowed.")
            return False

    def withdraw(self, amount):
        """Withdraws money from the account (common logic for both account types)."""
        if not self.is_suspended and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            if self.is_suspended:
                print("Account is suspended. Withdrawals are not allowed.")
            else:
                print("Insufficient funds.")
            return False

    def suspend_account(self):
        """Suspends the account, preventing transactions."""
        self.is_suspended = True
        print(f"Account {self.account_number} suspended.")

    def unsuspend_account(self):
        """Unsuspends the account, allowing transactions."""
        self.is_suspended = False
        print(f"Account {self.account_number} unsuspended.")

    def get_balance(self):
        """Returns the current account balance."""
        return self.balance

    def __str__(self):
        """Provides a string representation of the account details."""
        return f"""Account Number: {self.account_number}
Holder Name: {self.holder_name}
Branch: {self.branch}
Account Type: {self.account_type}
Balance: {self.balance:.2f}
Suspended: {'Yes' if self.is_suspended else 'No'}"""


class SavingsAccount(BankAccount):
    """Savings account class with an enhanced deposit calculation."""

    def __init__(self, holder_name, branch, initial_deposit=0):
        super().__init__(holder_name, branch, "Savings", initial_deposit)

    def deposit(self, amount):
        """Deposits money into the savings account with an additional 2.5% interest."""
        if super().deposit(amount * 1.025):  # Call parent class deposit with bonus
            print(
                f"Deposited BDT {amount:.2f} with 2.5% interest (BDT {amount * 0.025:.2f}).")
            return True
        else:
            return False


class CurrentAccount(BankAccount):
    """Current account class with a basic deposit functionality."""

    def __init__(self, holder_name, branch, initial_deposit=0):
        super().__init__(holder_name, branch, "Current", initial_deposit)


class Utility:
    """Static class for managing the account number counter."""
    counter = 0
    @staticmethod
    def get_next_account_number():
        """Generates a unique account number using the counter."""
        Utility.counter += 1
        return Utility.counter

accounts = []
ac1 = SavingsAccount("mahi", "Gazipur", 1000)
print(ac1)
accounts.append(ac1)
ac2 = SavingsAccount("Habibi", "Gazipur", 500)
print(ac2)