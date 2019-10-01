## Container With Most Water
## Will Schick
## 10/1/2019

# ---

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Image ref: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
# ((Hey look it's stored in an s3 container!!!! I know that now!!))
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. \\\
#       In this case, the max area of water (blue section) the container can contain is 49.

# ---

# Pre notes:
#           This will be really hard if I choose to do anything better than quadratic time. gotta get that $$$
#           I'm going to solve it with quadratic really quick and come back later.


def maxAreaQuadratic(nums):
    # Local variables
    highestArea = -1

    for i in range(len(nums)):
        for j in range(len(nums)):
            # Find the width, aka the distance between the two NDXs
            width = abs(i - j) # abs to get absolute value

            # Height has to be the lower of the two "bucket edges" (containers) because the water can't slant
            if nums[i] > nums[j]:
                height = nums[j]
            else:
                height = nums[i]

            if height * width > highestArea:
                highestArea = height * width

    return highestArea

# Post notes:
#             That was wayyyy way too easy a solution. So I need to try a linear version.

# Pre notes:
#             I read through the discussions on leetCode for a bit of help here.
#             Basically we loop through with an L and an R and (obviously) a max value.
#             The idea is that if the left side is lower, than that's handicapping our R, and vice versa
#             So we push the lower height value towards the middle until they merge, and in doing this process we find\\
#                     A max value! Pretty ingenious isn't it!!!???

def maxAreaLinear(nums):
    left = 0
    right = len(nums) - 1
    highestArea = -1

    while left < right:
        widthDifference = abs(left - right)

        if nums[left] < nums[right]: # compare their heights
            highestArea = max(highestArea, widthDifference * nums[left]) # Choose between the prev.max and current area
            # Since left is smaller we increment it forwards
            left = left + 1
        else: #else if right is the smaller height value
            highestArea = max(highestArea, widthDifference * nums[right]) # Choose between the prev.max and current area
            # Since right is smaller we increment it backwards (decrement it? I guess?)
            right = right - 1

    return highestArea

# Post notes:
#            I'm so proud of myself!
#            I did use a discussion thread for inspiration for this post, but two things:
#                         1. I didn't read the whole thing
#                         2. I ended up doing it more efficiently than they did anyways!!!
#                                   Turns out they used a for loop alongside L and R values! \\
#                                                                               They made it unnecessarily complicated!
#                                   Even though mine was based on theirs, mine was more efficient! Feels so good!


def main():
    nums = [1,8,6,2,5,4,8,3,7]

    print(maxAreaQuadratic(nums))
    print(maxAreaLinear(nums))

main()