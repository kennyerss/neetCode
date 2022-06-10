def binary_search(arr, target):
    """
    Takes in a sorted array and returns the index of the target

    ex: input = [-1,0,3,5,9,12] target = 9 >> output = 4 since 9 is at index 4 
        input = [-1,9,2] target = 4 >> output: -1 since 4 is not in our array

    Runtime: O(logn) where n is the size of our array
    Space: O(1)
    """
    # Initialize our two pointers for our binary search algorithm
    left, right = 0, len(arr) - 1
    # Iterate while left <= right:
    while left <= right:
        # Take our mid pointer
        # Since (left + right)  // 2 can lead to overflow when size of our array is really big
        mid = left + ((right-left) // 2)

        if arr[mid] < target:  # If mid value in arr is less than target, search through right side of our array
            # Set left pointer equal to mid+1
            left = mid+1
        # If mid value is greater than the target, then we search through the left side of array
        elif arr[mid] > target:
            # Set right pointer equal to mid-1
            right = mid - 1
        else:
            return mid  # Return mid pointer once we've found our mid == target

    return -1  # Otherwise if target is not in our array, return -1


arr, target = [-1, 0, 3, 5, 9, 12], 9

print(binary_search(arr, target))
