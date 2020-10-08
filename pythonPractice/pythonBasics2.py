# Python Activtiy
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# Part A. char_exists
# Define a function char_exists(str,chr) that takes a string and a character
# and returns the number of times (count) this character appeared in the string.
# If the string is empty and the character is not in the string it should return zero
def char_exists(s, char):
    # YOUR CODE HERE
    count = 0

    if len(s) == 0:
        return count
    for i in range (0, len(s)): # for c in s: if c == char
        if s[i] == char:
            count +=1 # count = count + 1

    return count


# Part B. char_count
# Define a function char_count(str,chr) that takes a string and a character
# and returns the string after replacing all occurrences of this character with an underscore
def char_remove(s, char):
    # YOUR CODE HERE

    return
