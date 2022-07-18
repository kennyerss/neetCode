from enum import unique


def first_unique(input_string):
    '''
    Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

    ex: "leetcode", return 0
        "loveleetcode", return 2
        "keek", return -1
        "abc", return 0
        "aabc", return 2

    Pattern:
        - Finding the "unique" element --> hashing

    Runtime: O(n) where n is the length of the string
    Space: O(n)

    '''
    # Store char: count
    letter_table = {}

    # Fill our hash table
    for char in input_string:
        letter_table[char] = letter_table.get(char, 0) + 1

    # Iterate through the length of input_string
    for i in range(len(input_string)):
        letter = input_string[i]
        # Once we find a letter with a count of 1, return its index
        if letter_table[letter] == 1:
            return i
    # Otherwise, if we can't find any unique elements, return -1
    return -1
