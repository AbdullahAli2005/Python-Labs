# Using Breath First Search

from collections import deque

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

def bfs_with_closed(graph, start, goal):
    queue = deque([start])
    closed = set()

    while queue:
        node = queue.popleft()
        if node == goal:
            return True  

        if node not in closed:
            closed.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in closed:
                    queue.append(neighbor)
    return False

print("BFS with Closed:", bfs_with_closed(graph, 'S', 'F'))
