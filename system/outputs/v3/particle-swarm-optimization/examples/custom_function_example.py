from pso.pso import PSO
from pso.cost_function import CostFunction

# Define a custom cost function
def custom_cost_function(position):
    return sum(x**2 for x in position) + 10

# Initialize PSO with parameters
pso = PSO(num_particles=40, max_iterations=150, bounds=[(-20, 20)] * 2, cost_function=custom_cost_function)

# Run optimization
pso.optimize()