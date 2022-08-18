

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side(root):
    '''
    Takes in a root tree and returns the right side view of the tree

    Example:
                1    
               / \
              5   3  
             /   /  
            3  2
           /
          0
    '''
    if not root:
        return []

    queue = deque()
    result = []

    queue.append(root)

    # If queue isn't empty (values need to be processed)
    while len(queue) > 0:

        # Process one level at a time (for each element in queue)
        for i in range(len(queue)):
            curr_node = queue.popleft()
            # For each node, append its children to the queue
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        # Add value of last node of curr level to result
        result.append(curr_node.val)

    return result


root = Node(1, Node(5, Node(3, Node(0), None), None), Node(3, Node(2), None))
print(right_side(root))
