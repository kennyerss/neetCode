def maximum_subarray(arr, k):
    '''
    Given an array of positive integers and a positive k, return the maximum sum of the subarray of sized k
    Otherwise return -1 if not possible

    ex: [2,3,5], k=2 >> return 8
        [2,3,5], k=3, >> return 10
        [2,3,5], k=4 >> return -1
    '''

    # First compute the initial window size k sum
    max_sum = 0
    for i in range(k):
        max_sum += arr[i]

    # Create current sum variable to store new sums when window size exceeds k
    curr_sum = max_sum

    # Start from k upto the length of the array
    for i in range(k, len(arr)):
        # Everytime window size exceeds, we're going to add the new element to our current sum and subtract the last element in our window
        curr_sum += arr[i] - arr[i-k]
        # Update the max_sum by taking the max of the max_sum with the curr_sum
        max_sum = max(max_sum, curr_sum)

    return max_sum


arr = [3, 5, 2]
k = 1

print(maximum_subarray(arr, k))
