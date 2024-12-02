from src.pso import PSO
from src.cost_function import CostFunction

if __name__ == "__main__":
    # Define the cost function
    cost_function = CostFunction.sphere_function

    # Define the bounds for each dimension
    bounds = [(-10, 10) for _ in range(2)]  # 2-dimensional problem

    # Initialize PSO
    pso = PSO(num_particles=30, max_iterations=100, bounds=bounds, cost_function=cost_function)

    # Run optimization
    best_position, best_value = pso.optimize()

    print(f"Best Position: {best_position}")
    print(f"Best Value: {best_value}")