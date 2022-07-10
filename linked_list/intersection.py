class LinkedNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def intersection(node1, node2):
    """
    Given two LinkedNode node and node2 parameters, return the node object intersection of the two linked lists
    Only one intersection!

    ex: 
        node1, node2 = None, None >> return None
        no intersecting nodes >> return None
        intersection == nodes with same value but not necessarily intersecting

    Multple passes? Need to get the length of the list?
    Dummy head? Reconstructing or modifying input list or creating entirely new list
    Two pointers? Help find node to remove and then restructure our pointers to "remove" the node from the list

    Using a set to store each node of node2 

    Runtime: O(m+n) where m and n are the total number of nodes for both lists
    Space: O(m) where m is the number of nodes in the first list
    """
    # Initialize set to store nodes of list
    node1_nodes = set()

    # Dummy head to traverse through node1
    temp_node1 = node1
    # Traverse node1 and insert address (node object) of each node into set
    while temp_node1 is not None:
        # Store the values first
        node1_nodes.add(temp_node1)
        temp_node1 = temp_node1.next

    # Dummy head to traverse through node2
    temp_node2 = node2
    # Traverse node2 and find first node that is already present in set
    while temp_node2 is not None:
        if temp_node2 in node1_nodes:
            # Return current node if its found in the set
            return temp_node2
        temp_node2 = temp_node2.next

    # Return none if linked lists do not intersect
    return None
