# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:  # Base case
            return

        else:

            self.swap_node(root)

            # Recursively call the root.left and root.right so it continuously swaps
            self.invert_tree(root.left)
            self.invert_tree(root.right)

            return root

    # Swap the node with temp variable
    def swap_node(self, node: Optional[TreeNode]) -> None:
        temp = node.left
        node.left = node.right
        node.right = temp
