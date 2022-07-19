from collections import defaultdict
from pickletools import stringnl_noescape_pair
from tokenize import group


def group_anagrams(strs):
    '''
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    ex:
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        Input: strs = [""]
        Output: [[""]]

        Input: strs = ["a"]
        Output: [["a"]]

        Input: strs = ["bat", "tab", "kek"]
        Output: [["bat", "tab"], ["kek" ]]

    First create a defaultdict with list as default value

    Iterate through array
        Create count_arr for chars from 'a' to 'z' size 26 [0]
        for each string:
            Get char using ord function
            "eat" --> count_arr = [1, ... 1, ... 1] where 0th index is 'a' and 25th index is 'z'
            Append it to count_arr
        Using tuple(count_arr) we append the string that matches that count_arr

    return defaultdict.values()

    Runtime: O(m*n) where m is the length of our string array, and n is the average length of each string
    Space: O(m) 
    '''

    # Initialize our resulting dictionary with default input list (takes care of edge cases)
    result_dict = defaultdict(list)

    # Iterate through our string
    for word in strs:
        # Create a count_arr for our dictionary key from 'a' to 'z'
        count_arr = [0] * 26
        # For each word in our string, iterate through word and add to our count_arr its char count using ord function
        for char in word:
            count_arr[ord(char) - ord("a")] += 1
        # Convert count_arr into tuple so we can use it as our key for our dictionary and append the current word as its value
        result_dict[tuple(count_arr)].append(word)

    # Initialize resulting array
    result_array = []
    # Append each value in our result_dict.values()
    for val in result_dict.values():
        result_array.append(val)
    # Return result_array containing all grouped string anagrams
    return result_array
