# Using Depth First Search
import random

graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': ['F'],
    'D': ['F', 'G'],
    'E': ['G'],
    'F': [],
    'G': []
}

def random_dfs(graph, start, goal):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node == goal:
            return True 

        if node not in visited:
            visited.add(node)
            neighbors = list(graph.get(node, []))
            random.shuffle(neighbors)  
            stack.extend(neighbors)
    return False

print("Random DFS:", random_dfs(graph, 'S', 'F'))

# Visualization
#      S
#     / \
#    A   B
#   / \   \
#  C   D   E
#  |  / \   \
#  F F   G   G
