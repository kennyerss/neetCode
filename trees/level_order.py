from collections import deque


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    '''
    Given a Node root binary tree, print array of elements in level order traveral 

    ex:
            2
           / \ 
          1   3 
         / \   \ 
        4   6   8 

        print 2, 1, 3, 4, 6, 8
    '''
    # Check for valid root
    if not root:
        return -1

    # Create queue
    queue = deque()

    # Add root val to queue
    queue.append(root)

    # Elements to be processed
    while len(queue) > 0:
        # print the curr_node with popleft method

        # For each level
        for i in range(len(queue)):
            curr_node = queue.popleft()
            print(curr_node.val)
            # Append each children of the curr_node to queue

            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)


root = Node(2, Node(1, Node(4), Node(6)), Node(3, None, Node(8)))
level_order(root)
