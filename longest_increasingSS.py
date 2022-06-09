def longest_increasing_SS(arr):
    """
    Takes in an unsorted array of integers and returns the longest increasing subsequence 

    ex: [1,2,4,3] >> return 3 since [1,2,3] or [1,2,4] is our longest

    Using DP >> Runtime: O(n^2) with O(n) space

    Method is to first store our LIS (longest increasing subsequence) with 1 times the len of the arr 

    Iterate through array backwards
        Iterate through each element greater than current up to the len of array
            if next > curr 
                find max of curr and next 
                append to our LIS array
    return the max of LIS 
    """
    assert arr
    # Use array LIS to store the maximum subsequence per index of our original array
    LIS = [1] * len(arr)

    for i in range(len(arr)-1, -1, -1):  # Iterate through array backwards
        for j in range(i+1, len(arr)):  # Iterate from i+1 upto the len(arr)
            if arr[i] < arr[j]:  # Check if the curr index is less than the index greater than it
                # Two choices... set max of itself or the max of next index
                LIS[i] = max(LIS[i], 1 + LIS[j])
    # Otherwise just return the max of the LIS array
    return max(LIS)


# Test cases
arr = [1]
print(longest_increasing_SS(arr))
