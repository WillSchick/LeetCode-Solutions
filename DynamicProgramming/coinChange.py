## CoinChange
## Will Schick
## 10/4/2019

#
# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
#
# If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.
#


# If I remember correctly from junior year I need to make a recursive backtracking algorithm
def coinChange(coins, amount):
    coins.sort(reverse = True) # reverse sort so the highest coins appear first

    # Base case: The amount is zero and no coins are used.
    if amount == 0:
        return 0
    elif amount < 0: # If our amount is negative for some reason, return -1
        return -1

    # Loop through the coins so we can try every available combo
    for i in range(len(coins)):
        if amount - coins[i] < 0: # If we overshoot our target we have to try the next lowest coin
            continue
        else:
            numCoins = coinChange(coins, amount - coins[i]) # Save the return value

            if numCoins == -1: # We hit a dead end down the line somewhere and need to try a different coin combo
                continue
            else:
                return numCoins + 1 # We found our solution! SEND IT DOWN THE LINE!!!!

    # We've tried every coin combo we could captain! A solution is not possible via this route, we need to back up
    return -1


def main():

    coins = [1, 2, 5]
    amount = 11

    print("Expected output: 3") # explanation: 11 = 5 + 5 + 1
    print(coinChange(coins, amount))


    ## =========

    coins = [2]
    amount = 3

    print("Expected output: -1")
    print(coinChange(coins, amount))



main()