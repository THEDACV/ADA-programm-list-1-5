import itertools

def tsp(graph):
    cities = list(graph.keys())
    # Generate all possible routes (permutations of cities excluding the first one)
    return min(
        (sum(graph[cities[0]][current[0]] +  # Distance from starting city to first city in permutation
              sum(graph[current[i]][current[i + 1]] for i in range(len(current) - 1)) +  # Sum distances between cities in permutation
              graph[current[-1]][cities[0]],  # Distance from last city back to starting city
              current)
         for current in itertools.permutations(cities[1:])),  # Permute remaining cities
        key=lambda x: x[0]
    )

# Example graph
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

cost, route = tsp(graph)
print("Best route:", ['A'] + list(route) + ['A'])
print("Minimum cost:", cost)