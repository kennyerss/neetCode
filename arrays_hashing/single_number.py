def single_number(nums):
    """
    Given a non-empty array of integers, find the element that appears only once

    ex: nums = [2, 2, 1] >> return 1 
        nums = [4, 1, 2, 1, 2] >> return 4

    Runtime: O(n) where n is the size of our array nums
    Space: O(n) since we're using an additional data structure
    """
    # Initialize our hash_map {key: counter}
    hash_map = {}
    # Iterate through our nums array
    for number in nums:
        # if our element is in the hash_map, increment by 1
        # otherwise, put in our hash_map
        hash_map[number] = hash_map.get(number, 0) + 1

    # Iterate key, counter in hash_map.items()
    for key, counter in hash_map.items():
        # Check if counter  == 1:
        if counter == 1:
            # return key
            return key


nums = [4, 1, 2, 1, 2]
print(single_number(nums))
