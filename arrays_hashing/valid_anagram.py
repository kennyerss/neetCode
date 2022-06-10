def is_anagram(self, s: str, t: str) -> bool:

    if len(s) != len(t):  # Base case
        return False

    countS, countT = {}, {}  # letter: count
    for i in range(len(s)):
        # increments 1 everytime the index is found
        # s[i] is the letter, incrementing the count by 1 each time key is found
        # (s[i], 0) is default value 0
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    if countS != countT:
        return False
    return True

    for c in countS:
        # checks if each key-value pair of countS is equal to countT
        if countS[c] != countT.get(c, 0):
            return False
    return True

    # solution with O(1) memory --> sort the strings first and then they'll be
    # the exact same string

    # return Sorted(s) == Sorted(t)
    # Otherwise create own sorting algorithm
