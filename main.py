# This is a sample Python script.

from queue import Queue
from binary_tree import Node,topDown,downTop,rightLeft,leftRight, printTree

if __name__ == '__main__':
    q = Queue(5)

    q.push('a')
    q.push('b')
    q.pop()
    q.push('c')
    q.push('d')
    q.push('e')
    print(q)

    t = Node('a')
    t.childLeft = Node('b')
    t.childRight = Node('c')
    t.childLeft.childLeft = Node('d')
    t.childLeft.childRight = Node('e')

    printTree(t)
    print(topDown(t))
    print(downTop(t))
    print(rightLeft(t))
    print(leftRight(t))


