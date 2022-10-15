"""Postorder Traversal"""


class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val)


if __name__ == '__main__':
    root = Node(5)
    root.right = Node(4)
    root.right.left = Node(3)
    root.right.left.right = Node(2)
    root.right.left.right.left = Node(1)

    postorder_traversal(root)

