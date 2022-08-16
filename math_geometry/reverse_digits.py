
def reverse_digits(number):
    '''
    Given an integer number, reverse its digits

    ex:
        42 -> 24
        -312 -> -213

    '''
    # Create result and make a temporary number with absolute value
    result, tmp_number = 0, abs(number)

    # Loop while valid tmp_number
    while tmp_number:
        # Update our result to be multiplied by 10 while adding the least significant digit to result
        result = result * 10 + tmp_number % 10
        # Update tmp_number to be floor divided by 10
        tmp_number //= 10

    # Return negative result if number is negative, otherwise return result
    return result * -1 if number < 0 else result


number = -312
print(reverse_digits(number))
