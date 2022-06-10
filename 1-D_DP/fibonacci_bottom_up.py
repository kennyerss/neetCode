def fibonacci_bottom_up(n):
    """
    Takes in nth positive number and returns the nth term in the fibonacci sequence

    Start is 1,1
    Uses bottom-up approach DP with initialized array

    Input: n = 5 >> 1,1,2,3,5 >> return 5

    Initialize a 1-index array sized n+1 so that nth term of the fibonacci sequence is on the nth index of this array
    Set first and second index to be 1 if n equals 1 or n equals 2 

    Iterate through loop starting from index 3 to n+1:
        Increment each index to be plus each previous two terms

    Return 1-index array of index n 
    """
    assert n > 0  # Assuming only valid positive integers
    # Create array initialized to be None with length n+1
    bottom_up = [None] * (n+1)

    # Initialize first two terms
    bottom_up[1], bottom_up[2] = 1, 1

    for i in range(3, n+1):  # From index 3 to n+1
        # Update the current index of bottom_up array to be its previous term + the second previous term
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    # Return the value at index n of bottom_up array
    return bottom_up[n]


# Test cases
n = 100
print(fibonacci_bottom_up(n))
