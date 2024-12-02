from pso.pso import PSO
from pso.cost_function import CostFunction

# Define the sphere function as the cost function
cost_function = CostFunction.sphere_function

# Initialize PSO with parameters
pso = PSO(num_particles=50, max_iterations=200, bounds=[(-5, 5)] * 3, cost_function=cost_function)

# Run optimization
pso.optimize()