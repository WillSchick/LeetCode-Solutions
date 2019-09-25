## Maximum Product Subarray
## Will Schick
## 9/25/2019

# ---
# Given an integer array nums, \\
#  return the contiguous subarray within an array (containing at least one number) which has the largest product.
# ---


# Quadratic Solution
def maxProductQuad(nums):

    # Initialize Local Variables
    savedStartNDX = 0
    savedStopNDX = 1
    currProduct = nums[0]
    maxProduct = nums[0]

    # Loop through and check every possible contiguous subarray. This isn't nearly as efficient as O(n).
    for i in (range(len(nums)-1)):  # Don't check the last to avoid NDX error with the j loop
        currProduct = nums[i]
        for j in (range(i+1, len(nums))):
            currProduct = currProduct * nums[j]

            # check to see if we found a new max product
            if currProduct > maxProduct:
                maxProduct = currProduct
                savedStopNDX = j+1

    # We still need to check the last NDX since we ended the i loop early
    if nums[-1] > maxProduct:
        outputArray = nums[-1]
        return outputArray

    # Build and return outputArray
    outputArray = []
    for i in (range(savedStartNDX, savedStopNDX)):
        outputArray.append(nums[i])
    return outputArray


# Linear solution notes:
#     The hardest part of this solution is that two negatives could potentially create a new max
#     I read some solutions on leetcode that stored the min and max and chose between them for the output, let's try
#            PS. I realized I had to return the actual product, not the subarray. So let's do that this time.
#            PSS. I'm going to heavily comment this so I can understand my own thought process better

def maxProductLinear(nums):
    #  Initialize Local Variables
    maxProd = nums [0]
    minProd = nums[0]
    highestMax = nums[0]

    for i in range(1, len(nums)):
        # Either of these could be the new maximum:
        # the current element is the highest (essentially resetting the startingNDX,
        # the running max * the current element
        # the running min * the current element (rememeber that negatives exist!)
        maxProd = max(nums[i],
                      maxProd * nums[i],
                      minProd * nums[i])

        # Either of these could be the newest minimum:
        # the current element could be the lowest (essentially resetting the minstartingNDX,
        # the current running min * the current element
        # the current running max * the current element
        minProd = min (nums[i],
                       maxProd * nums[i],
                       minProd * nums[i])

        # Now we need to compare our current max to the highestMax so far to see if we have a possible answer.
        # (Remember that maxProd is essentially the highest POSSIBLE product in each iteration, \\
        #           not necessarily the highest max SO FAR. That's what highestMax is for!)
        #           PS. Does that make a little more sense now? Yes? Good.

        # Either the newest possible max product is the highest so far,
        #        or our old highest is still the reigning king
        highestMax = max(maxProd,
                         highestMax)


    return highestMax


def main():
    nums = [2,3,-2,4]
    nums2 = [-2,0,-1]

    print(maxProductQuad(nums))
    print(maxProductQuad(nums2))

    print()
    print("Linear solutions")
    print(maxProductLinear(nums))
    print(maxProductLinear(nums2))


main()