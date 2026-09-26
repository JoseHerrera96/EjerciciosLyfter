class Node:
    data: str
    next: "Node"
    prev: "Node"

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    head: Node
    tail: Node

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def prepend(self):
        if self.is_empty():
            return None
        popped_node = self.head
        if self.head == self.tail:      # Solo queda 1 elemento
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return popped_node.data
    
    def delete(self,data):
        if self.is_empty():
            return None
        
        current_node = self.head
        
        while current_node is not None:
            if current_node.data == data:
                if current_node == self.head:
                    self.head = current_node.next
                    self.head.prev = None
                elif current_node == self.tail:
                    self.tail = current_node.prev
                    self.tail.next = None
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                return
            current_node = current_node.next
        return None

    def print_forward(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def print_backward(self):
        current_node = self.tail

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev

    def is_empty(self):
        return self.head is None and self.tail is None