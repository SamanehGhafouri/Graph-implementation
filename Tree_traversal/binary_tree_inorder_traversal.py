"""Inorder Traversal"""


class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def inorder_traverse(root):
    if root:
        inorder_traverse(root.left)
        print(root.val)
        inorder_traverse(root.right)


if __name__ == '__main__':
    root = Node(7)
    root.left = Node(4)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root.left.left.left = Node(1)
    root.left.left.right = Node(3)
    root.left.right.left = Node(5)

    root.right = Node(9)
    root.right.left = Node(8)
    root.right.right = Node(10)

    inorder_traverse(root)

