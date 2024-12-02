from pso.pso import PSO
from pso.cost_function import CostFunction

# Define the cost function
cost_function = CostFunction.sphere_function

# Initialize PSO with parameters
pso = PSO(num_particles=30, max_iterations=100, bounds=[(-10, 10)] * 2, cost_function=cost_function)

# Run optimization
pso.optimize()