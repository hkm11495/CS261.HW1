# Course: CS261 - Data Structures
# Student Name: Holly Murray
# Assignment: Homework 1 Problem 5
# Description: This program edits a string inputted from the user into individual words starting with
# capitalization (except for the first word) and concatenates them all into a string.


# returns length of a string
def length(input_string: str) -> int:
    """    TODO: Write this implementation    """
    count = 0
    for i in input_string:
        count +=1
    return count


# Receives original input string from the user and returns a clean version of it:
# 1) All english letters are lower case
# 2) All characters (other than letters ) are treated as word separators
# 3) All word separators are place by underscores
# 4) Duplicate word separators are removed
# 5) All leading and trailing word separators have been removed
def input_cleanup(input_string: str) -> str:
    """    TODO: Write this implementation    """
    s = list(input_string)
    strLength = length(input_string)
    i = 0
    # makes lower case
    while i < strLength:
        # convert to lower case if upper case
        if ord(s[i]) >= 65:
            if ord(s[i]) <= 90:
                s[i] = chr(ord(s[i]) + 32)

        # convert characters to underscore
        if ord(s[i]) < 97 or ord(s[i]) > 122:
            s[i] = '_'
            # check for duplicate underscores
            if i > 0 and strLength > 1:
                if s[i - 1] == '_':
                    s.pop(i)
                    strLength -= 1
                    i -= 1

        # check for leading underscores
        if i == 0:
            if ord(s[i]) == 95:
                s.pop(0)
                i -= 1
                strLength -= 1
                if strLength == 0:
                    return ""

        # check for trailing underscores
        if i == strLength - 1:
            if ord(s[i]) == 95:
                s.pop(strLength - 1)
                i -= 2
                strLength -= 1
                if strLength == 0:
                    return ""

        # increment i
        i += 1

    # Make list into string
    rString = ""

    for i in s:
        rString += i

    return rString


# This function verifies whether input string is clean and is ready for a camel case
# conversion if...
# 1) Input string contains only lowercase and underscores,
# 2) does not contain any duplicate underscore characters
# 3) does not contain any leading or trailing underscores
def is_clean_string(input_string: str) -> bool:
    """    TODO: Write this implementation    """
    if length(input_string) == 0:
        return True

    l = list(input_string)
    if l[0] =='_':
        return False
    if l[length(input_string)-1] == '_':
        return False

    i = 0
    # check for character and uppercase
    while i < length(input_string)-1:
        if ord(l[i]) < 97 or ord(l[i]) > 122:
            if ord(l[i]) != 95:
                return False

        # check for duplicate underscores
        if i > 0:
            if l[i] == '_' and l[i-1] =='_':
                return False

        i += 1
    return True


# This function accepts the original input string from user, as well as functions is_clean_string and input_clean.
# I then cleans up the original user string by calling func_cleanup. It will then...
# 1)
def camel_case(input_string: str, func_is_clean, func_cleanup):
    """    TODO: Write this implementation    """
    # sanitize input string
    clean_input = func_cleanup(input_string)    # DO NOT DELETE / CHANGE
    # check if input string is ready for camelCase conversion
    if not func_is_clean(clean_input):          # DO NOT DELETE / CHANGE
        return None                             # DO NOT DELETE / CHANGE
    # check that input string has at least two words in it
    # initialize elements
    l = list(clean_input)
    i = 1

    strLength = length(clean_input)
    twoWords = False

    # check if two words and change string list if two words
    while i < strLength - 2:
        if l[i] == '_':
            l[i + 1] = chr(ord(l[i + 1]) - 32)
            l.pop(i)
            i -= 1
            strLength -= 1
            twoWords = True
        i += 1

    # return None if it does not
    if twoWords == False:
        return None

    # convert clean input string into camelCase
    rString = ""

    for i in l:
        rString += i
    return rString

# BASIC TESTING

if __name__ == "__main__":
    if __name__ == "__main__":
        test_set = ("_random_ _word_provided",
                       "@$ptr*4con_", " ran  dom  word",
                       "example    word   ", "ANOTHER_Word",
                       "__", "_ _ _", "    ", "435%7_$$", "random")
       # example 1
        for test_string in test_set:
            result = input_cleanup(test_string)
            print(length(result), result)
        print()

        # example 2
        for test_string in test_set:
            result = input_cleanup(test_string)
            print(is_clean_string(test_string), is_clean_string(result))
        print()

        # example 3
        for test_string in test_set:
            result = camel_case(test_string, is_clean_string, input_cleanup)
            print("'" + test_string + "'", "-->", result)

