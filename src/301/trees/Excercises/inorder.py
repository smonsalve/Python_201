class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node

    def in_order(self, current_node):
        if current_node:
            self.in_order(current_node.left)
            print(current_node.data)
            self.in_order(current_node.right)

    def pre_order(self, current_node):
        if current_node:
            print(current_node.data)
            self.pre_order(current_node.left_child)
            self.pre_order(current_node.right_child)

    def post_order(self, current_node):
        if current_node:
            self.pre_order(current_node.left_child)
            self.pre_order(current_node.right_child)
            print(current_node.data)


my_tree = BinarySearchTree()
my_tree.insert(65)
my_tree.insert(20)
my_tree.insert(70)
my_tree.insert(10)
my_tree.insert(22)
my_tree.insert(68)
my_tree.insert(75)
my_tree.in_order(my_tree.root)

