from tkinter import E


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_left_leaves(root):
    '''
    Given a binary tree, find the sum of all of its left leaves

    ex:
            3
           / \
          9   20
             /  \
            15   7

        return 24 since 9 + 15
    '''
    def dfs(root):
        '''
        Depth first search algorithm to get sum of left leaves
        '''
        # Edge case if non valid root
        if not root:
            return 0

        total_sum = 0

        # Only add to our sum if we have a left subtree and if it has a left leaf
        if root.left and (not root.left.left and not root.left.right):
            total_sum += root.left.val

        # Return recursively by checking both the left and right subtrees
        return total_sum + dfs(root.left) + dfs(root.right)

    return dfs(root)


root = Node(3, Node(9), Node(20, Node(15), Node(7)))
print(sum_left_leaves(root))
