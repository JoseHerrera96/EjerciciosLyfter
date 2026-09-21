from Queue_LinkedList import Node

class DoubleEndedQueue:
    head: Node
    tail: Node

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop_front(self):
        if self.is_empty():
            return None
        popped_node = self.head
        assert self.head is not None
        self.head = self.head.next # type: ignore
        return popped_node.data

    def push_back(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop_back(self):
        if self.is_empty():
            return None
        popped_node = self.tail
        assert self.tail is not None
        self.tail = self.tail.next # type: ignore
        return popped_node.data

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def is_empty(self):
        return self.head is None

