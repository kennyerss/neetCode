
class Node:
    # Create our node class for our tree
    def __init___(self, value):
        self.left = None
        self.right = None
        self.value = value

    # Insert function to our tree
    def insert(self, value):
        if not self.value:
            self.value = value
