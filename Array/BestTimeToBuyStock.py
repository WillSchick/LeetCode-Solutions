## BestTimeToBuyStock.py
## Will Schick
## 9/16/2019

# -----

# You have an array for which the i^th element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (one buy and one sell),
#          design an algorithm to find the maximum profit.

# Note; you cannot sell a stock before you buy one

# SELF IMPOSED EXTRA CREDIT: Print the day of purchase and selling into the console!

# -----


def maxProfit(prices):
    # Initialize values
    lowestPrice = prices[0]
    tempBuyNDX = 0 # This gets updates alongside lowestPrice. We use it to update the final buyNDX

    profit = 0  # There's a chance that we don't want to buy or sell ANYTHING

    # These two are used for final reporting of the sell and buy date. Update these when you've actually sold something.
    buyNDX = -1
    sellNDX = -1

    # Loop through the prices
    for i in range(len(prices)):
        # If the current price is lower than our lowest price-- retroactively buy here instead
        if prices[i] < lowestPrice:
            lowestPrice = prices[i]
            tempBuyNDX = i

        # If the potential profit of selling here is higher than our record profit, then sell here
        if (prices[i] - lowestPrice) > profit:
            profit = prices[i] - lowestPrice
            buyNDX = tempBuyNDX
            sellNDX = i


    # Now we report our final buy and sell NDX
    if buyNDX == -1:
        print("It is more profitable to buy nothing at all!")
    else:
        print("BUY on day", buyNDX+1)
        print("SELL on day", sellNDX+1)

    return profit



def main():
    # Establish our prices
    prices = [7,2,5,3,6,1] # Buy on day 2, sell on day 5
    prices2 = [7,5,3,1] # Don't buy!

    print("Scenario 1--")
    print(maxProfit(prices))

    print()
    print()

    print("Scenario 2--")
    print(maxProfit(prices2))


main()


