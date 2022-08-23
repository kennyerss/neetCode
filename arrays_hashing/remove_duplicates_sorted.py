from turtle import left


def remove_duplicates(arr):
    '''
    Given a sorted array of integers, return the number of valid elements of the array once duplicate elements are removed

    ex:
       arr = [2,3,5,5,7,11] >> return 5 since (2,3,5,7,11)
       arr = [2,2,2,3] >> return 2 since (2,3)
    '''
    if not arr:
        return []

    left_index = 1

    # Iterate through array by moving one element at a time
    for i in range(1, len(arr)):
        # If unique element found, put unique element where write_index is currently at
        if arr[i-1] != arr[i]:
            arr[left_index] = arr[i]
            left_index += 1

    return left_index


arr = [2, 3, 3, 4]
print(remove_duplicates(arr))
