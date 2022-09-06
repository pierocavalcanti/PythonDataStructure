# This is a sample Python script.

from queue import Queue

if __name__ == '__main__':
    q = Queue(5)

    q.push('a')
    q.push('b')
    q.pop()
    q.push('c')
    q.push('d')
    q.push('e')
    print(q)
