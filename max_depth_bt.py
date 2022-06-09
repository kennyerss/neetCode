def max_depth_bt(root):
    """
    Takes in a valid tree given a root and returns the maximum depth of the binary tree

    Input:
            3
        2       5  
     1        

    Output: 2 since maximum depth is from 3 -> 2 -> 1

    Method: DFS -> search up until you can no longer search in this tree and then return its depth

    Recursive approach
    Runtime: O(n) where n is the total number of nodes we have to search through
    Memory: O(h) where h is the height of the tree specifying the total number of recursion calls we'll be allocating to memory
    """
    assert root
    # Initialize depth = 0
    depth = 0
    # Each recursive call, we'll take the maximum depth of root.left and root.right incrementing by 1 each time
    depth = 1 + max(max_depth_bt(root.left), max_depth_bt(root.right))
    return depth
