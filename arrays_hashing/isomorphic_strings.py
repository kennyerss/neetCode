
def isomorphic_strings(s, t):
    """
    Given two strings s and t which can be valid strings containing ASCII characters
    Return True if the strings are isomorphic, otherwise False

    ex: s = "add" t = "tbb" -> return True 
        s = "foo" t = "bar" -> return False since two o's in s cannot make the "ar" in t 

    Brute force -> nested for loops which would take O(n^2) runtime with O(1) space complexity
    Hashing Method -> O(n) runtime with O(n) space complexity where n is the length of the string

    """
    # Base cases
    # if not s return False
    if not s:
        return False
    #  if length of input strings are of different length, then we return False
    if len(s) != len(t):
        return False
    # Create map {s:t} to map from s to t
    map = {}
    # Iterate through length of s
    for i in range(len(s)):
        char1 = s[i]
        char2 = t[i]
        # Check if char1 is in the map
        if char1 in map:
            # If in map but different value -> return False
            if map[char1] != char2:
                return False
        # Put in map
        map[char1] = char2
    # Return True at the end
    return True


s, t = "add", "tbb"
print(isomorphic_strings(s, t))

u, v = "foo", "bar"
print(isomorphic_strings(u, v))
