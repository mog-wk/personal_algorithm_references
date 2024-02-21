
class Heap:
    def __init__(self, root, is_max=True):
        self.root = root
        self.tail = root.l_child
        self.is_max = is_max
        self.len = 1

    def insert(self, node, cur=None):
        if cur == None:
            cur = self.root
        self.tail = 


    def extract(self):
        pass

    def size(self):
        return self.len

    def heapfy(self):
        pass

class Node:
    def __init__(self, value):
        self.value = value
        self.l_child = None
        self.r_child = None

    @staticmethod
    def with_child(value, l_child, r_child):
        node = Node(value)
        node.l_child = l_child
        node.r_child = r_child
        return node

    def add_child(node):
        ## !!!!
        if not self.l_child:
            self.l_child = node
            return self
        if not self.r_child:
            self.r_child = node
            return self

        self.l_child.add_child(node)
        self.r_child.add_child(node)

    def __str__(self):
        # prints pre-order
        return "{} {} {} |".format(self.value, self.l_child, self.r_child)


nodes = [
        Node(25), Node(11), Node(6), Node(10),# Node(22), Node(42), Node(99), Node(2),
        ]
test_heap = Heap(Node(32))

for n in nodes:
    test_heap.insert(n)

print(
        "{}".format(test_heap.root, test_heap.len)
        )
