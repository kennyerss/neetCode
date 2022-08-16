

# Implementation of quicksort algorithm
# O(nlogn) runtime worst being O(n^2)
# In-place algorithm so no extra space needed but O(n) space for recursive stack call
def quicksort(arr, start, end):
    '''
    Sort an array using quicksort algorithm
    '''
    # If we have nothing to sort on either side
    if start >= end:
        return
    # Get partition index
    partition_index = partition(arr, start, end)
    # Quicksort again for left side
    quicksort(arr, start, partition_index-1)
    # Quicksort again for right side
    quicksort(arr, partition_index+1, end)

    return arr


def partition(arr, start, end):
    '''
    Partition an array into two halves with a pivot and returns the partition index
    '''
    # Choose end element as pivot
    pivot = arr[end]
    partition_index = start
    for i in range(start, end):
        if arr[i] <= pivot:
            swap(arr, i, partition_index)
            partition_index += 1

    # At the end of partitioning, swap the partition index with the end pivot
    swap(arr, partition_index, end)
    return partition_index


def swap(arr, i, j):
    '''
    Swap two elements, i and j, in an array 
    '''
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


arr = [3, 1, 6, 2, 4, 9, -1]
start = 0
end = len(arr)-1

print(quicksort(arr, start, end))
