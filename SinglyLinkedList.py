class Node(object):

    def __init__(self,item):
        self.item = item
        self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c

print(a.item)
print(a.nextnode.item)
print(b.nextnode.item)
print(c.nextnode)