
def DNA_substring(input_string):
    """
    Find all 10-letter-long sequences that occur more than once in a DNA molecule

    ex: input_string = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT" 
    Runtime: O(n) where n is length of our string
    Space: O(n) since additional data structure is created
    """
    # Use sliding window and hash_map
    # Initialize hash_map
    hash_map = {}
    # Set left pointer and right pointers for length 10-sized substring
    left, right = 0, 10
    # Iterate through our string
    while right < len(input_string):
        # For each 10-letter substring... put it in our map
        # If it already exists, increment counter by 1
        substring = input_string[left:right]
        hash_map[substring] = hash_map.get(substring, 0) + 1
        left += 1
        right += 1

    # Initialize result array
    result = []
    # Iterate key, value in hash_map.items():
    for key, count in hash_map.items():
        # If count > 1:
        if count > 1:
            result.append(key)
    # Return result array
    return result


old_string = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(DNA_substring(old_string))
input_string = "TGTTCCAGGCCTAGTTCCAGGCCTTTCCAG"
print(DNA_substring(input_string))
