from LinkedList import LinkedList

class Node:
  data: str

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Queue(LinkedList):
  def enqueue(self, new_node):
    current_node = self.head
    next_node = current_node.next
    while (next_node is not None):
      current_node = next_node
      next_node = current_node.next

    current_node.next = new_node

  def dequeue(self):
    self.head = self.head.next

