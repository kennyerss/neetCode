def even_fibonacci():
    """
    Takes in n number of Fibonacci sequence and returns total sum of even-valued terms
    Starts with 1 and 2 
    ex: n = 6 >> 1, 2, 3, 5, 8, 13... >> returns 10
        n = 5 >> 1, 2, 3, 5, 8 >> returns 10
        n = 4 >> 1, 2, 3, 5 >> returns 2
        n = 3 >> 1, 2, 3 >> returns 2
        n = 2 >> 1, 2 >> returns 2 
        n = 1 >> 1  >> returns 0
    """
    fib1 = 1
    fib2 = 2
    total_sum = 0

    while fib2 < 4000000:
        if fib2 % 2 == 0:
            total_sum += fib2

        fib1, fib2 = fib2, fib1+fib2

    return total_sum


print(even_fibonacci())
