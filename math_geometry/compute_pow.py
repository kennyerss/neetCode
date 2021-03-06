
def compute_pow(x, y):
    '''
    Takes in a double x and integer y and computes x to the power of y 

    ex: 1.1^2 >> 1.21

    Brute force: 1.1^21 by multiplying 1.1 21 times ... which takes a long time 

    Optimized approach: Recursive algorithm
        - Powers of 2: Iterated squaring 
            ex: x^8 = (x^4)^2
        - Powers of 10: (x^y/2)^2
            ex: x^10 = (x^5)^2
        - Change power y to -y and double x to 1/x when y is negative
    '''
    # Recursively is to do modular exponentiation
    # Runtime: O(logn) where n is the exponent and Space: O(1)
    # Base case if y==0 or y==1 or y is negative
    if y == 0:
        return 1
    if y == 1:
        return x
    if y == -1:
        return 1/x

    # Store result being the floor integer of the exponent
    result = compute_pow(x, y//2)

    # Recursive call
    return result * result * (x if y % 2 else 1)

    # # Initialize result and power
    # result, power = 1.0, y

    # # Change power and result if y is negative
    # if power < 0:
    #     x, power = 1.0/x, -y

    # # Iterate while power
    # while power:
    #     # Base case
    #     if power & 1:  # Think of power exponent in binary
    #         result = result * x
    #     # Otherwise, you multiply x by itself and right shift the power
    #     x, power = x * x, power >> 1
    # return result


print(compute_pow(2.5, 2))
print(compute_pow(2.5, 6))
