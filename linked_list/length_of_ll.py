
class ListNode (object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getLength(head):
    """
    Given the head of our ListNode class object, return the length of the linked list 
    ex:
        1->2->3 return 3
        None -> return 0

    Multiple passes method to get length of list
    Runtime: O(n)
    Space: O(1)

    Plan:
        1) Initialize length counter variable
        2) While head of node:
            3) Increment our length counter
            4) set head to head.next
        5) return length
    """
    if head == None:
        return 0
    length = 0
    while head is not None:
        length += 1
        head = head.next
    return length


class Tests:
    if __name__ == "__main__":
        n0 = ListNode(0)
        print(f"Test 1 - getLength returned: {getLength(n0)}, expected: 1")

        n1 = ListNode(val=1)
        n2 = ListNode(val=2)
        n3 = ListNode(val=3)
        n1.next = n2
        n2.next = n3
        print(f"Test 2 - getLength returned: {getLength(n1)}, expected: 3")


node0 = ListNode(None)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

# print(length_of_ll(node1))
# print(length_of_ll(node0))
