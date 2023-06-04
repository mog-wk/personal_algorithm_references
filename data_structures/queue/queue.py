
class Queue:
    def __init__(self, arr):
        self.contents = []
        self.len = 0

        for elt in arr:
            self.contents.append(elt)
            self.len += 1


    def display(self) -> str:
        return "{} ".format([elt for elt in self.contents])

    def peek(self, n: int = 1):
        if n < 0:
            n *= -1
        return self.contents[:-n]

    def dequeue(self):
        return self.contents.pop(0)

    def add(self, n):
        self.contents.append(n)

    def extend(self, ls: list):
        self.contents.extend(ls)

    def has(self, elt) -> bool:
        return elt in self.contents


if __name__ == "__main__":
    tests = [
            Queue([1, 2, 3, 4, 5]),
            Queue([12, 23, 5, 51, 5]),
            Queue([]),
            Queue([3, 4, 5, ["arr"], "str"]),
            ]

    for i, test in enumerate(tests):
        print("{} => {}".format(i, test.display()))


