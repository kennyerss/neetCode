def product_array(arr):
    '''
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    ex:
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]

        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]

    Method:

    Use ouput_arr as our prefix and postfix array with multiple passes of input array
    prefix = 1 
    postfix = 1

    for i in range(len(nums)):
        curr_num = nums[i]
        out
        prefix *= nums[i]

    '''

    output_arr = []

    # Set default values of prefix and postfix to be 1
    prefix = 1
    postfix = 1

    # First pass: Get the prefix values into output_arr
    for i in range(len(arr)):
        curr_num = arr[i]
        # Append the prefix value of 1 to our array
        output_arr.append(prefix)
        # Multiply the prefix value by the current number
        prefix *= curr_num

    # Second pass: Get the postfix values and multiply with prefix values in output_arr
    for i in range(len(arr)-1, -1, -1):
        curr_num = arr[i]
        # Starting from last index of array, multiply the prefix of last index with postfix
        output_arr[i] *= postfix
        # Update our postfix to be multiplied by the last number seen
        postfix *= curr_num

    return output_arr
