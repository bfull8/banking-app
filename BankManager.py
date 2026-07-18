import Bank
import BankUtility as bu
import Account
import CoinCollector as cc

class BankManager:
    def __init__(self):
        """Constructor will create an instance of the Bank Class """
        self.bank = Bank.Bank()

    @staticmethod    
    def promptForAccountNumberAndPIN(bank):
        """ Returns an Account object if it is present in the Bank object """

        # Account Number is an 8-digit integer
        # If the number entered is not a number, return an error
        try:
            account_number = int(bu.BankUtility().promptUserForString("Enter Account Number:\n"))
        except:
            print(f"Account number must be a number")
            return None

        # Call the findAccount method which returns an Account object from the bank object
        matched_account = bank.findAccount(account_number)

        # Ask for PIN if an account with that number is found, otherwise say the account is not found
        if matched_account != None:

            # Account PIN is a string
            account_pin = bu.BankUtility().promptUserForString("Enter Account PIN:\n")

            # If the PIN input matches what is on the account, return the account. Otherwise, say invalid PIN
            if matched_account.isValidPIN(account_pin):
                return matched_account
            else:
                print("Invalid PIN")
                return None
        else:
            print(f"Account not found for account number: {account_number}")
            return None


    def main(self):
        """ Method to be called to run the program"""

        # Continue to run program until user inputs 11.
        while True:
            print("="*40)
            print("What do you want to do? ")
            print("1. Open an account")
            print("2. Get account information and balance")
            print("3. Change PIN")
            print("4. Deposit money in account")
            print("5. Transfer money between accounts")
            print("6. Withdraw money from account")
            print("7. ATM withdrawal")
            print("8. Deposit change")
            print("9. Close an account")
            print("10. Add monthly interest to all accounts")
            print("11. End Program")
            print("="*40)

            menu_item = bu.BankUtility().promptUserForString(">>Input: ")

            # Based on the menu item selected, perform the respective operations
            # Error is returned if 1 - 11 are not entered
            match menu_item:
                case "1":
                    """ Open an account """

                    # Prompt the user to enter a First and Last Name for the Account Owner
                    fname = bu.BankUtility().promptUserForString("Enter Account Owner's First Name:\n")
                    lname = bu.BankUtility().promptUserForString("Enter Account Owner's Last Name:\n")
                    
                    # Prompt the user to enter a PIN as a string
                    while True:
                        ssn = bu.BankUtility().promptUserForString("Enter Account Owner's SSN (9 digits):\n")

                        # Check whether the input is a number
                        if bu.BankUtility().isNumeric(ssn) == False:
                            print(f"{ssn} is not a number")
                            continue
                        # Check whether 9 digits were entered
                        elif len(ssn) != 9:
                            print("Social Security Number must be 9 digits")
                            continue
                        # Break the loop if a valid SSN is entered
                        else:
                            break

                    # Generate a random 4 digit account PIN and convert it to a string
                    # The account can start with 1 or more zeros so generate each digit separately and concatenate
                    pin = ""
                    for i in range(4):
                        pin += str(bu.BankUtility().generateRandomInteger(0, 9))

                    # Generate a random 8 digit Account Number as an integer. Cannot start with 0
                    # If the account number is already present in the bank, generate a new number
                    while True:
                        account_number = bu.BankUtility().generateRandomInteger(10000000, 99999999)

                        if self.bank.findAccount(account_number) == None:
                            break
                        else:
                            continue

                    # Create Account Instance and set attributes using the values above
                    new_account = Account.Account()
                    new_account.set_ownerFirstName(fname)
                    new_account.set_ownerLastName(lname)
                    new_account.set_SSN(ssn)
                    new_account.set_pin(pin)
                    new_account.set_accountNumber(account_number)
                    #Initially set the balance as 0
                    new_account.set_Balance(0)

                    # Add account to the bank if there is room
                    if self.bank.addAccountToBank(new_account):
                        print(new_account)
        
                case "2":
                    """ Get account information and balance"""

                    # Prompt for account details and return matched account
                    account = BankManager().promptForAccountNumberAndPIN(self.bank)

                    # If an account is found, print the details
                    if account != None:
                        print(account)
                    
                case "3":
                    """ Change PIN """

                    # Prompt for account details and return matched account
                    account = BankManager().promptForAccountNumberAndPIN(self.bank)

                    # If an account is found, continue to change the PIN
                    if account != None:
                    
                        # Continue to ask for a pin until a new one is set
                        while True:
                            new_pin = bu.BankUtility().promptUserForString("Enter new PIN:\n")
                            
                            # If the new pin is not 4 digits, return an error and ask again
                            # Otherwise, ask for the user to enter the pin again
                            if bu.BankUtility().isNumeric(new_pin) == False:
                                print(f"{new_pin} is not a number.\nPIN must be 4 digits, try again")
                                continue
                            elif len(new_pin) != 4:
                                    print("PIN must be 4 digits, try again")
                                    continue
                            else:
                                confirm_pin = bu.BankUtility().promptUserForString("Enter new PIN again to confirm:\n")

                            # If the two PIN entries match, call the setter method for the PIN
                            # Otherwise, return to the top to ask for a new PIN
                            if new_pin == confirm_pin:
                                account.set_pin(confirm_pin)
                                print("PIN updated")
                                break
                            else:
                                print("PINs do not match, try again.")


                case "4":
                    """ Deposit Money into account"""

                    # Prompt for account details and return matched account
                    account = BankManager().promptForAccountNumberAndPIN(self.bank)

                    # If an account is found, continue to deposit the money
                    if account != None:
                        # Continue to prompt for a number until a valid number is given
                        while True:
                            # Prompt the user to enter a dollar amount. An error will be returned if a number is not entered or a negative is not entered
                            deposit_amount = bu.BankUtility().promptUserForPositiveNumber("Enter amount to deposit in dollars and cents (e.g. 2.57):\n")

                            # Check whether the amount entered only has 2 decimals for the cents
                            # If so, convert the dollar amount to cents and call the deposit method to increase the balance for the account
                            if bu.BankUtility().isValidDollarAmount(deposit_amount):
                                deposit_amount_cents = bu.BankUtility().convertFromDollarsToCents(deposit_amount)

                                account.deposit(deposit_amount_cents)

                                print()
                                print(f"New balance: ${bu.BankUtility().convertFromCentsToDollars(account.get_Balance()):.2f}")
                                break
                
                case "5":
                    """ Transfer money between accounts"""

                    # Prompt for account details for the account to withdraw from and return the account
                    print("Account to Transfer From:")
                    withdraw_account = BankManager().promptForAccountNumberAndPIN(self.bank)

                    # Only prompt for account details of the account to deposit to if a withdraw account is found
                    if withdraw_account != None:

                        # Prompt for account details for the account to deposit to and return the account
                        print("Account to Transfer To:")
                        deposit_account = BankManager().promptForAccountNumberAndPIN(self.bank)

                        # If a deposit account is found, begin asking for the dollar amount
                        if deposit_account != None:
                            while True:

                                # Prompt for a dollar amount to transfer
                                amount = bu.BankUtility().promptUserForPositiveNumber("Enter amount to transfer in dollars and cents (e.g. 2.57):\n")

                                # If a positive number with <= 2 decimals is input, continue to transfer
                                if bu.BankUtility().isValidDollarAmount(amount):

                                    # Convert the dollar amount to cents
                                    amount_cents = bu.BankUtility().convertFromDollarsToCents(amount)
                                    
                                    # Call the withdraw method which will return the new balance if there are sufficient funds
                                    withdraw_balance = withdraw_account.withdraw(amount_cents)

                                    # If the account does not have sufficient funds, go back to the main menu
                                    # Otherise, deposit the amount in the deposit account and display both accounts new balances
                                    if withdraw_balance == None:
                                        break
                                    else:
                                        deposit_balance = deposit_account.deposit(amount_cents)
                                        print()
                                        print("Transfer Complete")
                                        print(f"New balance in account: {withdraw_account.get_accountNumber()} is: ${bu.BankUtility().convertFromCentsToDollars(withdraw_balance):.2f}")
                                        print(f"New balance in account: {deposit_account.get_accountNumber()} is: ${bu.BankUtility().convertFromCentsToDollars(deposit_balance):.2f}")
                                        break
                        
                case "6":
                    """ Withdraw money from an account """
                         
                    # Prompt for account details for the account to withdraw from and return the account
                    account = BankManager().promptForAccountNumberAndPIN(self.bank)
                    
                    # If an account is found, proceed to withdraw from account
                    if account != None:
                        while True:
                            # Prompt for a dollar amount to withdraw
                            withdraw_amount = bu.BankUtility().promptUserForPositiveNumber("Enter amount to Withdraw in dollars and cents (e.g. 2.57):\n")

                            # If a positive number with <= 2 decimals is input, continue to withdraw
                            if bu.BankUtility().isValidDollarAmount(withdraw_amount):

                                # Converrt withdrawal amount to cents
                                withdraw_amount_cents = bu.BankUtility().convertFromDollarsToCents(withdraw_amount)

                                # Call withdraw method to attempt to withdraw. Must have sufficient funds
                                new_balance = account.withdraw(withdraw_amount_cents)

                                # If the account does not have sufficients funds, go back to the main menu
                                # Otherise, deduct the withdrawal amount from the balance
                                if new_balance == None:
                                    break
                                else:
                                    print()
                                    print(f"New balance: ${bu.BankUtility().convertFromCentsToDollars(new_balance):.2f}")
                                    break

                case "7":
                    """ ATM Withdrawal"""

                    # Prompt for account details for the account to withdraw from and return the account
                    account = BankManager().promptForAccountNumberAndPIN(self.bank)

                    # If an account is found, proceed to withdraw from account
                    if account != None:
                        while True:

                            # Prompt for a dollar amount to withdraw
                            withdraw_amount = bu.BankUtility().promptUserForPositiveNumber("Enter amount to Withdraw in dollars (no cents) in multiples of $5 (limit $1000):\n")

                            # Call the atmWithdrawal method
                            # Checks for proper number withdrawal amount and calculates bills to return
                            bills_returned = bu.BankUtility().atmWithdrawal(withdraw_amount)

                            # If the dollar amount entered can be dispensed via a ATM, proceed
                            if bills_returned != None:
                                
                                # Convert dollar amount to cents
                                withdraw_amount_cents = bu.BankUtility().convertFromDollarsToCents(withdraw_amount)
                                
                                # Call withdraw method to attempt to withdraw. Must have sufficient funds
                                withdraw_balance = account.withdraw(withdraw_amount_cents)

                                # If the account does not have sufficients funds, go back to the main menu
                                # Otherise, deduct the withdrawal amount from the balance and print bills to be dispensed
                                if withdraw_balance == None:
                                    break
                                else:
                                    print()
                                    for bill,quantity in bills_returned.items():
                                        print(f"Number of {bill}-dollar bills: {quantity}")
                                
                                    print(f"New balance: ${bu.BankUtility().convertFromCentsToDollars(withdraw_balance):.2f}")
                                    break
                        
                case "8":
                    """ Deposit Change into an account"""

                    # Prompt for account details for the account to deposit to and return the account
                    account = BankManager().promptForAccountNumberAndPIN(self.bank)

                    # If an account is found, proceed to deposit
                    if account != None:

                        # Prompt the user to enter coins
                        coins = bu.BankUtility().promptUserForString("Deposit Coins:\n").upper()

                        # Parse the change to return any invalid coins and then deposit the amount
                        print()
                        deposit_amount = cc.CoinCollector().parseChange(coins)
                        account.deposit(deposit_amount)
                        print(f"${bu.BankUtility().convertFromCentsToDollars(deposit_amount):.2f} in coins deposited into account")
                        print(f"New balance: ${bu.BankUtility().convertFromCentsToDollars(account.get_Balance()):.2f}")
                        


                case "9":
                    """ Close an account """
                    # Prompt for account details for the account to remove
                    account = BankManager().promptForAccountNumberAndPIN(self.bank)

                    # If the account is present, remove the account
                    # This will set the index where the account object is to None
                    if account != None:
                        self.bank.removeAccountFromBank(account)
                    
                case "10":
                    while True:
                        apy = bu.BankUtility().promptUserForPositiveNumber("Enter annual interest rate percentage (e.g. 2.75 for 2.75%):\n")

                        # Check that a valid percent between 0 and 100 is entered
                        if apy < 0 or apy > 100:
                            print("Enter a valid percent between 0 and 100. Try again.")
                            continue
                        else:
                            break

                    # Call the addMonthlyInterest method
                    # Deposits a monthly interest to all accounts in the bank based on user interest rate input      
                    self.bank.addMonthlyInterest(apy)

                case "11":
                    """ End program """
                    break
                case _:
                    print("Invalid Choice")

if __name__ == '__main__':
    # Initialize BankManager and call main() method
    bank_manager = BankManager()
    bank_manager.main()



    
