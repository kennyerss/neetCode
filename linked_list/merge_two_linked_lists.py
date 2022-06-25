
class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head_node: LinkedNode) -> None:
    trv = head_node

    while trv:
        print(trv.val)
        trv = trv.next


def merge_two_LL(List1, List2) -> LinkedNode:
    """x
    Given the heads of two sorted linked lists, merge the two LL together and return one sorted list
    Return the head of the merged linked list

    Input: list1 = [1,2,4], list2 = [1,3,4] >> [1,1,2,3,4,4]
           list1 = [], list2 = [] >> []
           list1 = [], list2 = [0] >> [0]
           list1 = [1,3], list2 = [1,2] >> [1,1,2,3]

    Edge case:
           list1 = [-1, 6], list2 = [-1, 1]
           return [-1,-1,1,6]

       Runtime: O(n+m)
       Space: O(1)

    Match: dummy head with two pointers to traverse through both linked lists

    Plan: 
        1) Create dummy head 
        2) Two pointers p1, p2 for both linked lists
        3) while 



    """
    # Create our dummy head
    dummy = LinkedNode(0)
    # Create our pointer of our return list
    dummy_pointer = dummy

    # Two pointers for both lists
    p1, p2 = List1, List2

    # Make sure while p1 and p2 have not been fully traversed (both p1 and p2 are not null)
    while p1 or p2:
        # Check which node to first look at (the smaller one) or if its equal
        if p1.val <= p2.val:
            dummy_pointer.next, p1 = p1, p1.next
        else:
            dummy_pointer, p2 = p2, p2.next

        dummy_pointer = dummy_pointer.next

    return dummy_pointer.next


node1 = LinkedNode(1)
node2 = LinkedNode(2)
node3 = LinkedNode(4)
node1.next = node2
node2.next = node3
node3.next = None

node4 = LinkedNode(1)
node5 = LinkedNode(3)
node6 = LinkedNode(4)
node4.next = node5
node5.next = node6
node6.next = None

result_list = merge_two_LL(node1, node4)
print(result_list)
while result_list.next:
    print(result_list.val)
