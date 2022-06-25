
class Node:

    # constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
    # if(self.head):


# create a single Node
first = Node(3)
print(first.data)
