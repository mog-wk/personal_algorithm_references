
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

def topological_sort_II(graph):
    visited = set()
    stack = []
    for i in graph.keys():
        if i not in visited:
            topological_sort_II_util(graph, i, visited, stack)
    return stack[::-1];

def topological_sort_II_util(graph, index, visited, stack):
    visited.add(index)
    print(visited)
    for i in graph[index]:
        if i not in visited:
            topological_sort_II_util(graph, index, visited, stack)
    stack.append(index)

if __name__ == "__main__":
    tests = [
        #{ "A": ["B", "C", "D"], "B": ["D"], "C": ["F"], "D": ["E"], "E": ["F"], },
        #{ "A": ["B", "H", "G"], "B": ["C", "E"], "C": ["D"], "E": ["D"], "F": ["E"], "H": ["E"], "G": ["H", "F"], },
        { "5": ["2", "0"], "0": [], "4": ["0", "1"], "2": ["3"], "3": ["1"], "1": [] },
        { "4": ["0", "1"], "5": ["2", "0"], "0": [], "1": [], "2": ["3"], "3": ["1"],  },
        ];

    for t in tests:
        #print(topological_sort(t, "5"))
        print(topological_sort_II(t))

