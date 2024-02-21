class Node:
    def __init__(self, n: int):
        self.data = n
        self.left  = None # ptr to left node
        self.right = None # ptr to right node

    def __str__(self):
        return f"data: {self.data}\nleft: {self.left}\nright: {self.right}"


class BST:
    '''binary search tree'''

    def __init__(self):
        self.root = None

    def add(self, node: Node):
        if not self.root:
            self.root = node
            return None

        cur = self.root

        while (1):
            if cur.data >= node.data:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = node
                    break
            else: 
                if cur.right:
                    cur = cur.right
                else: 
                    cur.right = node
                    break


    @staticmethod
    def from_list(node_list: list):
        '''return BST with all elements of node_list added linearly'''
        bst = BST()
        for i in node_list:
            node = Node(i)
            bst.add(node)

        return bst

    def print(self):
        '''bad print for debugging'''
        print(self.root)


    '''
    def preorder(self):
        cur = self.root
        stack = []
        while cur:
            print(cur.data)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            if len(stack) > 0:
                cur = stack.pop()
            else:
                cur = None
                '''
    # Depth first search
    def preorder(self, node=None):
        if not node: return;
        print(node.data, end=' ')
        self.preorder(node=node.left)
        self.preorder(node=node.right)

    def inorder(self, node=None):
        if (not node): return
        self.inorder(node=node.left)
        print(node.data, end=' ')
        self.inorder(node=node.right)

    def postorder(self, node=None):
        if (not node): return
        self.postorder(node=node.left)
        self.postorder(node=node.right)
        print(node.data, end=' ')

    # Breadth first search
    # ....


if __name__ == "__main__":
    tree = BST.from_list([4, 5, 2, 3, 1])

    print("preorder")
    tree.preorder(tree.root)
    print("\ninorder")
    tree.inorder(tree.root)
    print("\npostorder")
    tree.postorder(tree.root)
    print()
