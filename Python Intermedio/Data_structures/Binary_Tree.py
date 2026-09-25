class Node:
    data: str
    left: "Node"
    right: "Node"
    lvl : int

    def __init__(self, data, left=None, right=None, lvl=0):
        self.data = data
        self.left = left
        self.right = right
        self.lvl = lvl

class BinaryTree:
    root: Node
    level: int

    def __init__(self, root=None):
        self.root = root
        self.level = 0

    def insert_left(self, value, node=None):
        if self.is_empty():
            self.root = Node(value, lvl=0)
            self.level = 0
            return self.root
        if node is None:
            node = self.root
        new_node = Node(value, lvl=node.lvl + 1)
        node.left = new_node
        if new_node.lvl > self.level:
            self.level = new_node.lvl
        return new_node

    def insert_right(self, value, node=None):
        if self.is_empty():
            self.root = Node(value, lvl=0)
            self.level = 0
            return self.root
        if node is None:
            node = self.root
        new_node = Node(value, lvl=node.lvl + 1)
        node.right = new_node
        if new_node.lvl > self.level:
            self.level = new_node.lvl
        return new_node

    def _get_max_level(self, node):
        if node is None:
            return 0
        left_max = self._get_max_level(node.left)
        right_max = self._get_max_level(node.right)
        return max(node.lvl, left_max, right_max)

    def pop_left(self, node):
        if node is None or node.left is None:
            return None
        popped_node = node.left
        node.left = None
        if popped_node.lvl >= self.level:
            self.level = self._get_max_level(self.root)
        return popped_node.data
    
    def pop_right(self, node):
        if node is None or node.right is None:
            return None
        popped_node = node.right
        node.right = None
        if popped_node.lvl >= self.level:
            self.level = self._get_max_level(self.root)
        return popped_node.data

    def is_empty(self):
        return self.root is None
    
    def print_structure(self, node=None, level=0, prefix="Root: "):
        if level == 0:
            if self.is_empty():
                print("Tree is empty")
                return
            node = self.root

        if node is not None:
            print(" " * (level * 4) + prefix + str(node.data))
            if node.left or node.right:
                if node.left:
                    self.print_structure(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.print_structure(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")
        
# Create a binary tree
my_tree = BinaryTree()
my_tree.insert_left("Apple")                       # Root (level 0)
my_tree.insert_left("Banana", my_tree.root)        # Level 1 (left)
my_tree.insert_right("Cherry", my_tree.root)       # Level 1 (right)

my_tree.insert_left("Date", my_tree.root.left)         # Level 2
my_tree.insert_right("Elderberry", my_tree.root.left)   # Level 2
my_tree.insert_left("Fig", my_tree.root.right)         # Level 2
my_tree.insert_right("Grape", my_tree.root.right)      # Level 2

# Print the structure
print("--- Tree Structure ---")
my_tree.print_structure()
print(f"Current max level: {my_tree.level}")

# Test popping: pop 'Date' (level 2)
# There are still other nodes at level 2 (Elderberry, Fig, Grape), so level should NOT downgrade!
print("\n--- Popping 'Date' (lvl 2) from Banana ---")
popped = my_tree.pop_left(my_tree.root.left)
print(f"Popped node: {popped}")
print(f"Max level after pop (remains 2 because other level 2 nodes exist): {my_tree.level}")