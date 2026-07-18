import BankUtility as bu

class Account:
    def __init__(self):
        """ Account Constructor method"""

        # Each method should be private
        # Initially set the methods as None then use setter methods to set values
        self.__acct_number =  None
        self.__fname = None
        self.__lname = None
        self.__ssn = None
        self.__pin = None
        self.__balance = None

    def get_accountNumber(self):
        """ Retrieves the account's account number"""
        return self.__acct_number

    def set_accountNumber(self,acct_number):
        """ Sets the account's account number"""
        self.__acct_number = acct_number

    def get_ownerFirstName(self):
        """ Retrieves the account owner's first name"""
        return self.__fname

    def set_ownerFirstName(self,fname):
        """ Sets the account owner's first name"""
        self.__fname = fname
    
    def get_ownerLastName(self):
        """ Retrieves the account owner's last name"""
        return self.__lname

    def set_ownerLastName(self,lname):
        """ Sets the account owner's last name"""
        self.__lname = lname

    def get_SSN(self):
        """ Retrieves the account owner's SSN"""
        return self.__ssn

    def set_SSN(self,ssn):
        """ Sets the account owner's SSN"""
        self.__ssn = ssn

    def get_pin(self):
        """ Retrieves the account's PIN"""
        return self.__pin

    def set_pin(self,pin):
        """ Sets the account's PIN"""
        self.__pin = pin
    
    def get_Balance(self):
        """ Retrieves the account's balance """
        return self.__balance

    def set_Balance(self,balance):
        """ Sets the account's balance """
        self.__balance = balance

    def deposit(self,amount):
        """ Deposits an amount in cents into the account"""

        # Add the cents amount to the account's balance
        self.__balance += amount

        # Return the new balance
        return self.__balance
  
    def withdraw(self,amount):
        """ Withdraws an amount in cents from the account"""

        # First check if the account has sufficient funds
        # If insufficient funds, return None
        # Otherwise, subtract the withdrawal amount and return the new balance
        if amount > self.__balance:
            print(f"Insufficient funds in account {self.__acct_number}")
            return None
        else:
            self.__balance -= amount
            return self.__balance
    
    def isValidPIN(self,pin):
        """ Returns a boolean whether the PIN input matches what is on the account"""
        if self.__pin == pin:
            return True
        else:
            return False
    
    def toString(self):
        """ Returns a formatted string of account attributes"""

        account_details = f"""
{"="*40}\n
Account Number: {self.__acct_number}\n
Owner First Name: {self.__fname}\n
Owner Last Name: {self.__lname}\n
Owner SSN: XXX-XX-{self.__ssn[5:]}\n
PIN: {self.__pin}\n
Balance: ${bu.BankUtility().convertFromCentsToDollars(self.__balance):.2f}
        """

        return account_details

    def __repr__(self):
        """ Returns the formatted account details string if an account object is printed """
        return self.toString() 

    def __eq__(self,other):
        """ Returns a boolean whether two account objects have the same account number """
        if isinstance(other,Account):
            return self.get_accountNumber() == other.get_accountNumber()

