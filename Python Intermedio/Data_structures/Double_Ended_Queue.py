class Node:
  data: str
  next: "Node"
  prev: "Node"

  def __init__(self, data, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev

class DoubleEndedQueue:
    head: Node
    tail: Node

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def push_front(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_front(self):
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

    def push_back(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop_back(self):
        if self.is_empty():
            return None
        popped_node = self.tail
        if self.head == self.tail:      # Solo queda 1 elemento
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return popped_node.data

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def is_empty(self):
        return self.head is None and self.tail is None