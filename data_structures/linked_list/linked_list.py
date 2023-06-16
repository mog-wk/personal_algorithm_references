
class Node:
    def __init__(self, data, ptr):
        self.data = data;
        self.ptr = ptr

class SingleLinkedList():
    def __init__(self, node: Node):
        if not node or not isinstance(node, Node): 
            print("provide node")
            return
        self.head = node
        size = 0
        cur_node = node
        while cur_node.ptr != None:
            cur_node = cur_node.ptr
            size += 1
        self.size = size


if __name__ == "__main__":
    tests = [

            ]
