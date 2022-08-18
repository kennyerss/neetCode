
def max_frequency_arr(numbers):
    '''
    Given two arrays, numbers and q, find the freq of the maximum value of the 1-indexed array of number per index given in query
    Return the array of maximum values

    ex:
        numbers = [5,4,5,3,2]
        q = [1,2,3,4,5]

        return [2,1,1,1,1] since at the 1st index of q, from numbers[1] to numbers[5], the maximum value 5 occurs twice...repeats
        for all values in q

    Runtime: O(n) where n is the number of elements in numbers array
    Space: O(n) 
    '''
    n = len(numbers)
    res = [0] * n

    curr_max = numbers[n-1]
    count = 1
    res[n-1] = count

    # Iterate backwards
    for i in range(n - 2, -1, -1):
        # curr_max has changed, thus don't increment count
        if curr_max != max(numbers[i], curr_max):
            # Update the curr_max
            curr_max = max(numbers[i], curr_max)
            count += 0
        # Otherwise, if curr_max hasn't changed and is equal to the current index value, increment count by 1
        elif curr_max == max(numbers[i], curr_max) and curr_max == numbers[i]:
            count += 1

        res[i] = count

    return res
