class Node:
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next # type: ignore


class Queue:
    head: Node

    def __init__(self, head=None):
        self.head = head # type: ignore

    def print_all(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            if current_node.next is not None:
                print("->", end=" ")
            current_node = current_node.next

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def dequeue(self):
        if self.head:
            dequeued_data = self.head.data
            self.head = self.head.next
            return dequeued_data
        return None
