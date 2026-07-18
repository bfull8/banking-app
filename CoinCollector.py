import re

class CoinCollector:

    # Constructor so you cannot instantiate this class
    def __init__(self):
        pass

    def parseChange(self,coins):
        
        # Check the string entered for any invalid coins
        p = re.compile(r"[^PNDQHW]")
        invalid_coins = re.findall(p,coins)

        # Print the list of invalid coins
        if invalid_coins != None:
            print(f"Invalid Coin(s): {",".join(invalid_coins)}")

        # Remove the invalid coins from the coins to be counted
        coins = re.sub(p,"",coins)
        
        # For each coin, find the associated cent value and add it to a running total
        values = {"P":1,"N":5,"D":10,"Q":25,"H":50,"W":100}

        total_cents = 0
        for coin in coins:
            total_cents += values[coin]
        
        return total_cents
