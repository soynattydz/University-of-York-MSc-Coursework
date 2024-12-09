import numpy as np

# TSP distance matrix problem (8 interconnected cities)
distance_matrix = np.array([
    [0, 1, 3, 2, 2, 3, 5, 2],
    [1, 0, 4, 4, 4, 4, 4, 6],
    [3, 4, 0, 3, 2, 1, 1, 3],
    [2, 4, 3, 0, 1, 4, 3, 5],
    [2, 4, 2, 1, 0, 4, 4, 4],
    [3, 4, 1, 4, 4, 0, 1, 2],
    [5, 4, 1, 3, 4, 1, 0, 1],
    [2, 6, 3, 5, 4, 2, 1, 0]
])

def calculate_total_distance(route, matrix):
    """Calculate the total distance of the route."""
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += matrix[route[i]][route[i + 1]]
    # Add the distance to return to the start city
    total_distance += matrix[route[-1]][route[0]]
    return total_distance

def two_opt(route, matrix):
    """Perform the 2-opt algorithm to improve the route."""
    best_route = route
    best_distance = calculate_total_distance(route, matrix)
    
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # Skip adjacent nodes, no need to swap
                new_route = route[:]
                # Reverse the order of cities between i and j
                new_route[i:j] = route[i:j][::-1]
                new_distance = calculate_total_distance(new_route, matrix)
                if new_distance < best_distance:
                    best_route = new_route
                    best_distance = new_distance
                    improvement = True
        route = best_route  # Set the best route found so far
    return best_route, best_distance

# Example initial route from Nearest Neighbour Heuristic
initial_route = [0, 2, 5, 6, 4, 1, 7, 3, 0]  # Example route (cities 0-indexed)

# Perform 2-opt to improve the route
improved_route, improved_distance = two_opt(initial_route, distance_matrix)

print(f"Initial Route: {initial_route}, Initial Distance: {calculate_total_distance(initial_route, distance_matrix)}")
print(f"Improved Route: {improved_route}, Improved Distance: {improved_distance}")
