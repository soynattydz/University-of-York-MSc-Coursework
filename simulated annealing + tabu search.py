import random
import math
from collections import deque
import matplotlib.pyplot as plt

# Knapsack problem parameters
weights = [21, 12, 30, 24, 45, 47, 41, 36, 38, 45, 4, 17, 1, 42, 26, 19, 12, 27, 15, 4, 5, 4, 21, 7, 23, 45, 18, 7, 29, 44, 18, 3, 8, 4, 38, 23, 34, 35, 29, 32, 44, 34, 44, 24, 8, 4, 36, 16, 34, 33, 27, 36, 26, 25, 25, 47, 20, 6, 13, 35, 42, 49, 11, 39, 30, 21, 26, 25, 33, 38, 16, 5, 42, 20, 39, 9, 6, 46, 44, 50, 44, 2, 28, 50, 26, 44, 4, 50, 47, 29, 22, 17, 37, 1, 19, 47, 28, 24, 25, 16]
values = [96, 99, 52, 100, 46, 43, 22, 20, 84, 73, 53, 83, 52, 56, 22, 59, 15, 6, 69, 61, 22, 41, 63, 56, 13, 17, 1, 42, 49, 16, 67, 2, 12, 96, 98, 4, 50, 87, 25, 84, 82, 63, 1, 38, 91, 69, 38, 64, 25, 58, 99, 85, 29, 69, 36, 99, 9, 26, 82, 9, 54, 81, 74, 15, 44, 36, 48, 59, 15, 91, 65, 17, 57, 94, 79, 69, 47, 27, 57, 25, 32, 92, 89, 80, 93, 18, 52, 63, 92, 67, 39, 75, 82, 61, 9, 93, 6, 53, 12, 39]
capacity = 1500

# Function to calculate total weight and value of the selected items
def knapsack_value(solution):
    total_weight = sum(weights[i] for i in range(len(solution)) if solution[i] == 1)
    total_value = sum(values[i] for i in range(len(solution)) if solution[i] == 1)
    return total_weight, total_value

# Function to generate a random initial solution
def random_solution():
    solution = [random.randint(0, 1) for _ in range(len(weights))]
    while knapsack_value(solution)[0] > capacity:
        solution = [random.randint(0, 1) for _ in range(len(weights))]
    return solution

# Simulated Annealing Algorithm with iteration count
def simulated_annealing():
    initial_temperature = 1000
    cooling_rate = 0.995
    max_iterations = 1000
    threshold = 10  # Stop if no improvement in 10 iterations
    current_solution = random_solution()
    best_solution = current_solution[:]
    current_temperature = initial_temperature
    convergence_values = []
    iteration_count = 0
    no_improvement_count = 0
    
    for iteration in range(max_iterations):
        iteration_count += 1
        new_solution = current_solution[:]
        flip_index = random.randint(0, len(weights) - 1)
        new_solution[flip_index] = 1 - new_solution[flip_index]

        new_weight, new_value = knapsack_value(new_solution)
        if new_weight <= capacity:
            _, current_value = knapsack_value(current_solution)
            if new_value > current_value:
                current_solution = new_solution
                if new_value > knapsack_value(best_solution)[1]:
                    best_solution = new_solution
                    no_improvement_count = 0  # Reset if improvement
            else:
                acceptance_prob = math.exp((new_value - current_value) / current_temperature)
                if random.random() < acceptance_prob:
                    current_solution = new_solution
        
        current_temperature *= cooling_rate
        convergence_values.append(knapsack_value(current_solution)[1])  # Track convergence
        
        # Stop if no improvement in the last 'threshold' iterations
        no_improvement_count += 1
        if no_improvement_count >= threshold:
            break

    return best_solution, knapsack_value(best_solution), iteration_count, convergence_values


# Tabu Search Algorithm with iteration count
def tabu_search():
    tabu_size = 10
    num_iterations = 1000
    threshold = 10  # Stop if no improvement in 10 iterations
    current_solution = random_solution()
    best_solution = current_solution[:]
    tabu_list = deque(maxlen=tabu_size)
    convergence_values = []
    iteration_count = 0
    no_improvement_count = 0

    for iteration in range(num_iterations):
        iteration_count += 1
        neighbors = []
        for i in range(len(weights)):
            neighbor = current_solution[:]
            neighbor[i] = 1 - neighbor[i]
            neighbors.append(neighbor)

        valid_neighbors = [n for n in neighbors if knapsack_value(n)[0] <= capacity]
        best_neighbor = None
        best_value = 0
        for neighbor in valid_neighbors:
            if neighbor not in tabu_list:
                _, neighbor_value = knapsack_value(neighbor)
                if neighbor_value > best_value:
                    best_neighbor = neighbor
                    best_value = neighbor_value

        if best_neighbor:
            current_solution = best_neighbor
            tabu_list.append(current_solution)
            if best_value > knapsack_value(best_solution)[1]:
                best_solution = current_solution
                no_improvement_count = 0  # Reset if improvement

        convergence_values.append(knapsack_value(current_solution)[1])  # Track convergence
        
        # Stop if no improvement in the last 'threshold' iterations
        no_improvement_count += 1
        if no_improvement_count >= threshold:
            break

    return best_solution, knapsack_value(best_solution), iteration_count, convergence_values

# Running each algorithm 10 times and recording the results
tabu_values = []
annealing_values = []
tabu_convergence = []
annealing_convergence = []
tabu_iterations = []
annealing_iterations = []

print("Tabu Search Results:")
for run in range(10):
    solution, (weight, value), iterations, convergence = tabu_search()
    tabu_values.append(value)
    tabu_convergence.append(convergence)
    tabu_iterations.append(iterations)
    print(f"Run {run+1}: Weight = {weight}, Value = {value}, Iterations = {iterations}")

print("\nSimulated Annealing Results:")
for run in range(10):
    solution, (weight, value), iterations, convergence = simulated_annealing()
    annealing_values.append(value)
    annealing_convergence.append(convergence)
    annealing_iterations.append(iterations)
    print(f"Run {run+1}: Weight = {weight}, Value = {value}, Iterations = {iterations}")

# Plotting results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot for Tabu Search
ax1.plot(range(1, 11), tabu_values, marker='o')
ax1.set_title("Tabu Search: Values Across 10 Runs")
ax1.set_xlabel("Run")
ax1.set_ylabel("Knapsack Value")
ax1.set_ylim([min(tabu_values) - 50, max(tabu_values) + 50])

# Plot for Simulated Annealing
ax2.plot(range(1, 11), annealing_values, marker='o')
ax2.set_title("Simulated Annealing: Values Across 10 Runs")
ax2.set_xlabel("Run")
ax2.set_ylabel("Knapsack Value")
ax2.set_ylim([min(annealing_values) - 50, max(annealing_values) + 50])

plt.tight_layout()
plt.show()

# Convergence Plot for Tabu Search
plt.figure(figsize=(10, 6))
for i, convergence in enumerate(tabu_convergence):
    plt.plot(convergence, label=f'Tabu Run {i+1}')
plt.title('Tabu Search Convergence')
plt.xlabel('Iteration')
plt.ylabel('Knapsack Value')
plt.legend()
plt.show()

# Convergence Plot for Simulated Annealing
plt.figure(figsize=(10, 6))
for i, convergence in enumerate(annealing_convergence):
    plt.plot(convergence, label=f'Annealing Run {i+1}')
plt.title('Simulated Annealing Convergence')
plt.xlabel('Iteration')
plt.ylabel('Knapsack Value')
plt.legend()
plt.show()