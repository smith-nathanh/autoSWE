from src.pso import PSO
from src.cost_function import CostFunction

if __name__ == "__main__":
    # Define the cost function
    cost_function = CostFunction()

    # Define the PSO parameters
    num_particles = 30
    max_iterations = 100
    bounds = [(-10, 10) for _ in range(2)]  # 2-dimensional problem

    # Initialize and run PSO
    pso = PSO(num_particles, max_iterations, bounds, cost_function)
    best_position, best_value = pso.run_optimization()

    print(f"Best Position: {best_position}")
    print(f"Best Value: {best_value}")