# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Set to keep track of visited nodes
visited = set()

# DFS function
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)

        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)


# Starting DFS from node A
print("Depth-First Search:")
dfs(visited, graph, 'A')