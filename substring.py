
def substring(big_string, sub) -> bool:
    '''
    Takes in two parameters:
        String and sub... return True if sub is a substring of big_string

    ex: "laboratory" and "rat"... return True since rat is a substring of laboratory

    Runtime: O(n*m) length of first string * length of second string
    Memory: O(1)
    '''

    # Base case if substring is greater than the length of original string then return False
    # Either greater than the length of big_string or sub is empty
    if len(sub) > len(big_string) or len(sub) < 1:
        return False

    # Two pointers
    left = 0
    right = len(sub)

    # Indexing method
    while right <= len(big_string) - 1:

        if big_string[left:right] == sub:
            return True

        # Increment left and right pointers
        left += 1
        right += 1

    return False


big_string, sub = "laboratory", "rat"
result = substring(big_string, sub)
print(result)
