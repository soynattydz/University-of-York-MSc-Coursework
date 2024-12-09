import matplotlib.pyplot as plt

def simulated_annealing_with_plot():
    current_solution = random_solution()
    best_solution = current_solution[:]
    current_temperature = initial_temperature
    values_over_time = []
    
    for iteration in range(max_iterations):
        # Generate a neighboring solution by flipping a random item
        new_solution = current_solution[:]
        flip_index = random.randint(0, len(weights) - 1)
        new_solution[flip_index] = 1 - new_solution[flip_index]  # Flip 0 to 1 or 1 to 0

        new_weight, new_value = knapsack_value(new_solution)
        
        if new_weight <= capacity:
            _, current_value = knapsack_value(current_solution)
            if new_value > current_value:
                current_solution = new_solution
                if new_value > knapsack_value(best_solution)[1]:
                    best_solution = new_solution
            else:
                acceptance_prob = math.exp((new_value - current_value) / current_temperature)
                if random.random() < acceptance_prob:
                    current_solution = new_solution

        values_over_time.append(knapsack_value(best_solution)[1])
        current_temperature *= cooling_rate
        
    return best_solution, knapsack_value(best_solution), values_over_time

# Running the Simulated Annealing algorithm with plotting
solution, (weight, value), values_over_time = simulated_annealing_with_plot()

# Plotting the progress of simulated annealing
plt.plot(values_over_time, label="Simulated Annealing")
plt.xlabel("Iterations")
plt.ylabel("Best Value")
plt.title("Simulated Annealing Progress")
plt.legend()
plt.show()
