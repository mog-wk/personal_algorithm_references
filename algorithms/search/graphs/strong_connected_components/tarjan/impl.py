
def dfs(graph, start):
    visited = set()

    stack = [start] # start at a arbitrary node
    while len(stack) != 0:
        cur = stack.pop()
        print(cur, visited)
        if cur not in graph.keys():
            print(cur)
            visited.add(cur)
            continue

        neighbors = graph[cur]
        for node in neighbors:
            if node not in visited:
                visited.add(node)
                stack.append(node)
    return len(visited)

# kosaraju
def has_scc(graph, start):
    graph_len = len(graph)
    return (dfs(graph, start) == graph_len and dfs(rev(graph), start) == graph_len)

def rev(graph):
    rev_graph = {k: [] for k in graph.keys()}
    for k in graph.keys():
        print("asdasd", rev_graph);
        for n in graph[k]:
            if n in rev_graph.keys():
                rev_graph[n].append(k) 
            else:
                rev_graph[n] = []
    return rev_graph


if __name__ == "__main__":
    tests = [
        { "A": ["B", "C", "D"], "B": ["D"], "C": ["F"], "D": ["E"], "E": ["F"], },
        #{ "A": ["B", "H", "G"], "B": ["C", "E"], "C": ["D"], "E": ["D"], "F": ["E"], "H": ["E"], "G": ["H", "F"], },
        { "A": ["B"], "B": ["C"], "C": ["D", "E"], "D": ["A"], "E": ["C"] },
        ];

    for t in tests:
        print(has_scc(t, "A"))

