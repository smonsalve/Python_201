from bst import BinarySearchTree


def demo1():
    my_bst = BinarySearchTree()
    my_bst.insert(2)
    my_bst.insert(1)
    my_bst.insert(3)

    print(my_bst.root.value)
    print(my_bst.root.left.value)
    print(my_bst.root.right.value)

def demo2():
    my_bst = BinarySearchTree()
    my_bst.insert(47)
    my_bst.insert(21)
    my_bst.insert(76)
    my_bst.insert(18)
    my_bst.insert(27)
    my_bst.insert(52)
    my_bst.insert(82)

    print(my_bst.contains(18))
    print(my_bst.contains(17))


def main():
    demo2()


if __name__ == "__main__":
    main()
