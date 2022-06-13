
def sparse_search(target_string, arr):
    """
    Given a sorted array of strings that is interpersed with empty strings. 
    Write a method to find the location of a given string.

    ex: Input: “ball”, ["at", "", "", "", "ball", "car", "dad", ""]
        Output: 4 

        Input: "ball", ["", "", "", "", "", ""]
        Output: -1 

        Input: "ball", ["", "", "", "", "ball"]
        Output: 4

        Input: "ball", ["ball", "", "", "", ""]
        Output: 0

        Input: "ball", ["arrow", "ball", ""]
        Output: 1

        Input: "ball", ["ball", "cat", "cattack"]

        for i in array:
            if array[i] == target_string:
                return i

        Runtime: O(logn) Space: O(1)
    """
    # Helper function
    def find_nonempty_mid(target_string, arr):
        """
        Takes in array and finds the first non-empty mid-pointer
        """
        mid_pointer = len(arr) // 2
        distance_from_mid = 1

        check = True
        while check:
            # Initialize left and right pointers from mid_pointer
            left_of_mid = mid_pointer - distance_from_mid
            right_of_mid = mid_pointer + distance_from_mid

            # Checks if our mid_pointer is equal to our target_string
            if arr[mid_pointer] == target_string:
                check = False
                return mid_pointer

            # If mid_pointer is not equal to target_string, we check both sides of the mid_pointer
            # Keep track whether or not distance pointers are in bound of our array
            if left_of_mid >= 0 and arr[left_of_mid] != "":
                return left_of_mid

            if right_of_mid < len(arr) and arr[right_of_mid] != "":
                return right_of_mid

            # If distance has been maximized, meaning that the distance is at most equal to half the size of our array
            # set check boolean to False and return -1
            if distance_from_mid >= len(arr) / 2:
                check = False
                return -1
            # Otherwise, keep incrementing our distance
            distance_from_mid += 1

    # Binary Search Algorithm
    left, right = 0, len(arr) - 1
    while left <= right:
        # Get our non_empty mid_pointer
        mid_pointer = find_nonempty_mid(target_string, arr)

        # Element at mid_pointer is less than target_string, search the right side of the array
        if arr[mid_pointer] < target_string:
            left = mid_pointer + 1

        # If element at mid_pointer is greater than target_string, search the left side of array
        if arr[mid_pointer] > target_string:
            right = mid_pointer - 1

        else:  # Else we find that the mid_pointer is equals to our target_string, just return mid_pointer
            return mid_pointer

# TEST CASES


target = "ball"
test_1 = ["", "", "", "", "", ""]  # -> -1
test_2 = ["at", "", "", "", "ball", "car", "dad", ""]  # -> 4
test_3 = ["", "", "", "", "ball"]  # -> 4
test_4 = ["ball", "", "", "", ""]  # -> 0
test_5 = ["arrow", "ball", ""]

print(sparse_search(target, test_3))
