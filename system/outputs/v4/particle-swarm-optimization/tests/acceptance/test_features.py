import unittest
from src.pso import PSO
from src.cost_function import CostFunction

class TestPSOFeatures(unittest.TestCase):
    def test_successful_optimization(self):
        """Test that PSO successfully optimizes the given cost function within bounds."""
        cost_function = CostFunction.sphere_function
        bounds = [(-10, 10) for _ in range(2)]
        pso = PSO(num_particles=30, max_iterations=100, bounds=bounds, cost_function=cost_function)
        best_position, best_value = pso.optimize()
        
        # Check if the best position is a list and best value is a float
        self.assertIsInstance(best_position, list)
        self.assertIsInstance(best_value, float)
        
        # Check if the best position is within bounds
        for i in range(len(bounds)):
            self.assertGreaterEqual(best_position[i], bounds[i][0])
            self.assertLessEqual(best_position[i], bounds[i][1])

    def test_verbose_output(self):
        """Test that the output displays the iterative process and final solution."""
        cost_function = CostFunction.sphere_function
        bounds = [(-10, 10) for _ in range(2)]
        pso = PSO(num_particles=30, max_iterations=5, bounds=bounds, cost_function=cost_function)
        
        # Capture the output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        pso.optimize()
        sys.stdout = sys.__stdout__
        
        # Check if the output contains iteration information
        output = captured_output.getvalue()
        for i in range(1, 6):
            self.assertIn(f"Iteration {i}/5", output)
        
        # Check if the output contains the final best value
        self.assertIn("Best Value:", output)

if __name__ == '__main__':
    unittest.main()
