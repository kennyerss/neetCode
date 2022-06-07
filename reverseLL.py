class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

    prev, curr = None, head

    while head:

        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        
    return prev

    
