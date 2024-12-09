import numpy as np

# City coordinates as provided
city_coordinates = np.array([
    [2.7933, 3.694], [2.6067, 4.4254], [2.86, 5.0373], [2.54, 6.2463],
    [3.1267, 6.4701], [3.7267, 6.8881], [4.4867, 7.4403], [5.5533, 7.4254],
    [6.3, 7.3955], [7.6333, 6.9179], [7.22, 6.3955], [6.6333, 5.8284],
    [7.0867, 5.1269], [7.4733, 4.4701], [7.18, 3.709], [6.6867, 2.8284],
    [6.2067, 2.0522], [5.54, 1.8731], [5.1533, 2.3358], [4.9667, 3.0075],
    [4.8867, 3.5448], [4.2733, 3.2313], [3.6333, 2.7537], [2.9933, 2.8433]
])

# Number of cities
num_cities = len(city_coordinates)

# Function to calculate the Euclidean distance between two points (cities)
def euclidean_distance(city1, city2):
    return np.sqrt(np.sum((city1 - city2) ** 2))

# Function to calculate the total distance (cost) of a solution (tour)
def total_distance(tour, city_coordinates):
    distance = 0.0
    for i in range(len(tour) - 1):
        distance += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    # Add the distance to return to the starting city
    distance += euclidean_distance(city_coordinates[tour[-1]], city_coordinates[tour[0]])
    return distance

# Step 1: Generate a random initial solution (tour)
initial_tour = np.random.permutation(num_cities)

# Step 2: Neighbourhood operator: Swap two adjacent cities in the tour
def swap_adjacent_cities(tour):
    new_tour = np.copy(tour)
    # Randomly choose two adjacent cities to swap
    idx = np.random.randint(0, num_cities - 1)
    new_tour[idx], new_tour[idx + 1] = new_tour[idx + 1], new_tour[idx]
    return new_tour

# Step 4: Run the Steepest Ascent Hill Climbing Algorithm
def steepest_ascent_hill_climbing(city_coordinates, max_no_improvement_iters=100):
    current_tour = np.random.permutation(num_cities)  # Start with a random tour
    current_cost = total_distance(current_tour, city_coordinates)  # Calculate the initial cost
    no_improvement_count = 0
    iteration = 0

    while no_improvement_count < max_no_improvement_iters:
        # Explore neighbourhood: Generate neighbouring solutions and evaluate them
        best_neighbour = None
        best_cost = current_cost
        for _ in range(50):  # Try 50 different neighbours
            new_tour = swap_adjacent_cities(current_tour)
            new_cost = total_distance(new_tour, city_coordinates)
            if new_cost < best_cost:
                best_neighbour = new_tour
                best_cost = new_cost

        # If the best neighbour is better than the current solution, update the current solution
        if best_neighbour is not None:
            current_tour = best_neighbour
            current_cost = best_cost
            no_improvement_count = 0  # Reset no improvement count
        else:
            no_improvement_count += 1  # No better neighbour found

        iteration += 1

    return current_tour, current_cost, iteration

# Run the algorithm and get the results
final_tour, final_cost, iterations_taken = steepest_ascent_hill_climbing(city_coordinates)

print(f"Final Tour: {final_tour}")
print(f"Final Cost (Total Distance): {final_cost}")
print(f"Iterations Taken: {iterations_taken}")
