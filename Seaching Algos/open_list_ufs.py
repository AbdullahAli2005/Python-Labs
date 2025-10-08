import heapq

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

def uniform_cost_search(graph, start, goal):
    open_list = [(0, start)]  
    visited = {}

    while open_list:
        cost, node = heapq.heappop(open_list)

        if node == goal:
            return cost  

        if node not in visited or cost < visited[node]:
            visited[node] = cost
            for neighbor, weight in graph.get(node, []):
                heapq.heappush(open_list, (cost + weight, neighbor))
    return float("inf")  

print("Uniform Cost Search:", uniform_cost_search(graph, 'S', 'F'))