def kth_Largest(arr, k):
    '''
    Given array of integers and an integer k, find the kth largest element

    ex: arr = [1, 6, 2, 5, 3] k = 4 >> return 5

    U >> Can we have negative numbers in our array? 
         Will there always be a valid kth integer (as in will k not exceed len(arr)) >> 
         Are duplicate numbers in this array possible? >> Yes
         Is this array sorted/unsorted? >> Unsorted
         Are we returning the kth largest element? >> Yes

    test cases:
        arr = [2,6,7,7,9] k = 4 >> return 6
    '''
