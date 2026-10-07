class Node:
  next: "Node"

  def __init__(self, data, next=None):
    self.data = data
    self.next = next # type: ignore

class LinkedList:
  head: Node

  def __init__(self, head=None):
    self.head = head # type: ignore

  def insert_front(self, data):
    if self.head is None:
      self.head = Node(data)
      return
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_back(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return

    current_node = self.head
    while current_node.next is not None:
      current_node = current_node.next
    current_node.next = new_node

  def delete(self, data):
    current_node = self.head

    while current_node is not None:
      if current_node.data == data:
        self.head = current_node.next
        return
      if current_node.next is not None and current_node.next.data == data:
        current_node.next = current_node.next.next
        return
      current_node = current_node.next

  def print_all(self):
    current_node = self.head

    while current_node is not None:
      print(current_node.data)
      if current_node.next is not None:
        print("->", end=" ")
      current_node = current_node.next