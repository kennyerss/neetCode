
def longest_sub(s):
    """
    Takes in a string s and returns the length of the longest substring without repeating characters

    ex:  s = "abcabcbb" >> returns 3 since "abc" is the longest substring without repeating characters
         s = "bbbbb" >> returns 1 since "b" can only be the substring without repeating characters
         s = "pwwkew" >> returns 3 since "wke" has length 3
        "abcabcbb"
        take a .... append b
        "ab" c ... is c in our string already? no... append c
        "abc" next is a... is a in our substring? yes then remove first a and now substring is "bca"
        >> Continuously update our max length of substring only when we don't have any duplicates

    Runtime: O(N) since we'll be traversing through all of the string
    Space: O(N) since maybe all of the characters in the string could be unique then we add them all to our set

   Sliding Window Method
    """

    left = 0
    charSet = set()  # Initialize set to keep duplicated elements
    max_length = 0

    for right in range(len(s)):
        # Checking in our set for duplicate elements
        # If duplicate element is found, remove it from the set and increment left pointer
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        # Update the max length using left and right pointers only when we know the substring does not have any duplicate elements
        max_length = max(max_length, right - left + 1)
    return max_length


t = "abcabcbb"
s = "pwwkew"
print(longest_sub(s))
print(longest_sub(t))
