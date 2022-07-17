def longest_sequence(arr):
    '''
    Takes in an unsorted array and returns the longest sequence in the array

    ex:
        Input: nums = [100,4,200,1,3,2]
        Output: 4

        Input: nums = [0,3,7,2,5,8,4,6,0,1]
        Output: 9

    Create a hash set so that our number array are ordered with O(1) lookup
    Initialize max sequence = 0

    Iterate through arr:
        Check if val in arr has a left neighbor (our starting point of sequence)
            Initialize length = 0
            while (val + length) in hash set:
                length += 1
            Update max sequence

    Runtime: O(n)
    Space: O(n)
    '''

    # Create hash set
    hash_set = set(arr)

    # Result sequence
    longest_sequence = 0

    for value in arr:
        # Check if we have a starting index for a sequence
        if (value-1) not in hash_set:
            length = 0
            while (value + length) in hash_set:
                length += 1
            # Update our longest_sequence potentially finding our max length
            longest_sequence = max(length, longest_sequence)

    # Return our longest sequence of our array
    return longest_sequence
