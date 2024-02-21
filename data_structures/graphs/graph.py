# builds a undirected graph
class Graph:
    def __init__(self):
        self.nodes = {}

    @staticmethod
    def from_edge_list(edge_list: list):
        graph = Graph()
        for edge in edge_list:
            node_1, node_2 = edge
            if node_1 in graph.nodes.keys():
                graph.nodes[node_1].append(node_2)
            else:
                graph.nodes[node_1] = [node_2]
            if node_2 in graph.nodes.keys():
                graph.nodes[node_2].append(node_1)
            else:
                graph.nodes[node_2] = [node_1]
        return graph

    def add_node(self, node):
        if not node in self.nodes.keys():
            self.nodes[node] = []
    def add_edge_list(self, edge_list):
        for edge in edge_list:
            node_1, node_2 = edge
            if node_1 in self.nodes.keys():
                self.nodes[node_1].append(node_2)
            else:
                self.nodes[node_1] = [node_2]
            if node_2 in self.nodes.keys():
                self.nodes[node_2].append(node_1)
            else:
                self.nodes[node_2] = [node_1]
    def add_edge(self, edge):
        if not isinstance(edge, list): return
        if len(edge) != 2: return

        node_1, node_2 = edge
        if node_1 in self.nodes.keys():
            self.nodes[node_1].append(node_2)
        else:
            self.nodes[node_1] = [node_2]
        if node_2 in self.nodes.keys():
            self.nodes[node_2].append(node_1)
        else:
            self.nodes[node_2] = [node_1]

    #bfs
    def shortest_path(self, start: str, data: str):
        if start == data: return [start]
        queue = [start]
        visited = set(queue)
        path = []
        while len(queue) > 0:
            print(queue, path)
            cur_node = queue.pop(0)
            edges = self.nodes[cur_node]
            path.append(cur_node)
            for n in edges:
                if n in visited:
                    continue
                if n == data:
                    path.append(n)
                    return path
                visited.add(n)
                queue.append(n)
        return None

    def has(self, data: str):
        return data in self.nodes.keys()

    # dfs
    def has_path(self, start: str, data: str):
        if start == data: return True
        stack = [start]
        visited = set(stack)
        path = []
        while len(stack) > 0:
            print(stack, path)
            cur_node = stack.pop(-1)
            edges = self.nodes[cur_node]
            path.append(cur_node)
            for n in edges:
                if n in visited:
                    continue
                if n == data:
                    path.append(n)
                    return (path)
                    return True
                visited.add(n)
                stack.append(n)
        return False

    def print(self):
        print(f"{self.nodes}")


if __name__ == "__main__":
    edge_list = [
            ['1', '2'],
            ['2', '3'],
            ['3', '4'],
            ['1', '4'],
            ['4', '5'],
            ['7', '8'],
            ['3', '7'],
            ['5', '7'],
            ['2', '9'],
            ];

    graph = Graph.from_edge_list(edge_list)

    graph.print()
    print(graph.shortest_path('1', '9')) # 1 -> 2 -> 4 -> 5 || 1 -> 4 -> 5
    print(graph.has_path('1', '9')) # 1 -> 2 -> 4 -> 5 || 1 -> 4 -> 5
