## Product of Array Except Self
## Will Schick
## 9/18/2019

## ---

# Given an array called nums composed of n integers where n > 1,
#         return an array output such that output[i] is equal to the product of all elements of nums EXCEPT nums[i]

# SOLVE WITHOUT USING DIVISION!!!

# Follow up: Could you solve it with constant space complexity?

# ---

# Quadratic time complexity O(n^2) solution:
def productExceptSelf(nums):
    output = []

    for i in range(len(nums)):
        totalProduct = 1  # reset product

        # Loop through nums and create our product, ignoring nums[i]
        for j in range(len(nums)):
            if i != j:  # Only update totalProduct if the NDXs don't match
                totalProduct = totalProduct * nums[j]

        # append our product and continue to the next loop
        output.append(totalProduct)

    return output


# Linear time complexity O(n) solution:
#     (This one was a bit tougher since we can't use division. Got a hint from the discussion page on LeetCode)
#      Basically, output[i] is the product of all elements before and after num[i].
def productExceptSelfLinear(nums):
    productsLeft = []
    productsRight = []
    output = []

    # Build products of elements to the left
    product = 1
    for i in range(len(nums)):
        # For the first index
        if i == 0:
            productsLeft.append(1) # There's nothing to the left of the first index
        else:
            productsLeft.append(product)

        product = product * nums[i]  # Update product for the next loop


    # Build products of elements to the right
    product = 1
    for i in range(len(nums)-1,-1,-1):
        # We're building this backwards so using insert 0, will push everything where it should be
        # For the last index
        if i == len(nums)-1:
            productsRight.insert(0, 1)  # There's nothing to the right of the last index
        else:
            productsRight.insert(0, product)

        product = product * nums[i]  # Update product for the next loop


    # The products of each element of the left and right lists create the elements of our output
    for i in range(len(nums)):
        # Almost like magic, huh?
        output.append(productsLeft[i] * productsRight[i])

    return output


def main():

    nums = [1, 2, 3, 4]

    print(productExceptSelf(nums))
    print(productExceptSelfLinear(nums))

main()
