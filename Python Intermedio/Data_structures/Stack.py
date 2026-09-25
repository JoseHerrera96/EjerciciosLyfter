from Queue_LinkedList import Node

class Stack:
    top: Node

    def __init__(self, head=None):
        self.top = head
    
    def push(self, value):
        if self.is_empty():
            self.top = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node


    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            return popped_node.data

    def print_structure(self):
        current_node = self.top

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    def is_empty(self):
        return self.top is None