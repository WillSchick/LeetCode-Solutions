## Will Schick
## 9/15/2019
## LeetCode: Two Sum

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have EXACTLY one solution, and that you may not use the same element twice.

# ---

def twoSum(numbers, target):
    # Loop through our numbers twice
    for i in numbers:
        for j in numbers:
            # If they add up, return them
            if i + j == target:
                # We need to make sure that they aren't the same element.
                i = numbers.index(i)
                j = numbers.index(j)

                if i != j:
                    return [i, j]


def main():
    givenNums = [0, 88, 4, 2, 6, 11, 15]
    target = 8

    print(twoSum(givenNums, target))

main()
