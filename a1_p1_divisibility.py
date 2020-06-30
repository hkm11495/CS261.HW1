# Course: CS261 - Data Structures
# Student Name: Holly Murray
# Assignment:Homework 1 Problem 1
# Description: This problem has a function that receives four integers (m,n,a,b) and for each number in the range (m,n inclusive)
#determines whether it is divisible by a, b, both, or neither. It then returns the result as a list of strings where eachs tring is a seperate list element.
# The numbers are processes in reverse order.
"""
Recieves: Recieves a string
Returns:  returns the length of the string you pass as argument to the function.

"""


def length(s: str) -> int:
    """
    TODO: Write this implementation
    """
    print('in function length')
    return 0


'''
Recieves: 4 integers
Returns: Returns the result as a list of strings, each string as separate list element
'''


# : associates various parts of a function with arbitrary python expressions at compile time.
def is_divisible(m: int, n: int, a: int, b: int) -> []:
    """
    TODO: Write this implementation
    """

    # Error Check

    if m > n:
        return 'Incorrect Input'
    elif a == b:
        return 'Incorrect Input'
    elif m < 1:
        return 'Incorrect Input'
    elif n < 1:
        return 'Incorrect Input'
    elif a < 1:
        return 'Incorrect Input'
    elif b < 1:
        return 'Incorrect Input'
    # No Error
    else:
        langs = []
        while n >= m:
            count = 0

            num = str(n)

            # divisible by a
            if n % a == 0:
                count = count + 1
                output = num + "\t" + "div by " + str(a)

            # divisible by b
            if n % b == 0:
                count = count + 1
                output = num + "\t" + "div by " + str(b)

            # format string
            if count == 2:
                output = num + "\t" + "both"

            if count == 0:
                output = num + "\t" + "none"
            n = n - 1
            langs.append(output)

    return langs


print(*is_divisible(2, 7, 2, 3), sep="\n")
print(is_divisible(1, 20, -1, 3))
print(is_divisible(20, 0, 100, 200))
print(is_divisible(10, 8, 7, 2))
print(is_divisible(3, 30, 7, 7))
