
def plus_one(digits):
    """
    Given an integer array digits, where each digits[i] is the ith digit of the integer
    Return the resulting array of digits after adding one to its least significant digit in the array
    No leading zero's in the largest integer

    ex: [1,2,3] >> [1,2,4] since 123 + 1 = 124
        100 + 20 + 3 + 4 >> 124

        [9] >> [1,0] since 9+1 = 10
        9 + 1 = 0
        [1,0,9] >> [1,1,0] since 109+1 = 110
        100 + 00 + 9 + 1 >> 100 + 1 + 0
        [1,9,9,9] >> [2,0,0,0] since 1999+1 = 2000

    Runtime: O(N)
    Space: O(1)
    """
    # First add 1 to end of array
    digits[-1] += 1

    # Loop starting from end of array and change current value if digits[i] + 1 is equal to 10
    for i in range(len(digits)-1, -1, -1):
        if digits[i] != 10:
            break
        else:
            # If digits + 1 == 10, then make current value to 0 and add 1 to the left index of current index
            digits[i] = 0
            digits[i-1] += 1
    else:  # After looping, get the we have a 10 in the first index of array
        # Make first index value be 1 and then just append 0 to end of array
        digits[0] = 1
        digits.append(1)

    return digits


digits = [1, 2, 9]
print(plus_one(digits))
