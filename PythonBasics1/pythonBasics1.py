# Python Activtiy
# 
# Fill in the code for the functions below. 
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# Part A. starts_with
# Define a function starts_with(s, char) that takes a string and a character
# and returns true if the string starts with that character and false otherwise. 
def starts_with(s, char):
    if (len(s) > 0) & (len(char) > 0):
        if s[0] == char:
            return True
        else:
            return False
    if (len(s) == 0) & (len(char) == 0):
        return True
    else:
        return False


# Part B. starts_with_vowel
# Define a function starts_with_vowel(s) that takes a string and
# returns true if the string starts with a vowel and false otherwise. 
# For our purposes, a consonant is any letter other than A, E, I, O, U)
# Your solution should work for both upper and lower cases 
def starts_with_vowel(s):
    if len(s) > 0:
        if (s[0] in ('a', 'e', 'i', 'o', 'u')) | (s[0] in ('A', 'E', 'I', 'O', 'U')):
            return True
        else:
            return False
    else:
        return False

# Part C. max_min_sum
# Define a function max_min_sum(arr) that takes an array and returns the sum
# of the largest element and the smallest element of the array.
# For an empty array it should return zero
# For an array with just one element, it should return that element
def max_min_sum(arr):
    #check for empty array
    if len(arr) == 0:
        return 0

    # check for single element array
    if len(arr) == 1:
        return arr[0]

    # for array has 2 or more elements
    #get largest value
    maxNum = max(arr)

    #get smallest value
    minNum = min(arr)

    #add max and min
    return maxNum + minNum
