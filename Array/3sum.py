## 3Sum
## Will Schick
## 9/30/2019

# ---

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.


# The solution set must not contain duplicate triplets.

# ---

def threeSum(nums):
    output = []
    for a in range(len(nums)):
        for b in range(len(nums)):
            for c in range(len(nums)):
                if a != b and b != c and a!= c:  # Make sure they're separate elements
                    if nums[a] + nums[b] + nums[c] == 0:  # Check to see if they add up to zero
                        tempTriplet = [nums[a], nums[b], nums[c]]
                        tempTriplet.sort()
                        # Quickly look to see if our temp exists already in our output
                        if tempTriplet not in output:
                            output.append(tempTriplet)



    return output

# Finish notes:
#  My Only regret with this solution is that the time complexity is garbage. (You can tell this was a first draft.)
#  I'm pretty sure this is cubic time? O(n^3). I could try to bump it up to quadratic, let me draft some ideas.

#  I found an AMAZING solution on leetcode, learned a bunch reading through it.
#  They sorted nums and used this code to prevent duplicates
#             if i > 0 and nums[i] == nums[i-1]:
#                      continue
#  i - 1 

def main():
    nums = [-1, 0, 1, 2, -1, -4]

    print(threeSum(nums))

main()