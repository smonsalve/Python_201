
from r_tree import BinarySearchTree


def crear_arbol0():
    arbol0 = BinarySearchTree()
    arbol0.r_insert(2)
    arbol0.r_insert(1)
    arbol0.r_insert(3)

    print(f"Root: {arbol0.root.value}")
    print(f"Root -> Left:  {arbol0.root.left.value}")
    print(f"Root -> Right:  {arbol0.root.right.value}")


def crear_arbol1():
    arbol1 = BinarySearchTree()
    arbol1.r_insert(47)
    arbol1.r_insert(21)
    arbol1.r_insert(76)
    arbol1.r_insert(18)
    arbol1.r_insert(27)
    arbol1.r_insert(52)
    arbol1.r_insert(82)

    print(f"arbol1 contiene el 27: {arbol1.r_contains(27)}")  # True
    print(f"arbol1 contiene el 17: {arbol1.r_contains(17)}")  # False


if __name__ == "__main__":
    # crear_arbol0()
    crear_arbol1()
