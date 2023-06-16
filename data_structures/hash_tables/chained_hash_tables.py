# impl for chained hash table

class Node:
    def __init__(self, value, ptr=None):
        self.value = value
        self.ptr = ptr
    def __str__(self):
        return f"{self.value} | {self.ptr}"


class ChainedHashTable:
    def __init__(self, nodes: list):
        self.keys = list()
        
        for key, value in nodes:
            self.add(key, value)


    def add(self, key, value):
        if not isinstance(key, str): 
            key = str(key)
            

        if not self.contains(key):
            node = Node(value)
            self.keys.append((key, node))
        else:
            ind = self.from_key(key)
            cur = self.keys[ind][1]
            
            # go to end of chain
            while cur.ptr:
                cur = cur.ptr
            cur.ptr = Node(value)

    def remove(self, key):
        ind = self.from_key(key)
        self.keys.pop(ind)

    def contains(self, key):
        return key in [i[0] for i in self.keys]

    
    # private
    def from_key(self, key):
        for i in range(len(self.keys)):
            cur = self.keys[i][0]
            if cur == key:
                return i
        else:
            raise ValueError

    def empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.keys)
    
    def __contains__(self, key):
        return key in [i[0] for i in self.keys]

    def __str__(self):
        return f"{[(i[0], i[1].__str__()) for i in self.keys]}"


if __name__ == "__main__":
    tests = [
            ChainedHashTable([("test_1", 12)]),
            ChainedHashTable([("test_1", 12), ("test_1", 13)]),
            ChainedHashTable([("test_1", 12), ("test_1", 13), ("test_2", 12), ("test_3", 12), ("test_3", 12), ]),
            ]

    for test in tests:
        test.add("1", 12)
        test.add(1, 12)
        test.remove("1")
        print(test)
