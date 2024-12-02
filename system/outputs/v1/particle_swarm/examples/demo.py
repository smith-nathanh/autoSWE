from pso.pso import PSO
from pso.cost_function import CostFunction

if __name__ == "__main__":
    num_particles = 30
    max_iterations = 100
    bounds = [(-10, 10)] * 2  # Example for 2D optimization
    cost_function = CostFunction()

    pso = PSO(num_particles, max_iterations, bounds, cost_function)
    best_position, best_value = pso.run_optimization()

    print(f"Best Position: {best_position}")
    print(f"Best Value: {best_value}")