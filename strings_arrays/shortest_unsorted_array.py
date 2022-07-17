def shortest_unsorted_array(arr):
    '''
    Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

    ex:
    Input: [1, 2, 5, 3, 7, 10, 9, 12]
    Output: 5
    Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

    Input: [1, 3, 2, 0, -1, 7, 10]
    Output: 5
    Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
    '''
    # If empty array
    if not arr:
        return -1

    left = 0
    right = len(arr)
    while left < right and arr[left+1] > arr[left]:
        if arr[left+1]
        left += 1
        right -= 1
