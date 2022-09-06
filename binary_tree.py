class Node:
    def __init__(self,label,left=None, right=None):
        self.childLeft = left
        self.childRight = right
        self.label = label

def leftRight(root):
    "visiting nodes from left to right"
    if root:
        leftRight(root.childLeft)
        print(root.label)
        leftRight(root.childRight)

def rightLeft(root):
    "visiting nodes from left to right"
    if root:
        rightLeft(root.childRight)
        print(root.label)
        rightLeft(root.childLeft)

def downTop(root):
    if root:
        downTop(root.childLeft)
        downTop(root.childRight)
        print(root.label)

def topDown(root):
    if root:
        print(root.label)
        topDown(root.childLeft)
        topDown(root.childRight)


def printTree(node, level = 0):
    if node != None:
        printTree(node.childRight, level + 1)
        print(' ' * 4 * level + '-> ' + node.label)
        printTree(node.childLeft, level + 1)