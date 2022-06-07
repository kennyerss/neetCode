def fibonacci(n):
    '''
    Given integer n, print nth terms in the Fibonacci sequence assuming n > 0
    
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8... 

    Test cases: 5 >> 0, 1, 1, 2, 3 
                2 >> 0, 1
                7 >> 0, 1, 1, 2, 3, 5, 8
    '''

    # Recursive solution

    # Base case: if we get 1, return 0
    if n == 1:
        return 0
    # Second base case: If we get 2, return 1
    elif n == 2:
        return 1
    # Recursive step:
    else:
        # f(n+1) = f(n) + f(n-1)
        return fibonacci(n-1) + fibonacci(n-2)

n1 = 5  
n2 = 2
n3 = 7

