import unittest
from src.pso import PSO
from src.cost_function import CostFunction

class TestPSO(unittest.TestCase):
    def test_optimization(self):
        cost_function = CostFunction()
        num_particles = 10
        max_iterations = 50
        bounds = [(-5, 5) for _ in range(2)]
        pso = PSO(num_particles, max_iterations, bounds, cost_function)
        best_position, best_value = pso.run_optimization()
        self.assertIsInstance(best_position, list)
        self.assertIsInstance(best_value, float)

if __name__ == '__main__':
    unittest.main()