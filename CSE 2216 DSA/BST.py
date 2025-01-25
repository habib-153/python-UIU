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

def deleteNode(root, key):
    if root is None:
        return root
    if root.data > key:
        root.left = deleteNode(root.left, key)
    elif root.data < key:
        root.right =  deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root

def levelOrder(root):
    if root is None:
        return f"Tree is empty"
    else:
        q = []
        q.append(root)
        while len(q) > 0:
            print(q[0].data, end=' ')
            node = q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

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
deleteNode(root, 1)
postOrder(root)
print()
preOrder(root)
print()
levelOrder(root)