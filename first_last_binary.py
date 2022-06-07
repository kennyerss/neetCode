
# Binary search with two pointers
# Runtime: O(logn) space: O(1)
# Split into two functions: finding the first... and finding the last indices

# Finding the first index
# Base case: If first index of array is equal to target return index
# Two pointers: one for left and one for right
# Take the mid-pointer... if mid == target AND mid-1 < target then return mid
# If mid < target then left = mid
# If mid > target then right = mid
# Return -1 if target not found

from tkinter import W


def firstIndex(arr, target):
    '''
    Going to find the first index of target in sorted array
    Return -1 if target is not found
    '''

    if arr[0] == target:
        return 0

    left = 0
    right = len(arr) - 1

    while left <= right:
        # Takes the floor division to get the mid pointer with also considering overflow
        mid = (left + right) // 2

        if arr[mid] == target and arr[mid-1] < target:
            return mid

        elif arr[mid] < target:
            left = mid+1

        else:
            right = mid-1

    return -1


# Finding the last index
# Base case: If last index is equal to target then return last index
# Create two pointers: left (start of array) and right (end of array)
# Iterate through array while left < right
# Take the mid pointer
# If arr[mid] == target and arr[mid+1] > target then return mid
# If arr[mid] < target:
#     left = mid + 1
# else we increment right = mid - 1


def lastIndex(arr, target):

    # Takes in sorted array of integers and returns the last index of the target integer
    # Returns -1 otherwise target not found

    if arr[-1] == target:
        return len(arr) - 1  # last index

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target and arr[mid+1] > target:
            return mid

        elif arr[mid] > target:
            right = mid-1

        else:
            left = mid+1
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
