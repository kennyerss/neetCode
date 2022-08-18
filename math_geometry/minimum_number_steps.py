def min_number_steps(num):
    '''
    Given integer num, return number of steps to reduce integer to zero

    If num is even, divide num by 2, otherwise subtract 1 

    Runtime
    '''
    total_steps = 0
    while num:
        if num % 2 == 0:
            num //= 2

        else:
            num -= 1

        total_steps += 1

    return total_steps


print(min_number_steps(123))
