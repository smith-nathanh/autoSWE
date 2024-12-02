import unittest
from pso.pso import PSO
from pso.cost_function import CostFunction

class TestPSOFeatures(unittest.TestCase):
    def setUp(self):
        # Define a simple cost function for testing
        self.cost_function = CostFunction.sphere_function
        self.bounds = [(-10, 10)] * 2

    def test_pso_optimization(self):
        # Initialize PSO with parameters
        pso = PSO(num_particles=30, max_iterations=100, bounds=self.bounds, cost_function=self.cost_function)
        
        # Run optimization
        pso.optimize()

        # Check if the best solution is within the bounds
        for i, bound in enumerate(self.bounds):
            self.assertGreaterEqual(pso.best_solution[i], bound[0])
            self.assertLessEqual(pso.best_solution[i], bound[1])

    def test_pso_output(self):
        # Initialize PSO with parameters
        pso = PSO(num_particles=30, max_iterations=100, bounds=self.bounds, cost_function=self.cost_function)
        
        # Capture the output
        import io
        import sys
        captured_output = io.StringIO()          # Create StringIO object
        sys.stdout = captured_output             # Redirect stdout.
        pso.optimize()                           # Call function.
        sys.stdout = sys.__stdout__              # Reset redirect.

        # Check if the output contains expected strings
        output = captured_output.getvalue()
        self.assertIn("Optimization completed.", output)
        self.assertIn("Best Value =", output)

if __name__ == '__main__':
    unittest.main()
