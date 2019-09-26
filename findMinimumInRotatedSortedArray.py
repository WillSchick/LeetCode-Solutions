## Find Minimum in Rotated Storage Array
## Will Schick
## 9/26/2019

# ---

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2])

# Find the minimum element.

# You may assume no duplicate exists in the array.

# ---

#  Since no duplicates exist and the list is sorted, this should be a cinch
def findMin(nums):
    for i in range(len(nums)-1): # We reference i+1 so we need to end the loop early
        if nums[i] > nums[i+1]: # This num is min
            return nums[i+1]

    # The only case this statement doesn't cover is if nums[0] is the min, and the list hasn't been shifted/rotated
    return nums[0]


def main():
    nums = [3,4,5,1,2]
    nums2 = [4,5,6,7,0,1,2]
    nums3 = [1, 2, 3, 4, 5]  # Control group so to say

    print(findMin(nums))
    print(findMin(nums2))
    print(findMin(nums3))


main()