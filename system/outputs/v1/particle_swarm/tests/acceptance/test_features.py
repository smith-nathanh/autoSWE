import unittest
from pso.pso import PSO
from pso.cost_function import CostFunction

class TestPSOFeatures(unittest.TestCase):
    def setUp(self):
        self.num_particles = 30
        self.max_iterations = 100
        self.bounds = [(-10, 10)] * 2  # 2D optimization
        self.cost_function = CostFunction()

    def test_optimization_process(self):
        pso = PSO(self.num_particles, self.max_iterations, self.bounds, self.cost_function)
        best_position, best_value = pso.run_optimization()

        # Check if the best position is within the bounds
        for pos, bound in zip(best_position, self.bounds):
            self.assertGreaterEqual(pos, bound[0])
            self.assertLessEqual(pos, bound[1])

        # Check if the best value is a float
        self.assertIsInstance(best_value, float)

    def test_output_consistency(self):
        pso = PSO(self.num_particles, self.max_iterations, self.bounds, self.cost_function)
        best_position, best_value = pso.run_optimization()

        # Run the optimization again to check for consistency
        best_position_2, best_value_2 = pso.run_optimization()

        # Check if the results are consistent
        self.assertEqual(best_position, best_position_2)
        self.assertEqual(best_value, best_value_2)

if __name__ == '__main__':
    unittest.main()
