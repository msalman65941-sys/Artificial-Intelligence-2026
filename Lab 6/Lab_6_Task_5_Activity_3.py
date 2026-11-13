graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C', 'I'],
    'H': ['E'],
    'I': ['G']
}


def dfs_path(graph, start, end, visited=None, path=None):

    if visited is None:
        visited = set()

    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    # If ending node is reached
    if start == end:
        return path

    # Visit all neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs_path(graph, neighbor, end, visited, path)

            if result is not None:
                return result

    # Backtrack
    path.pop()
    return None


# Starting and ending nodes
start = 'A'
end = 'I'

result = dfs_path(graph, start, end)

if result:
    print("Path found:")
    print(" -> ".join(result))
else:
    print("No path found.")