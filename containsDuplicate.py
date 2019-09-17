## Contains Duplicate
## Will Schick
## 9/17/2019

# Given an array of integers, find if the array contains any duplicates
# Your function should return true if any value appears at least twice in the array,
#                      return false if all values are distinct

# Will's note: I want to try this multiple ways

# ---

## This method uses a linear search to find our answer. The time complexity (I think!) is O(n^2), and is quadratic.
##      The reason this function is quadratic is because it loops through n for each element of n. Therefore N^2.
##                 E.G. With 3 elements, we loop three times for each element. 3^2. N^2.
def containsDuplicate(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            # Skip if they're the same index
            if i == j:
                continue
            elif numbers[i] == numbers[j]:
                print("Element", i, "and element", j, "have the identical value:", numbers[i])
                return True


    print("This array contains no duplicates! Yay!")
    return False

## This next method uses a sort and checks consecutive numbers
##       (Since we know duplicates will appear next to each other in a sorted list)
def containsDuplicateSort(numbers):
    # Make a copy of the list (In a real world scenario we might not want to sort the original list!)
    sortedNumbers = numbers.copy()

    #Sort our new list
    sortedNumbers.sort()

    # Loop through and check all consecutive elements (except the last to avoid index error)
    for i in range(len(sortedNumbers)-1):
        if sortedNumbers[i] == sortedNumbers[i+1]: # This i + 1 is the reason we check all elements except the last
            return True
    return False


def main():
    numb1 = [1,2,3,1]
    print("Scenario 1-----")
    print(containsDuplicate(numb1))
    print(containsDuplicateSort(numb1))
    print()

    numb1 = [1,2,3,4]
    print("Scenario 2-----")
    print(containsDuplicate(numb1))
    print(containsDuplicateSort(numb1))
    print()

    numb1 = [1,1,1,3,3,4,3,2,4,2]
    print("Scenario 3-----")
    print(containsDuplicate(numb1))
    print(containsDuplicateSort(numb1))
    print()

main()