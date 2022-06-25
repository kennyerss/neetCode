
class LinkedNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_node(head: LinkedNode, val: int) -> LinkedNode:
    """
    Given a ListNode object node as our parameter, delete the integer val from our linked list and return the new linked list 
    with the deleted val

    Dummy node and traversing through linked list
    """
    # First creating our dummy node with value initialized as zero
    dummy = LinkedNode(0)
    # Point to dummy.next as our head which is what we would eventually return
    dummy.next = head

    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    # Because dummy.next is pointing to the head of our linked list, we just return this
    return dummy.next
