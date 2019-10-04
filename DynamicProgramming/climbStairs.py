## Climbing Stairs
## Will Schick
## 10/3/2019

##

# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

##

# Recursive solution
def climbStairsRecursion(n):
    # n = number of stairs
    # Base case: We're on the floor or the first step
    if n == 0 or n == 1:
        return 1
    else: # Step is GREATER than 1 (2 or above)
        return climbStairsRecursion(n-1) + climbStairsRecursion(n-2)


# I'm only just getting into Memoized and bottom up solutions, so forgive me if this doesn't work quite right!
# Dynamic Programming solution (Memoized Solution)
def climbStairsDynamic(n, memo):
    if memo[n] is not None: # If the index exists, return it instead of computing it.
        return memo[n] # This allows us to save on repetitious computation time (Better than our recursive solution!!!!)
    else: # If we need to compute it
        if n == 0 or n == 1: # If we're on the floor or bottom step...
            memo[n] = 1
            return 1
        else: # If we're step 2 or higher...
            memo[n] = climbStairsDynamic(n-1, memo) + climbStairsDynamic(n-2, memo)
            return memo[n]


def main():
    # Set stairs
    n = 10

    print(climbStairsRecursion(n))

    memo = [None] * (n+1) # Create an empty list with n+1 elements for memoing
    print(climbStairsDynamic(n,memo))

main()

