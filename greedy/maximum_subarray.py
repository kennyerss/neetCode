def maximumSubArray(array):
    '''
    Parameters:
        List of integer array NONEMPTY
    Returns:
        Maximum sum you can get from a contiguous sub array
    '''

    # Using Kadane's Algorithm
    # Runtime O(n) and memory space O(n)
    max_sub = array[0]
    curr_sum = 0

    for num in array:
        if curr_sum < 0:
            curr_sum = 0 # Set the current sum back to 0 if the sum is negative
        # Otherwise you increment the curr_sum with the current num
        curr_sum += num
        # Update the max of the max_sub array with the curr_sum
        max_sub = max(max_sub, curr_sum)

    return max_sub
