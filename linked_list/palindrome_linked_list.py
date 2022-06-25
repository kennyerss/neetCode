from xml.dom.pulldom import ErrorHandler


class Node(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def is_palindrome(head):
    """
    Given the head of a singly linked list, return true if it is a palindrome

    ex: head = [1,2,2,1] -> true
        head = [1,2] -> false
        head = [] -> false?
        head = [1] -> true?

    Manipulating linked list -> reverse the linked list... check if it's the same as our head
    Dummy head method

    Runtime: O(n)
    Space: O(1)

    1) Create dummy head of our linked list
    2) Reverse function that reverses linked list 
    3) Compare dummy head and head ... return True if it is equal otherwise False
    """
    # Create reversed function
    def reverse_linked_list(head):
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

    reversed_ll = reverse_linked_list(head)
    return reversed_ll == head
