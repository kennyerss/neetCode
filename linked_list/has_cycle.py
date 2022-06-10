
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(self, head: Optional[ListNode]) -> bool:
    '''
    Returns true if LL has a cycle, otherwise if not, return False

    Floyd's Algorithm
    Runtime: O(n)
    Memory: O(1)
    '''

    # Two pointers that start at head
    slow = head
    fast = head

    # Loop runs when
    while head and head.next:

        slow = slow.next  # Increment slow pointer by one node
        fast = fast.next.next  # Increment fast pointer by two nodes

        # Eventually, if the two pointers ever intersect, return True since there is a cycle
        if slow == fast:
            return True

    return False
