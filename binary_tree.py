class Node:
    def __init__(self,label,left=None, right=None):
        self.childLeft = left
        self.childRight = right
        self.label = label

def leftRight(root):
    "visiting nodes from left to right"
    if root:
        topdown(root.childLeft)
        print(root.label)
        topdown(root.childRight)

def rightLeft(root):
    "visiting nodes from left to right"
    if root:
        topdown(root.childRight)
        print(root.label)
        topdown(root.childLeft)

def downTop(root):
    if root:
        topdown(root.childLeft)
        topdown(root.childRight)
        print(root.label)

def topDown(root):
    if root:
        print(root.label)
        topdown(root.childLeft)
        topdown(root.childRight)


def printTree(node, level = 0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + node.value)
        printTree(node.right, level + 1)