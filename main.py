
from stack import Stack
from binary_tree import Node,topDown,downTop,rightLeft,leftRight,printTree
from sorting import bubbleSort
from searching import binarySearch, linearSearch

if __name__ == '__main__':
    print('a')
    q = Stack(5)

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
    t.childRight.childLeft = Node('f')
    t.childRight.childRight = Node('g')

    printTree(t)
    print(topDown(t))
    print(downTop(t))
    print(rightLeft(t))
    print(leftRight(t))

    array = ['Piero','Paolo','Gian','Andrea','Richeldi']
    print(array)
    print(bubbleSort(array))

    print(binarySearch(array,'Piero'))
    print(binarySearch(array,'Peter'))
    print(linearSearch(array,'Piero'))
    print(linearSearch(array,'Peter'))






