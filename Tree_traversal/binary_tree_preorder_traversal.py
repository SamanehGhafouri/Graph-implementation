"""Preorder Traversal"""


class Node:

    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key


def preorder_traversal(root):
    if root:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(4)
    root.left.left = Node(3)
    root.left.right = Node(8)
    root.left.right.left = Node(5)

    root.right = Node(7)
    root.right.left = Node(2)
    root.right.left.right = Node(6)
    root.right.right = Node(9)

    preorder_traversal(root)
