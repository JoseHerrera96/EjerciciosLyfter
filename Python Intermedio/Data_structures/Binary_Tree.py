from LinkedList import Node

class BinaryTree:
    head: Node
    left: Node
    right: Node

    def __init__(self, head=None, left=None, right=None):
        self.head = head
        self.left = left
        self.right = right

    def insert(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            self.left = new_node
    
    def is_empty(self):
        return self.head is None
    
    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    