def first_and_last(arr, target):
    '''
    Take in a sorted array of integers and return the first and last index of integer target
    Return [-1,-1] if target cannot be found 

    ex: arr = [2,4,5,5,5,5,5,7,9,9] target = 5
        return [2,6]

        else if target = 3
        return [-1,1]
    '''
    # Runtime: O(n) Memory: O(1)
    # Two pointer method

    # Have a left and right pointer since the array is sorted

    # If either pointer is less than or greater than... we can shift the pointer up until either both pointers are
    # equal to the target

    # Then return pointer indices

    # Base case if array is empty, or if first element is greater than target or if last element is less than target
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]

    else:
        left = 0
        right = len(arr) - 1

        while left <= right:
            if arr[left] < target:
                left += 1

            if arr[right] > target:
                right -= 1

            if arr[left] and arr[right] == target:
                return [left, right]

        return [-1, -1]


arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
target = 5
print(first_and_last(arr, target))
