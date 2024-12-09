import random
from collections import deque

# Knapsack problem parameters
weights = [21, 12, 30, 24, 45, 47, 41, 36, 38, 45, 4, 17, 1, 42, 26, 19, 12, 27, 15, 4, 5, 4, 21, 7, 23, 45, 18, 7, 29, 44, 18, 3, 8, 4, 38, 23, 34, 35, 29, 32, 44, 34, 44, 24, 8, 4, 36, 16, 34, 33, 27, 36, 26, 25, 25, 47, 20, 6, 13, 35, 42, 49, 11, 39, 30, 21, 26, 25, 33, 38, 16, 5, 42, 20, 39, 9, 6, 46, 44, 50, 44, 2, 28, 50, 26, 44, 4, 50, 47, 29, 22, 17, 37, 1, 19, 47, 28, 24, 25, 16]
values = [96, 99, 52, 100, 46, 43, 22, 20, 84, 73, 53, 83, 52, 56, 22, 59, 15, 6, 69, 61, 22, 41, 63, 56, 13, 17, 1, 42, 49, 16, 67, 2, 12, 96, 98, 4, 50, 87, 25, 84, 82, 63, 1, 38, 91, 69, 38, 64, 25, 58, 99, 85, 29, 69, 36, 99, 9, 26, 82, 9, 54, 81, 74, 15, 44, 36, 48, 59, 15, 91, 65, 17, 57, 94, 79, 69, 47, 27, 57, 25, 32, 92, 89, 80, 93, 18, 52, 63, 92, 67, 39, 75, 82, 61, 9, 93, 6, 53, 12, 39]
capacity = 1500

# Function to generate a random solution
def random_solution():
    return [random.randint(0, 1) for _ in range(len(weights))]

# Function to calculate the total weight and value of a solution
def knapsack_value(solution):
    total_weight = sum(weights[i] for i in range(len(solution)) if solution[i] == 1)
    total_value = sum(values[i] for i in range(len(solution)) if solution[i] == 1)
    return total_weight, total_value

# Tabu Search parameters
tabu_size = 10
num_iterations = 1000

# Tabu Search Algorithm
def tabu_search():
    current_solution = random_solution()
    best_solution = current_solution[:]
    tabu_list = deque(maxlen=tabu_size)
    
    for iteration in range(num_iterations):
        neighbors = []
        
        # Generate neighbors by flipping each item once
        for i in range(len(weights)):
            neighbor = current_solution[:]
            neighbor[i] = 1 - neighbor[i]  # Flip the item
            neighbors.append(neighbor)

        # Filter neighbors that exceed the capacity
        valid_neighbors = [n for n in neighbors if knapsack_value(n)[0] <= capacity]
        
        # Find the best neighbor not in the tabu list
        best_neighbor = None
        best_value = 0
        
        for neighbor in valid_neighbors:
            if neighbor not in tabu_list:
                _, neighbor_value = knapsack_value(neighbor)
                if neighbor_value > best_value:
                    best_neighbor = neighbor
                    best_value = neighbor_value
        
        # Update the solution and tabu list
        if best_neighbor:
            current_solution = best_neighbor
            tabu_list.append(current_solution)
            if best_value > knapsack_value(best_solution)[1]:
                best_solution = current_solution

    return best_solution, knapsack_value(best_solution)

# Running the Tabu Search algorithm
solution, (weight, value) = tabu_search()
print(f"Tabu Search Solution: Weight = {weight}, Value = {value}")
