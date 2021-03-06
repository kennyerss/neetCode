
import re


def reverse_string(string):
    '''
    Takes in input string and reverse it ... 
    Return reversed string 

    ex: "hello" --> "olleh"

    Runtime: O(n)
    Memory: O(n)
    '''

    # String concatenation... initialize empty string
    reversed_string = ""

    # Iterate over input string starting from last index all the way to our first index
    # Second parameter to range is non-inclusive, so have to go to -1 instead of 0
    for char in range(len(string) - 1, - 1, -1):
        reversed_string = reversed_string + string[char]
    return reversed_string


string = "hello"
reversed = reverse_string(string)
print(reversed)
