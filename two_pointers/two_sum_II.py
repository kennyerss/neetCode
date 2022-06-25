def two_sum(numbers, target):
    """
    Given a 1-index array of integers numbers that is sorted in non-decreasing order, 
    find the two numbers such that they add up to a specific target integer. 

    Return the indices of the two numbers added by one as an integer array of length 2.

    Assume that all elements are distinct and there is exactly one solution. 

    ex: numbers = [2,7,11,15], target = 9 -> return [1,2] since 2 + 7 == 9
        numbers = [2,3,4], target = 6 -> return [1,3] since 2
        numbers = [-1,0], target = -1 -> return [1,2] since -1 + 0 == -1

    Since array is sorted, we can use binary search to find our two indices

    Runtime: O(n)
    Space: O(1)
    """
    # Two pointers of 1-indexed array
    left = 0
    right = len(numbers) - 1
    # Iterate through array while left + right != target
    while left < right:
        total_sum = numbers[left] + numbers[right]
        # Return indices once total_sum is equal to our target
        if total_sum == target:
            return [left + 1, right + 1]
        # If total_sum is more than the target, decrement right pointer
        if total_sum > target:
            right -= 1
        # If total_sum is less than the target, increment left pointer
        if total_sum < target:
            left += 1


numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))
