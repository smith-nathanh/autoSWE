from pso.pso import PSO
from pso.cost_function import CostFunction

class CustomCostFunction(CostFunction):
    def evaluate(self, position):
        # Example: simple sum of position values
        return sum(position)

# Define parameters
num_particles = 30
max_iterations = 100
bounds = [(-10, 10)] * 2  # 2D problem

# Initialize PSO with CustomCostFunction
pso = PSO(num_particles, max_iterations, bounds, CustomCostFunction())

# Run optimization
pso.optimize()