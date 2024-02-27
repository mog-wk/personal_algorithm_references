
class Graph:
    def __init__(self, nodes: dict, directed=True):
        self.nodes = nodes
        self.len = len(nodes.keys())
        self.directed = directed

    @staticmethod
    def from_edgelist(edgelist: list, directed=True):
        nodes = dict()
        if directed:
            for edge in edgelist:
                parent, child, weight = edge
                if parent in nodes.keys():
                    nodes[parent].append((child, weight))
                else:
                    nodes[parent] = [(child, weight)]
        else:
            for edge in edgelist:
                parent, child, weight = edge
                if parent in nodes.keys():
                    nodes[parent].append((child, weight))
                else:
                    nodes[parent] = [(child, weight)]
                if child in nodes.keys():
                    nodes[child].append((parent, weight))
                else:
                    nodes[child] = [(parent, weight)]

        return Graph(nodes, directed=directed)

    def __str__(self):
        st = ""
        counter = 0
        for k in self.nodes:
            st += "{:0} | {}: {}\n".format(counter, k, self.nodes[k])
            counter += 1
        return st

    def minimun_spanning_tree(self, start):
        visited = set()
        frontier = set()
        tree = [start]
        while len(tree) != self.len:
            cur = tree[-1]
            if cur in visited:
                continue
            visited.add(cur)

            for node, weight in self.nodes[cur]:
                if node not in visited:
                    frontier.add((node, weight))

            next_node = cur
            min_weight = 10000
            for node, weight in frontier:
                if node not in visited:
                    if weight < min_weight:
                        min_weight = weight
                        next_node = node
            if not min_weight == 10000:
                frontier.remove((next_node, min_weight))
                tree.append(next_node)
            else:
                # TODO: proper cycle handleing
                return tree

        return tree


tests_edgelists = [
        [ ["A", "B", 4], ["A", "C", 1], ["C", "F", 12], ["E", "F", 8], ["A", "D", 5], ["D", "E", 3], ["B", "D", 3] ],
        [
            ["A", "B", 4], ["B", "C", 8], ["C", "D", 7], ["D", "E", 9], ["E", "F", 10], ["F", "G", 2], ["G", "H", 1],
            ["H", "I", 7], ["H", "A", 8], ["H", "B", 11], ["G", "I", 6], ["C", "F", 4], ["C", "I", 2], ["D", "F", 14],
        ],
        [ ["A", "B", 4], ["A", "C", 1], ["E", "F", 8], ["A", "D", 5], ["B", "D", 3] ],
        ]

tests_graphs = [Graph.from_edgelist(i, directed=False) for i in tests_edgelists]

for test in tests_graphs:
    print("testing =====================")
    print(test)
    print(test.minimun_spanning_tree("A"))
