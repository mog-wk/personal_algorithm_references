

def dfs(graph, el):
    visited = set()
    # handles directed graph and islands
    for i in graph.keys():
        stack = [i]
        if i in visited:
            continue
        while len(stack) != 0:
            cur = stack.pop()
            if cur == el:
                return True
            print(cur)
            if cur not in graph:
                continue
            neighbors = graph[cur]
            for node in neighbors:
                if node not in visited:
                    visited.add(node)
                    stack.append(node)


    return False



if __name__ == "__main__":
    tests = [
        { "A": ["B", "C", "D"], "B": ["D"], "C": ["F"], "D": ["E"], "E": ["F"], },
        { "A": ["B", "H", "G"], "B": ["C", "E"], "C": ["D"], "E": ["D"], "F": ["E"], "H": ["E"], "G": ["H", "F"], },
        ];

    for t in tests:
        print(dfs(t, "F"))
        print(dfs(t, "A"))

