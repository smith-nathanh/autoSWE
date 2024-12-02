from pso.pso import PSO
from pso.sphere_function import SphereFunction

# Define parameters
num_particles = 30
max_iterations = 100
bounds = [(-10, 10)] * 2  # 2D problem

# Initialize PSO with SphereFunction
pso = PSO(num_particles, max_iterations, bounds, SphereFunction())

# Run optimization
pso.optimize()