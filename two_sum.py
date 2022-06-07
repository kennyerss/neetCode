def two_sum(self, nums: List[int], target: int) -> List[int]:
    # Optimized solution
    # Create HashMap dict
    sumMap = {}  # value: index
    for index, value in enumerate(nums):
        difference = target - value
        if difference in sumMap:
            return [sumMap[difference], index]
        # Update the dictionary to map value with index
        sumMap[value] = index
