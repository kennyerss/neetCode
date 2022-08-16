from logging import root


class Node:

    def __init__(self, val, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right


def root_to_leaf(node, paths=[]):
    '''
    Given a Node tree, find all the paths from the root to leaf

    Method: 

    Postorder Traversal --> we want to explore the children first before the root   


    '''

    if not node:
        return

    paths.append(node.val)
    # Leaf node
    if not node.left and not node.right:
        print(paths)

    root_to_leaf(node.left)
    root_to_leaf(node.right)
    paths.pop()
    # root_to_leaf(tree.right)
    # return tree.val


input4 = Node(6, Node(4, Node(3, Node(1), Node(-1)),
                      Node(2, Node(1), Node(-1))), Node(7,
                                                        Node(3, Node(1), Node(-1)), Node(2, Node(1), Node(-1))))

root_to_leaf(input4)
