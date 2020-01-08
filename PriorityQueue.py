class PriorityQueue:

    def __init__(self):
        self.queue = []

    def __str__(self):
        print(' '.join([str(i) for i in self.queue]))

    def isEmpty(self):
        return len(self.queue) == []

    def insert(self, item):
        self.queue.append(item)
        print(self.queue)

    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            print('item',item)
            del self.queue[max]
            print(self.queue)
            return item
        except IndexError:
            print()
            exit()
p = PriorityQueue()
p.insert(10)
p.insert(12)
p.insert(5)
p.insert(30)
p.delete()