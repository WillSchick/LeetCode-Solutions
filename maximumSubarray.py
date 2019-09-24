## Maximum subarray
## Will Schick
## 9/24/2019

# ---

# Given an integer array nums,
# return the contiguous subarray (containing at least one number) which has the largest sum

# ---
# notes:
# I'd like to solve this using linear time so I'll have to store
#       - firstNDX, NDX of the first element in our output subarray
#       - currSum, current running sum of elements from firstNDX until the current element
#       - greatestSum, a stored value representing the highest point of the currSum.
#       - stoppingNDX, NDX opposite from firstNDX to the current element. Updated when greatestSum is updated

# Algorithm
# Add element to variable currSum (current running sum)
# If the updated currSum is higher than the greatestSum, update our output array and set greatestSum to currSum
# If the currSum is less than zero, check to see if the current element is greater than the currSum and refresh firstNDX

def maxSubArray(nums):
    # initialize local variables to the first index
    savedStartingNDX = 0
    savedStoppingNDX = 1
    tempStartingNDX = 0
    currSum = 0
    greatestSum = 0

    for i in range(len(nums)):
        # If the element is higher than a running negative sum, refresh tempStartingNDX
        if currSum < 0 and nums[i] > currSum :
            tempStartingNDX = i
            currSum = 0  # reset our currSum. It'll increment up next

        # Increment the currSum
        currSum += nums[i]

        # Check to see if we have a new greatest Sum
        if greatestSum < currSum:
            greatestSum = currSum
            savedStartingNDX = tempStartingNDX
            savedStoppingNDX = i + 1

    # Now we have the start and stopping index of maxSubArray, let's build and return it.
    outputArray = []
    for i in range(savedStartingNDX, savedStoppingNDX):
        outputArray.append(nums[i])

    return outputArray


def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]

    print ("Expected output: [4, -1, 2, 1]")
    print(maxSubArray(nums))

main()