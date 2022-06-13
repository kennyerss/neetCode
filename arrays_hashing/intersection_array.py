def intersection_of_two_arrays(nums1, nums2):
    """
    Given two integer arrays nums1 and nums2, return an array of their intersection. 
    Each element in the result must be unique and you may return the result in any order.

    ex: nums1 = [1,2,2,1], nums2 = [2,2] >> return [2]
        nums1 = [4,9,5], nums2 = [9,4,9,8,4] >> return [9,4] or [4,9] 

    Runtime: O(n+m) >> where n is the size of nums1 and m is the size of nums2 
    Space: O(n+m) >> creating additional data structures for both >> worst case would be if all the elements are unique 
    """
    # Assertion test cases
    assert len(nums1) > 0
    assert len(nums2) <= 1000

    # Initialize set
    hash_set = set()

    # Iterate through our nums1 and nums2 array and add it to our hash set
    for number in nums1:
        hash_set.add(number)
    for number in nums2:
        hash_set.add(number)

    result = []  # Initialize our result array to return

    # Iterate through our hash_set
    for number in hash_set:
        # If number is in both nums1 and nums2, append to our result array
        if (number in nums1) and (number in nums2):
            result.append(number)
    # Return our result array
    return result


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

print(intersection_of_two_arrays(nums1, nums2))
