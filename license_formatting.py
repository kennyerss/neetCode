from hashlib import new
from unittest import result


def license_formatting(s, k):
    '''
    Given a string containing alphanumeric characters and dashes, return the reformatted license key where each group of strings contain exactly k characters
    The first group can contain shorter characters but must contain at least one character.

    ex:
    Input: s = "5F3Z-2e-9-w", k = 4
    Output: "5F3Z-2E9W"

    Input: s = "2-5g-3-J", k = 2
    Output: "2-5G-3J"
    '''
    string_arr = s.split('-')
    print(string_arr)

    new_string = "".join(string_arr)
    new_string = new_string.upper()
    print(new_string)

    result_string = ""
    count = 0
    for i in range(len(new_string)-1, -1, -1):
        if count == k:
            result_string = "-" + result_string
            count = 0

        result_string = new_string[i] + result_string
        count += 1

    return(result_string)


s, k = "2-5g-3-J", 2
print(license_formatting(s, k))
