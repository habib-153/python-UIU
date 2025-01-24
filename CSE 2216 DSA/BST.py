class Node:
    def __init__(self, key):
        self.left = None
        self.data = key
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if root.data > key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inOrder(root):
    if root is None:
        return f"Tree is empty"
    else:
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)

def preOrder(root):
    if root is None:
        return f"Tree is empty"
    else:
        print(root.data, end=' ')
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root is None:
        return f"Tree is empty"
    else:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=' ')


def minValueNode(node):
    current = node

    # Find the leftmost leaf
    while (current.left is not None):
        current = current.left

    return current


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

inOrder(root)
print()
postOrder(root)
print()
preOrder(root)