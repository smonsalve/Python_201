
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
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
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node.value)

        while (len(queue)>0):
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
               queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

