def top_k_frequent(nums, k):
    """
    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
    Guaranteed that the answer is unique
    ex:     
        nums = [1,1,1,2,2,3], k = 2 >> [1,2]
            Step1 = {1: 3, 2: 2, 3:1} 
            Step2 = get max and key >> 1 
            Step3: pop key 1 and now map should just be {2:2, 3:1}
            Step4: Get max again... 2... now we have sufficed k == 2 

        nums = [1], k = 1 >> [1]

    BUCKET SORT WITH HASHING
    Runtime: O(n) 
    Space: O(n) 

    HashMap the elements in our array to get counter >> Space: O(N)
    Iterate through key, values in map.items() to check the first max if k == 1
    if k > 1 then we pop out the max value from our map and then update to also return our next max index up until we get to k
    """
    assert k > 0

    counter = {}  # Hashmap to store counter for each element
    # Putting all the frequency of each element in its own array as a 1-index array
    frequency = [[] for i in range(len(nums)+1)]

    for element in nums:
        # Using get method, we can easily set a default value 0 otherwise increment by 1 if the key exists in our dict counter
        counter[element] = counter.get(element, 0) + 1

    # counter = {1: 3, 2: 2, 3: 1}
    for key, value in counter.items():
        # Store value as the index of frequency array with the value being its key
        frequency[value].append(key)

    result = []  # Initialize array into result variable
    # Iterate through the frequency array backwards to get the top K elements upto 0
    for i in range(len(frequency) - 1, 0, -1):
        # For each index of our frequency array, we're going to go through and append the element assuming the index is non-empty
        for count in frequency[i]:
            result.append(count)
            # Stop appending to result once the length of result matches the k value input
            if len(result) == k:
                return result  # Return result once match is found


arr = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(arr, k))
