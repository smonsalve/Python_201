class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():

    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)        
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results


miarbol = BinarySearchTree()
miarbol.insert(1)
miarbol.insert(2)
miarbol.insert(5)
miarbol.insert(3)
miarbol.insert(4)
miarbol.insert(6)

print(miarbol.dfs_pre_order())  # [1, 2, 5, 3, 4, 6]


# miarbol = BinarySearchTree()
# miarbol.insert(47)
# miarbol.insert(21)
# miarbol.insert(76)
# miarbol.insert(18)
# miarbol.insert(27)
# miarbol.insert(52)
# miarbol.insert(82)

# print(miarbol.dfs_pre_order())  # [47, 21, 18, 27, 76, 52, 82]