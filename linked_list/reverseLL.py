class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Given the head of a singly linked list, reverse the linked list and return its new head

    Runtime: O(n) where n is the size of our linked list array 
    Space: O(1) since no additional data structure is created
    """
    # Two pointer method
    # Keep a pointer for the previous node and the current node
    prev, curr = None, head

    # While head is not None
    while head:
        # Keep track of the next node with a temporary variable
        temp = curr.next
        # Update our next node to be the previous node
        curr.next = prev
        # Set previous to be the current node
        prev = curr
        # Set current node as the next node
        curr = temp
    # Once head is None, we just return prev which is now the head of our reversed linked list
    return prev
