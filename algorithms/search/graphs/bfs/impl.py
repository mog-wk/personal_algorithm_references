

def bfs(graph, start, el):
    queue = [start]
    visited = set(start)

    while len(queue) != 0:
        cur = queue.pop(0)
        print(cur, queue, visited)
        if cur == el:
            return True
        if not cur in graph:
            continue
        neighbors = graph[cur]
        for node in neighbors:
            if not node in visited:
                queue.append(node)
                visited.add(node)


    return False


def grapH_from_edge_list(edge_l: list):
    pass

if __name__ == "__main__":
    tests = [
        { "A": ["B", "C", "D"], "B": ["D"], "C": ["F"], "D": ["E"], "E": ["F"], },
        { "A": ["B", "H", "G"], "B": ["C", "E"], "C": ["D"], "E": ["D"], "F": ["E"], "H": ["E"], "G": ["H", "F"], },
        ];

    for t in tests:
        print(bfs(t, "A", "F"))

