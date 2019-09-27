# Search in Rotated Sorted Array
# Will Schick
# 9/27/2019

# ---

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array!!!

# Your algorithm's runtime complexity must be in the order of O(log n).

# ---
# Notes:
# So if it must be O(log n) <<logarithmic time>>, It'll have to be a binary search.
# How can we do binary search when everything is shifted?

# COMPLETION NOTES:
# This one was the hardest yet. ((Two hours of work))
# Here's a way of thinking of it that'll clarify how it works:
#
# From the middle index, either the left side is rotated, or the right side is.
# We can find which side is pivoted with the if statement: "if nums[lo] >= nums[mid]"
# If this statement is true: We know that the left side is abnormal, and the right is a typical sorted list
# If this statement is false: We know that the left side is normal, and by elimination the right side is abnormal.
# --
# Next we ask if the target falls into the normal sorted side,\\
#             and use that answer to determine where the high / low is placed for the next loop


# Essentially this is a binary search where the start index is random. Hm....
def search(nums, target):
    # local variables,
    low = 0
    high = len(nums)-1

    while low <= high:
        mid = (low + high) // 2
        print(low, mid, high)  # Debug

        # check to see if we found target
        if nums[mid] == target:
            return mid

        # Go through our four different cases.
        if nums[low] >= nums[mid]: # in this case, the left side is the abnormal / pivoted / rotated side
            if nums[mid] <= target <= nums[high]: # Does the target fall into the non-pivoted side?
                low = mid + 1
            else:
                high = mid - 1
        else: # In this case, the right side is the abnormal / pivoted / rotated side
            if nums[low] <= target <= nums[mid]: # Does the target fall into the non-pivoted side?
                high = mid - 1
            else:
                low = mid + 1


    # We couldn't find it!!!
    return -1


def main():
    num1 = [4,5,6,7,0,1,2]
    target1 = 0

    num2 = [4,5,6,7,0,1,2]
    target2 = 8

    print(search(num1, target1))
    print(search(num2, target2))

main()