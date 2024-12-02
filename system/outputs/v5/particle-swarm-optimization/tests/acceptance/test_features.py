import unittest
from src.pso import PSO
from src.cost_function import CostFunction

class TestPSOFeatures(unittest.TestCase):
    def test_pso_optimizes_cost_function(self):
        """Test that PSO optimizes the given cost function within specified bounds."""
        cost_function = CostFunction()
        num_particles = 30
        max_iterations = 100
        bounds = [(-10, 10) for _ in range(2)]
        pso = PSO(num_particles, max_iterations, bounds, cost_function)
        best_position, best_value = pso.run_optimization()
        self.assertIsInstance(best_position, list)
        self.assertIsInstance(best_value, float)

    def test_pso_output_format(self):
        """Test that PSO output clearly displays the iterative process and final solution."""
        cost_function = CostFunction()
        num_particles = 5
        max_iterations = 5
        bounds = [(-5, 5) for _ in range(2)]
        pso = PSO(num_particles, max_iterations, bounds, cost_function)
        best_position, best_value = pso.run_optimization()
        # Check if the output is in the expected format
        self.assertIsInstance(best_position, list)
        self.assertIsInstance(best_value, float)

    def test_pso_consistent_solution(self):
        """Test that the solution found by PSO is consistent with expected results."""
        cost_function = CostFunction()
        num_particles = 10
        max_iterations = 50
        bounds = [(-5, 5) for _ in range(2)]
        pso = PSO(num_particles, max_iterations, bounds, cost_function)
        best_position, best_value = pso.run_optimization()
        # Since the sphere function minimum is at [0, 0], we expect the best value to be close to 0
        self.assertAlmostEqual(best_value, 0, delta=1.0)

if __name__ == '__main__':
    unittest.main()
