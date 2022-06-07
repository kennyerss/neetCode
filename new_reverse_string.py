def reverseString(string):

    '''
    Takes in a string and returns reversed string 

    Uses two pointer method with runtime O(N) and memory O(N)
    '''

    # Convert string into array
    string = list(string)

    # Create two pointers: one on the left and one on the right (end of array)
    left = 0
    right = len(string)-1

    # Iterate through string array while left pointer is less than right
    while left < right:

        # Swap each character with left and right index
        string[left], string[right] = string[right], string[left]
        # Shift left and right pointer towards middle  
        left, right = left+1, right-1
    # Return the array joining ""
    return "".join(string)


string = "hello"
print(reverseString(string))