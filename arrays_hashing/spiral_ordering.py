
def spiral_ordering(matrix):
    '''
    Given a 2D matrix, nested array, return all the elements of the matrix in spiral order

    ex:

    [1 2 3
     4 5 6
     7 8 9]

    return [1,2,3,6,9,8,7,4,5]

    EDGE CASE: not nxn matrix

    [1 2
     3 5
     6 7]

    return [1, 2, 5, 7, 6, 3]

    Runtime: O(n*m) traversing through all elements of matrix
    Space: O(n*m) all elements
    '''

    # Keep track of directions: left-right, up-down, right-left, down-up

    res = []

    rows = len(matrix)
    cols = len(matrix[0])

    # Boundaries for each direction
    left = up = 0
    right = cols - 1
    down = rows - 1

    # Make sure that we can keep appending while all elements have yet to be appended to result arr
    while len(res) < rows * cols:

        # Traverse right-left
        # 1, 2, 3
        for col in range(left, right+1):
            res.append(matrix[up][col])

        # Traverse down-up
        # 6, 9
        for row in range(up+1, down+1):
            res.append(matrix[row][right])

        # Traversing right-left and making sure not visiting a column already traversed
        if up != down:
            for col in range(right-1, left-1, -1):
                res.append(matrix[down][col])

        # Traversing down-up and making sure not visiting a row already traversed
        if left != right:
            for row in range(down-1, up, -1):
                res.append(matrix[row][left])

        # Update boundary values
        left += 1
        right -= 1
        up += 1
        down -= 1

    return res


matrix = [[1, 2], [3, 5], [6, 7]]
print(spiral_ordering(matrix))
