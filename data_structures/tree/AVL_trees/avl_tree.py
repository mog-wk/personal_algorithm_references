class Node:
    def __init__(self, data):
        self.balance_factor = 0
        self.data = data
        self.l_ptr = None
        self.r_ptr = None

    def __str__(self):
        return f"({self.data}, {self.balance_factor})"
        #return f"========\n{self.data}\n{self.l_ptr}\n{self.r_ptr}\n{self.balance_factor}"

class AvlTree:
    def __init__(self, root: Node):
        self.root = root

    def insert(self, node: Node):
        cur = self.root

        while cur:
            if node.data <= cur.data:
                if cur.l_ptr != None:
                    cur = cur.l_ptr
                else:
                    cur.l_ptr = node
                    break
            else:
                if cur.r_ptr != None:
                    cur = cur.r_ptr
                else:
                    cur.r_ptr = node
                    break

    def pre_order(self):
        def traverse(node):
            if not node: return 
            print(node, end=' ')
            traverse(node.l_ptr)
            traverse(node.r_ptr)
        traverse(self.root)
        print()
    def in_order(self):
        def traverse(node):
            if not node: return
            traverse(node.l_ptr)
            print(node, end=' ')
            traverse(node.r_ptr)
        traverse(self.root)
        print()
    def post_order(self):
        def traverse(node):
            if not node: return
            traverse(node.l_ptr)
            traverse(node.r_ptr)
            print(node, end=' ')
        traverse(self.root)
        print()

        
tree = AvlTree(Node(12))
data_list = [8, 16, 23, 16, 9, 2, 5, 1]
for data in data_list:
    tree.insert(Node(data))



tree.pre_order()
tree.in_order()
tree.post_order()
