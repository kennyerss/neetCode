def remove_nth_node(linked_list, n):
    """
    Given the head of a linked list, remove the nth node from the end of the linked list.
    Return the new linked list with the removed node.

    U -> Can n be larger than the length of the linked list?
         What should a sized one linked list return? []
         [1,2], n=1 -> [1] 

    Multiple pass -> Take a first pass through linked list to store elements in array
                     Can also take a pass to get the length of the linked list and then a second pass to remove reference from nth to last node

    Runtime: O(n) where n is the length of our linked list
    Space: O(1) since no additional data structure is created
    """
    # Iterate through LL to get our lenght
    # Target position is length - n
    # Initialize variable nodes_seen to how much nodes_seen so far to compare to our target node
    # Iterate through our LL until nodes_seen == target
    # prev node of nth node should point to nth node.next
