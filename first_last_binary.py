
# Binary search with two pointers
# Runtime: O(logn) space: O(1)
# Split into two functions: finding the first... and finding the last indices

# Finding the first index
def firstIndex(arr, target):
    '''
    Going to find the first index of target in sorted array
    Return -1 if target is not found
    '''

    # Base case: If first index of array is equal to target return index
    if arr[0] == target:
        return 0
    # Two pointers: one for left and one for right
    left = 0
    right = len(arr) - 1

    # Take the mid-pointer... if mid == target AND mid-1 < target then return mid
    while left <= right:
        # Takes the floor division to get the mid pointer with also considering overflow
        mid = (left + right) // 2

        if arr[mid] == target and arr[mid-1] < target:
            return mid
        # If mid < target then left = mid+1
        elif arr[mid] < target:
            left = mid+1
        else:
            # If mid > target then right = mid-1
            right = mid-1
    # Return -1 if target not found
    return -1


# Finding the last index
def lastIndex(arr, target):
    """
    Takes in sorted array of integers and returns the last index of the target integer
    Returns -1 otherwise target not found
    """

    # Base case: If last index is equal to target then return last index
    if arr[-1] == target:
        return len(arr) - 1  # last index
    # Create two pointers: left (start of array) and right (end of array)
    left = 0
    right = len(arr) - 1
    # Iterate through array while left < right
    while left <= right:
        mid = (left + right) // 2  # Take the mid pointer

        # If arr[mid] == target and arr[mid+1] > target then return mid
        if arr[mid] == target and arr[mid+1] > target:
            return mid
        # else we increment right = mid - 1
        elif arr[mid] > target:
            right = mid-1
        # If arr[mid] < target:
        else:
            left = mid+1
    # Return -1 if target is not found
    return -1


def firstAndLast(arr, target):
    '''
    Takes in a sorted array and returns the first and last index of the target integer
    Returns [-1, -1] if target not in array

    ex: arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9] target = 5 >> [2, 6]
    '''

    # Base case: if first index is greater than target or last index less than target or input is an empty array then return [-1, -1]
    if arr[0] > target or arr[-1] < target or len(arr) == 0:
        return [-1, -1]

    start = firstIndex(arr, target)
    last = lastIndex(arr, target)
    return [start, last]


arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
target = 5
print(firstAndLast(arr, target))
