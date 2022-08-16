import re


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_binary(node):
    '''
    Takes in a Node node tree that prints all the leaf nodes from left to right

    Method:

    Use an inorder traversal --> search the left side first then the root then the right

    Keep searching up until the node does not have a left or right node == LEAF NODE
    '''

    if not node:
        return

    if not node.left and not node.right:
        print(node.val)

    print_binary(node.left)

    print_binary(node.right)


input3 = Node(5, Node(3, Node(1), Node(4)), Node(6, None, Node(7)))
print_binary(input3)

# input1 = Node(2, Node(1), Node(3))
# print_binary(input1)

# input2 = Node(3, Node(2, Node(1)), Node(4, None, Node(5)))
# print_binary(input2)
