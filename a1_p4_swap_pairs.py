# Course: CS261 - Data Structures
# Student Name: Holly Murray
# Assignment: 1 Problem 4
# Description: This receives a 1D list of integers and returns a new list the same length where pairs of
# elements are swapped. The original list is not changed.

def swap_pairs(arr: []) -> []:
# """  ODO: Write this implementation    """
    list1 = []
    i = 0

    while i < len(arr):
        if i +1 < len(arr):
            list1.append(arr[i + 1])
        list1.append(arr[i])
        i = i+2
    return list1


# BASIC TESTING
if __name__ == "__main__":
# example 1
    print(swap_pairs([1, 2, 3, 4, 5]))
# example 2
    print(swap_pairs([8, 7, 6, -5, 4, 10]))
# example 3
    print(swap_pairs([]))
