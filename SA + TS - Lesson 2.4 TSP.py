import numpy as np
import random
import math

# Example TSP distance matrix from your problem (8 cities)
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

def get_neighbor(route):
    """Generate a neighboring solution by swapping two cities."""
    new_route = route[:]
    i, j = random.sample(range(len(route)), 2)  # Select two random cities
    new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route

def acceptance_probability(delta_e, temperature):
    """Simulated annealing probability calculation."""
    if delta_e < 0:
        return 1
    else:
        return math.exp(-delta_e / temperature)

def tabu_search_sa(initial_route, matrix, max_iterations=1000, initial_temp=1000, cooling_rate=0.995, tabu_tenure=5):
    """Combined Tabu Search and Simulated Annealing."""
    current_route = initial_route[:]
    current_cost = calculate_total_distance(current_route, matrix)
    
    # Tabu List (stores tuples of city pairs)
    tabu_list = []
    
    best_route = current_route[:]
    best_cost = current_cost
    temperature = initial_temp
    
    for iteration in range(max_iterations):
        # Generate a neighbor solution
        neighbor_route = get_neighbor(current_route)
        neighbor_cost = calculate_total_distance(neighbor_route, matrix)
        
        delta_e = neighbor_cost - current_cost
        
        # Simulated Annealing part: Decide whether to accept the move
        if acceptance_probability(delta_e, temperature) > random.random():
            current_route = neighbor_route
            current_cost = neighbor_cost
        
        # Tabu Search part: Avoid moves that are in the Tabu List
        move = tuple(sorted((neighbor_route[0], neighbor_route[1])))  # Store city pair as a tuple
        if move not in tabu_list:
            if neighbor_cost < best_cost:  # Update best solution
                best_route = neighbor_route
                best_cost = neighbor_cost
            tabu_list.append(move)  # Add move to Tabu List
            if len(tabu_list) > tabu_tenure:  # Remove oldest item if Tabu List is full
                tabu_list.pop(0)
        
        # Cool down temperature
        temperature *= cooling_rate
    
    return best_route, best_cost

# Example initial route (cities indexed from 0)
initial_route = [0, 1, 2, 3, 4, 5, 6, 7]

# Run the combined Simulated Annealing + Tabu Search algorithm
best_route, best_cost = tabu_search_sa(initial_route, distance_matrix)

print(f"Best Route: {best_route}, Best Cost: {best_cost}")
