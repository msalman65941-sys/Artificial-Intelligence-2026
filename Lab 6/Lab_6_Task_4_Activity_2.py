# Binary tree represented as a dictionary
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# DFS function
def dfs(tree, node):
    print(node)

    for child in tree[node]:
        dfs(tree, child)


# Start DFS from root node A
print("Depth-First Search:")
dfs(tree, 'A')