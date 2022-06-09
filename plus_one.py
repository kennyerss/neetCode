
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
    # Pointer method
    last = len(digits) - 1

    while last >= 0:
        if digits[last] == 9:
            digits[last] = 0
        else:
            digits[last] += 1
            return digits
        last -= 1
    return [1] + digits

    # while last >= 0:  # [1, 0, 9]
    #     if digits[last] == 9:
    #         digits[last] = 0
    #         last -= 1
    #     digits[last] += 1
    # # digits[last] += 1
    # return digits


digits = [1, 9, 9, 9]
print(plus_one(digits))
