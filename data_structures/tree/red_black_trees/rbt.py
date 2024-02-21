
## Attempt to make binary search tree balanced
## 1. all Nodes of the tree are colored either red or black
## 1.1. inserted nodes are always red
## 2. all leaves(nils) are collored black
## 3. every red node has black child
## 4. for any node, the number of black nodes for any path to the leaves is the same

class Node:
    def __init__(self, value):
        self.value = value
        self.is_black = False
        self.l_child = None
        self.r_child = None

    def __str__(self):
        return "{}\n{}\n{}".format(
                self.value,
                self.l_child,
                self.r_child,
                )

    def add(self, node):
        if node.value <= self.value:
            if not self.l_child:
                self.l_child = node
            else:
                self.l_child.add(node)
        else:
            if not self.r_child:
                self.r_child = node
            else:
                self.r_child.add(node)


if __name__ == "__main__":
    tree = Node(4)
    tree.add(Node(5))
    tree.add(Node(2))
    print(tree)
