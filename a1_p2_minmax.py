# Course: CS261 - Data Structures
# Student Name: Holly Murray
# Assignment: Homework 1 Problem 2
# Description: This program has a function that receives a one dimensional list of integers
# and returns a tuple with two values. If list is empty return (None, None)

def min_max(arr: []) -> ():
    """    TODO: Write this implementation    """
    # empty list
    if len(arr) == 0:
        return (None,None)

    # non empty list
    min_val = arr[0]
    max_val = arr[0]
    for x in arr:
        # Check for min value
        if x < min_val:
            min_val = x
        # Check for max value
        if x > max_val:
            max_val = x
    # return tuple if non empty list
    return (min_val,max_val)


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    print(min_max([1, 2, 3, 4, 5]))

    # example 2
    print(min_max([8, 7, 6, -5, 4]))

    # example 3
    print(min_max([]))