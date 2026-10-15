from Binary_Tree import BinaryTree, Node
from Double_Ended_Queue import DoubleEndedQueue, Node
from Stack import Stack

def BubbleSort(list):
    if isinstance(list, BinaryTree):
        return BubbleSort_BinaryTree(list)
    elif isinstance(list, DoubleEndedQueue):
        return BubbleSort_DoubleEndedQueue(list)
    elif isinstance(list, Stack):
        return BubbleSort_Stack(list)
    elif list is None:
        return
    else:
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
                    swapped = True
        return list


def leftist_node(tree: BinaryTree):
    if tree is None or tree.root is None:
        return None
    node = tree.root
    while node.left is not None:
        node = node.left
    return node

def BubbleSort_BinaryTree(tree: BinaryTree):
    if tree is None or tree.is_empty():
        return tree

    nodes = []

    def collect_in_order(node):
        if node is None:
            return
        collect_in_order(node.left)
        nodes.append(node)
        collect_in_order(node.right)

    collect_in_order(tree.root)

    swapped = True
    while swapped:
        swapped = False
        for index in range(len(nodes) - 1):
            if nodes[index].data > nodes[index + 1].data:
                nodes[index].data, nodes[index + 1].data = (
                    nodes[index + 1].data,
                    nodes[index].data,
                )
                swapped = True

    return tree

def BubbleSort_DoubleEndedQueue(deque: DoubleEndedQueue):
    if deque is None:
        return None
    if deque.is_empty():
        return deque

    swapped = True
    while swapped:
        swapped = False
        current = deque.head
        while current is not None and current.next is not None:
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
                swapped = True
            current = current.next
    return deque

def BubbleSort_Stack(stack: Stack):
    if stack is None:
        return None
    if stack.is_empty():
        return stack

    swapped = True
    while swapped:
        swapped = False
        current = stack.top
        while current is not None and current.next is not None:
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
                swapped = True
            current = current.next
    return stack