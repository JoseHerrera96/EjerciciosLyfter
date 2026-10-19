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



def _insert_bst_value(tree: BinaryTree, value):
    if tree.is_empty():
        tree.insert_left(value)
        return

    current = tree.root
    while True:
        if value <= current.data:
            if current.left is None:
                tree.insert_left(value, current)
                return
            current = current.left
        else:
            if current.right is None:
                tree.insert_right(value, current)
                return
            current = current.right


def _insert_tree_values(sorted_tree: BinaryTree, node):
    if node is None:
        return
    _insert_bst_value(sorted_tree, node.data)
    _insert_tree_values(sorted_tree, node.left)
    _insert_tree_values(sorted_tree, node.right)


def BubbleSort_BinaryTree(tree: BinaryTree):
    if tree is None or tree.is_empty():
        return tree

    sorted_tree = BinaryTree()
    _insert_tree_values(sorted_tree, tree.root)
    tree.root = sorted_tree.root
    tree.level = sorted_tree.level
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