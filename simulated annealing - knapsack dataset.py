import random
import math

# Data: weights and values
weights = [21, 12, 30, 24, 45, 47, 41, 36, 38, 45, 4, 17, 1, 42, 26, 19, 12, 27, 15, 4, 5, 4, 21, 7, 23, 45, 18, 7, 29, 44, 18, 3, 8, 4, 38, 23, 34, 35, 29, 32, 44, 34, 44, 24, 8, 4, 36, 16, 34, 33, 27, 36, 26, 25, 25, 47, 20, 6, 13, 35, 42, 49, 11, 39, 30, 21, 26, 25, 33, 38, 16, 5, 42, 20, 39, 9, 6, 46, 44, 50, 44, 2, 28, 50, 26, 44, 4, 50, 47, 29, 22, 17, 37, 1, 19, 47, 28, 24, 25, 16]
values = [96, 99, 52, 100, 46, 43, 22, 20, 84, 73, 53, 83, 52, 56, 22, 59, 15, 6, 69, 61, 22, 41, 63, 56, 13, 17, 1, 42, 49, 16, 67, 2, 12, 96, 98, 4, 50, 87, 25, 84, 82, 63, 1, 38, 91, 69, 38, 64, 25, 58, 99, 85, 29, 69, 36, 99, 9, 26, 82, 9, 54, 81, 74, 15, 44, 36, 48, 59, 15, 91, 65, 17, 57, 94, 79, 69, 47, 27, 57, 25, 32, 92, 89, 80, 93, 18, 52, 63, 92, 67, 39, 75, 82, 61, 9, 93, 6, 53, 12, 39]

capacity = 1500
initial_temperature = 1000
cooling_rate = 0.995
max_iterations = 10000

# Function to calculate the total weight and value of the selected items
def knapsack_value(solution):
    total_weight = sum(weights[i] for i in range(len(solution)) if solution[i] == 1)
    total_value = sum(values[i] for i in range(len(solution)) if solution[i] == 1)
    return total_weight, total_value

# Function to generate a random initial solution
def random_solution():
    solution = [random.randint(0, 1) for _ in range(len(weights))]
    while knapsack_value(solution)[0] > capacity:  # Ensure initial solution fits
        solution = [random.randint(0, 1) for _ in range(len(weights))]
    return solution

# Simulated Annealing Algorithm
def simulated_annealing():
    current_solution = random_solution()
    best_solution = current_solution[:]
    current_temperature = initial_temperature
    
    for iteration in range(max_iterations):
        # Generate a neighboring solution by flipping a random item
        new_solution = current_solution[:]
        flip_index = random.randint(0, len(weights) - 1)
        new_solution[flip_index] = 1 - new_solution[flip_index]  # Flip 0 to 1 or 1 to 0

        # Calculate the total weight and value of the new solution
        new_weight, new_value = knapsack_value(new_solution)
        
        if new_weight <= capacity:
            # Check if the new solution is better, or accept it with a probability based on temperature
            _, current_value = knapsack_value(current_solution)
            if new_value > current_value:
                current_solution = new_solution
                if new_value > knapsack_value(best_solution)[1]:
                    best_solution = new_solution
            else:
                acceptance_prob = math.exp((new_value - current_value) / current_temperature)
                if random.random() < acceptance_prob:
                    current_solution = new_solution

        # Cool down the temperature
        current_temperature *= cooling_rate
        
    return best_solution, knapsack_value(best_solution)

# Running the Simulated Annealing algorithm
solution, (weight, value) = simulated_annealing()
print(f"Simulated Annealing Solution: Weight = {weight}, Value = {value}")
