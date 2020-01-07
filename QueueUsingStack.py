class Queue2Stacks(object):

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self,item):
        self.instack.append(item)
        print(self.instack)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        print(self.outstack.pop())

q = Queue2Stacks()
