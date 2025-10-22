# brute force approach

from itertools import permutations

# Number of cities
N = 4

# Distance matrix
# Example: distance[i][j] = cost to go from city i to city j
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def travelling_salesman(graph, start):
    # Store all vertices except the start city
    cities = [i for i in range(len(graph)) if i != start]

    min_path = float('inf')
    best_route = []

    # Generate all possible permutations of cities
    for perm in permutations(cities):
        # Calculate current path weight
        current_cost = 0
        k = start
        for j in perm:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][start]  # return to start

        # Update minimum
        if current_cost < min_path:
            min_path = current_cost
            best_route = (start,) + perm + (start,)

    print("Minimum cost Hamiltonian Cycle:", " -> ".join(map(str, best_route)))
    print("Minimum Cost:", min_path)


if __name__ == "__main__":
    travelling_salesman(distance, 0)
