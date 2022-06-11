def permutations(nums):
    """
    Takes in an array nums and n number of objects and returns all the possible ways of ordering the array

    ex: nums = [1,2,3] >> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
                       >> [1] >> pop off 1 
                       >> [2,3] >> permute until len is 1 
                       >> [2] [1,3] >> 
        nums = [0,1] >> [[0,1], [1,0]]

        nums = [1] >> [[1]]

        Can the elements of this array be duplicates? Negative? What would happen if we pass in an empty array?

        Using backtracking with recursion
        Runtime: O(Nlogn)
        Space: O(N)
    """
    # Base cases
    if not nums:
        return []
    if len(nums) == 1:
        # instead of nums.copy() we just return nums[:] index of whole
        return [nums[:]]

    result = []  # Result array to store all our permutations
    # Iterate through len of nums
    for num in range(len(nums)):
        # Pop off the first index
        start = nums.pop(0)
        # Store permutations with rest of array
        perms = permutations(nums)
        # Iterate through perms array to append our first index
        for iteration in perms:
            # Append our first index to end of array
            iteration.append(start)
        # Extend nums to add in our permutations that we got
        result.extend(perms)
        # Update our array nums to append the first index at the end
        nums.append(start)
    # Return our result once we have found all our permutations
    return result


nums = [1, 2, 3]
print(permutations(nums))
