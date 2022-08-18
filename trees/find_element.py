class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_element(root, element):
    '''
    Takes in a TreeNode root and returns boolean True or False if element exists or not in the BST

    ex: element = 4
        3
       / \
      1   4  

    return True

    element = 5 >> return False
    '''
    # Check for valid root and whether or not element doesn't exist
    if not root:
        return False

    # Else if element == root value return True
    elif root.val == element:
        return True

    # Search right subtree if element is greater than the root value
    elif element > root.val:
        return find_element(root.right, element)

    # Search left subtree if element is less than or equal to root value
    elif element <= root.val:
        return find_element(root.left, element)


root = TreeNode(3, TreeNode(1), TreeNode(4))
element = 2

print(find_element(root, element))
