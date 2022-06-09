
def kth_frequency(arr, k):
    """
    Takes in an array of integers and k input
    Return the value in array which appears with a frequency of k 
    """
    # Map the array so that we implement a counter for each value
    # Iterate through array so that we add it to our dictionary
    # element: counter
    # Increment by one to element when we find it again
    # Return element in dictionary whose value is equal to k

    counter = {}

    for num in range(len(arr)):
        if arr[num] not in counter:
            counter[arr[num]] = 1
        counter[arr[num]] += 1

    for key, value in counter.items():
        if value == k:
            return key

    return None


arr = [8, 7, 9, 6, 7, 5, 1]
k = 2
print(kth_frequency(arr, k))
