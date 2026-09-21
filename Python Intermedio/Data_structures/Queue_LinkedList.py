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


tercer_nodo = Node("Soy el tercer nodo")
segundo_nodo = Node("Soy el segundo nodo", tercer_nodo)
primer_nodo = Node("Soy el primer nodo", segundo_nodo)

queue = Queue(primer_nodo)

print("Agregando un elemento")

queue.enqueue(Node("Soy el nuevo nodo!"))
queue.print_structure()

print("Quitando un elemento")

queue.dequeue()
#queue.print_structure()https://drive.google.com/file/d/11OMGR8dFh9gzEMkICyrHltV-02elvgQg/view?usp=sharing
