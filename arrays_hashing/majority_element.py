def majority_element(arr):
    """
    Takes in array of sized n and returns the majority element
    Assuming that a majority element always exists in the array
    Majority element is greater than n/2 times 

    arr: [3,2,3] >> return 3 
         [3,2,2,2,3] >> return 2 

    Runtime: O(N)
    Space complexity: O(N)
    """
    assert arr  # Assuming that empty arrays are not valid

    counter = {}  # Initialize our counter dict

    # Iterate through array upto len(arr)
    for number in arr:
        # If arr[i] is not in the counter dict, we put it with a default value of 1
        if number not in counter:
            counter[number] = 1
        counter[number] += 1
    # print(counter)

    # Iterate through items to get key, value pairs
    for key, value in counter.items():
        if value > (len(arr) / 2):  # If value is greater than the len(arr) / 2 return key
            return key

    return -1  # If there is no majority element in array


arr = [3, 2, 5, 6, 7, 7, 7, 3]
print(majority_element(arr))
