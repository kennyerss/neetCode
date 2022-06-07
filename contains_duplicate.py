def contains_duplicate(self, nums: List[int]) -> bool:
    # Create a hashset
    # Runtime: O(n)
    # Space complexity: O(n)
    hashSet = set()
    for i in nums:
        if i in hashSet:
            return True
        hashSet.add(i)

    return False

    '''
        Second solution
        Runtime and space complexity: O(n)
        Convert list to set and compare length

        numSet = set(nums)
        if len(numSet) == len(nums):
            return False
        return True
        '''
