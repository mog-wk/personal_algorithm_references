import time

class Set:
    def __init__(self, *elts):
        self.elements = []
        self.size: int = 0
        for elt in elts:
            self.insert(elt)
            self.size += 1


    @staticmethod
    def from_list(arr):
        s = Set()
        for elt in arr:
            s.elements.append(elt)
            s.size += 1
        return s

    def destroy(self):
        for elt in self.elements:
            del elt
        del self.size
        del self

    def copy(self):
        return Set.from_list(self.set())

    def insert(self, elt) -> bool:
        if self.contains(elt):
            return False
        self.set().append(elt)
        self.size += 1
        return 0

    def remove(self, elt) -> bool:
        if not self.contains(elt):
            return False
        self.set().remove(elt)
        self.size -= 1
        return True

    def unite(self, set_2):
        if not isinstance(set_2, Set): raise Exception
        s = self.copy()
        for elt in set_2.elements: s.insert(elt)
        return s

    def intersect(self, set_2):
        if not isinstance(set_2, Set): raise Exception
        s = Set()
        for elt in self.elements:
            if set_2.contains(elt): s.insert(elt)
        return s

    def diff(self, set_2):
        s = Set()
        s_int = self.intersect(set_2)
        for elt in self.elements:
            if not s_int.contains(elt): s.insert(elt)
        for elt in set_2.elements:
            if not s_int.contains(elt): s.insert(elt)
        return s

    def contains(self, elt) -> bool:
        # TODO mk O(1)
        for i in self.set():
            if i is elt: return True
        return False

    def is_subset(self, st) -> bool:
        for elt in st.elements:
            if not self.contains(elt): return False
        return True

    def len(self) -> int:
        return self.size

    def set(self):
        # TODO shuffle
        return self.elements

    def __str__(self):
        return f"{self.set()}"



if __name__ == "__main__":
    tests = [
            Set(2, 3, 4, 5),
            Set(5, 5),
            Set(),
            Set(2.23, 3.3, 4.3, 21.2),
            Set(1, 2, 3, 5, 7, 11),
            Set.from_list([4, 2, 3, 65]),
            ]
    t2 = Set(4, 5, 678)
    t3 = Set(2, 4)

    for t in tests:
        st = time.perf_counter()
        print(t, t2)
        print(" union: {}\n intersection: {}\n difference: {}"
              .format(t.unite(t2), t.intersect(t2), t.diff(t2)))
        print(t.is_subset(t3))
        end = time.perf_counter() - st
        print("{:.8f} ==========================".format(end))


