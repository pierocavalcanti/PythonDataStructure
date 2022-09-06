class Queue:
    def __init__(self,maxlen):
        self.maxlen = maxlen
        self.data = []

    def length(self):
        return len(self.data)

    def is_full(self):
        return len(self.data) == self.maxlen

    def push(self,elem):
        if len(self.data) == 5:
            raise Exception("Error: queue overflow (max length = {} )".format(self.maxlen),self.maxlen)
            return
        self.data.append(elem)

    def pop(self):
        if len(self.data) == 0:
            raise Exception("Error: queue is empty")
            return
        return self.data.pop()

    def __str__(self):
        return '['+','.join(self.data)+']'