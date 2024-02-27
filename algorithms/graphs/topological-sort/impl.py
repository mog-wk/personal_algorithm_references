
def topological_sort(graph, start_node):
    sorted_list = []
    visited = set()

    for i in graph.keys():
        stack = [i]
        if i in visited or len(graph[i]) == 0:
            continue
        print(sorted_list)
        while len(stack) != 0:
            cur = stack.pop()
            if cur not in graph:
                # assume node with 0 out-degree
                sorted_list.append(cur)
                continue
            neighbors = graph[cur]
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

            sorted_list.append(cur)

    return sorted_list

def shortest_path_in_dag(graph, start_node):
    order = topological_sort(graph, start_node)
    for node in order:
        # djikstra
        pass

if __name__ == "__main__":
    tests = [
        #{ "A": ["B", "C", "D"], "B": ["D"], "C": ["F"], "D": ["E"], "E": ["F"], },
        #{ "A": ["B", "H", "G"], "B": ["C", "E"], "C": ["D"], "E": ["D"], "F": ["E"], "H": ["E"], "G": ["H", "F"], },
        { "5": ["2", "0"], "0": [], "4": ["0", "1"], "2": ["3"], "3": ["1"], "1": [] },
        { "4": ["0", "1"], "5": ["2", "0"], "0": [], "1": [], "2": ["3"], "3": ["1"],  },
        ];

    for t in tests:
        print(topological_sort(t, "5"))
