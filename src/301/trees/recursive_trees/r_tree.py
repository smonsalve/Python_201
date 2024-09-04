class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
    def r_contains(self, value):
        self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def height(self, root):
        if root is None:
            return 0
        return max(height(root.left), height(root.right))+1
 
    def getcol(h):
        if h == 1:
            return 1
        return getcol(h-1) + getcol(h-1) + 1
    
    
    def printTree(M, root, col, row, height):
        if root is None:
            return
        M[row][col] = root.data
        printTree(M, root.left, col-pow(2, height-2), row+1, height-1)
        printTree(M, root.right, col+pow(2, height-2), row+1, height-1)
    
    
    def TreePrinter():
        h = height(myTree.root)
        col = getcol(h)
        M = [[0 for _ in range(col)] for __ in range(h)]
        printTree(M, myTree.root, col//2, 0, h)
        for i in M:
            for j in i:
                if j == 0:
                    print(" ", end=" ")
                else:
                    print(j, end=" ")
            print("")