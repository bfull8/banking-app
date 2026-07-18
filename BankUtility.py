import random

class BankUtility:
    def __init__(self):
        pass

    def promptUserForString(self,prompt):
        """ 
            Prompts the user for an input based on parameter provided 
            and returns user input as a string
        """
        value = input(prompt)
        
        return value

    def promptUserForPositiveNumber(self,prompt):
        """ 
            Prompts the user for an input based on parameter provided 
            and returns user input as a float
        """

        # Continue to ask for the input until a number greater than 0 is entered
        # Then return the number as a float
        while True:
            try:
                value = float(input(prompt))
            except:
                print("The amount entered is not a number.")
                continue
        
            if value <= 0:
                print("Amount cannot be negative. Try again")
                continue
            else:
                return value

    def convertFromDollarsToCents(self,amount):
        """ Converts dollar value to cents and returns an integer """
        cents_amount = int(amount * 100)
        
        return cents_amount

    def convertFromCentsToDollars(self,cents):
        """ Converts cents value to dollar and returns a float """
        dollar_amount = float(cents / 100)

        return dollar_amount
        
    def generateRandomInteger(self,min, max):
        """ Returns a random int between the min and max (inclusive)"""
        random_number = random.randint(min,max)
        
        return random_number

    def isValidDollarAmount(self,amount):
        """ Checks that only two decimals are in a user's dollar input"""

        # Count how many digits are after the decimal and return True if there are 2 or less
        # Otherwise, return False
        if len(str(amount)[str(amount).index("."):]) > 3:
            print("The dollar amount can only have 2 digits after the decimal. Try again.")
            return False
        else:
            return True

    def atmWithdrawal(self,amount):
        """ Performs operations for an ATM withdrawal """

        # Only 20s, 10s, and 5s can be withdrawn from an ATM
        # Key = dollar-bill, value = amount to be dispensed
        result = {20:0,10:0,5:0}

        # ATM withdrawal must be in increments of 5 and between 5 and 1000
        if (amount < 5) or (amount > 1000) or (amount % 5 != 0):
            print("Invalid Amount. Try Again.")
            return None
        else:
            # Calculate the max amount of dollar bills at 20, then 10, then 5
            for bill in result.keys():
                result[bill] = int(amount // bill)
                amount %= bill
            
            return result

    
    '''
      Checks if a given string is a number (long)
      This does NOT handle decimals.
      
      YOU DO NOT NEED TO CHANGE THIS METHOD
      THIS IS FREE FOR YOU TO USE AS NEEDED
      
      @param numberToCheck String to check
      @return true if the String is a number, false otherwise
     '''
    def isNumeric(self,numberToCheck):
        try:
            if numberToCheck.isdigit():
                return True
            else:
                return False
        except ValueError:
            return False
