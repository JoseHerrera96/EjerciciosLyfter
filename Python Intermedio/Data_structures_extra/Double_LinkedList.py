class Node:
    next: "Node"
    prev: "Node"

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next # type: ignore
        self.prev = prev # type: ignore

class DoubleLinkedList:
    head: Node
    tail: Node

    def __init__(self, head=None, tail=None):
        self.head = head # type: ignore
        self.tail = tail # type: ignore
    
    def prepend(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def delete(self,data):
        if self.is_empty():
            return None
                
        current_node = self.head
        
        while current_node is not None:
            if current_node.data == data:
                if self.head == self.tail:
                    self.head = None # type: ignore
                    self.tail = None # type: ignore
                    return
                
                if current_node == self.head:
                    self.head = current_node.next
                    self.head.prev = None # type: ignore
                elif current_node == self.tail:
                    self.tail = current_node.prev
                    self.tail.next = None # type: ignore
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
            if current_node.next is not None:
                print("->", end=" ")
            current_node = current_node.next

    def print_backward(self):
        current_node = self.tail

        while current_node is not None:
            print(current_node.data)
            if current_node.prev is not None:
                print("<-", end=" ")
            current_node = current_node.prev

    def is_empty(self):
        return self.head is None and self.tail is None