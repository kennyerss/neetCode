def roman_to_int(roman):
    """
    Takes in string roman number and returns roman number into integer
    s = "III" >> 3 >> I*3 = 3
    s = "LVIII" >> 58 >> L = 50, V = 5, III = 3
    s = "IV" >> 4 >> V - I = 4

    Runtime: O(N) 
    Space: O(1)
    """
    # Hashmap problem
    # Map out the values of roman symbols to int
    # map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, M: '1000'}
    # result = 0
    # Symbol: Int
    # for symbol in range(len(roman), -1)
    # if symbol > roman[smh]
    # subtract

    assert roman  # Base case we have valid input
    result = 0
    roman_int = {"I": 1, "V": 5, "X": 10,
                 "L": 50, "C": 100, "D": 500, "M": 1000}
    # IV >>

    for i in range(len(roman)):
        # Make sure that i+1 stays in bound of len of the string
        # If value next is greater than the current, subtract from result
        if i+1 < len(roman) and roman_int[roman[i]] < roman_int[roman[i+1]]:
            result -= roman_int[roman[i+1]]
        # Other wise add to result
        result += roman_int[roman[i]]
    # Return result once string has been traversed
    return result


roman = 'LVIII'
print(roman_to_int(roman))
