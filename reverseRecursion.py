# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursively
        # Runtime O(n), memory space O(n)

        # Base case: if head is empty
        if not head:
            return None 
        
        newHead = head # Going to be our new head of the reversed list
        
        if head: 
            newHead = self.reverseList(head.next) # recursively set our newHead to be the head.next 
            head.next.next = head 
        head.next = None # When we reach the last node of our list, set its next node to be None

        return newHead


list = [1,2,3,4,5]
print(reverseList(list))