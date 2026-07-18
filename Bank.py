import BankUtility as bu

class Bank:
    def __init__(self):
        """ Constructor for Bank Object"""
        self.account_limit = 100

        # Initialize a list to hold accounts with None as the placeholder
        # Number of elements is set by account limit
        self.accounts = [None] * self.account_limit

    def addAccountToBank(self,account):
        """ Receives an account Object to place in the bank's accounts attribute"""

        # None indicates an account spot is available.
        if None not in self.accounts:
            print("No more accounts available")
            return False
        else:
            # Find the first index where an account is available
            null_index = self.accounts.index(None)

            #Place the account object at that index
            self.accounts[null_index] = account
            return True

    def removeAccountFromBank(self,account):
        """ Removes an account object from the bank's accounts attribute"""

        # Account numbers are unique, so we can use index() to find index of account number
        # Account Object equality is set to compare account numbers
        account_index = self.accounts.index(account)

        # Set the account index to None to remove it
        self.accounts[account_index] = None

        # Print that the account is closed
        print(f"Account {account.get_accountNumber()} closed")
    
    def findAccount(self,accountNumber):
        """ Retrieves an account object based on account number"""

        # Loop through each account's account number and return the account if there is a match
        for account in self.accounts:
            if account == None:
                continue
            elif account.get_accountNumber() == accountNumber:
                return account
        
        # Return None if no account is found
        return None

    def addMonthlyInterest(self,percent):
        # EXTRA CREDIT

        # Convert the annual interest into a monthly rate
        monthly_apr = (percent / 100) / 12

        # For each account:
        # Find the monthly interest (balance * monthly interest rate)
        # Call the deposit method to deposit the interest
        # Display the new balance
        for account in self.accounts:
            if account != None:
                monthly_interest = account.get_Balance() * monthly_apr

                account.deposit(monthly_interest)

                print(f"Deposited interest: ${bu.BankUtility().convertFromCentsToDollars(monthly_interest):.2f} into account number {account.get_accountNumber()}, new balance: ${bu.BankUtility().convertFromCentsToDollars(account.get_Balance()):.2f}")
        
        