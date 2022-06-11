def sumOfTwoArrays(arr1, arr2, target):
    '''
    Takes in two arrays and finds the index of the pair with the nearest sum
    arr1 = [-1, 3, 8, 2, 9, 5]
    arr2 = [4, 1, 2, 10, 5, 20]
    target = 24
    '''
    # Understand >> brute force would be just comparing each pair of numbers in both arrays if it equals or close to 24
    # Match >> Use a hashtable to get the difference value of the number in first array
    # Plan >> First we could hash the first array with the difference and then traverse through second array if it equals to target

    hashMap = {}
    # Hash first array
    for num in arr1:
        difference = target - num

        hashMap[num] = difference
    # Iterate through second array
    # for num in arr2:
    #     if
