import unittest
from src.pso import PSO
from src.cost_function import CostFunction

class TestPSO(unittest.TestCase):
    def test_optimization(self):
        cost_function = CostFunction.sphere_function
        bounds = [(-10, 10) for _ in range(2)]
        pso = PSO(num_particles=10, max_iterations=10, bounds=bounds, cost_function=cost_function)
        best_position, best_value = pso.optimize()
        self.assertIsInstance(best_position, list)
        self.assertIsInstance(best_value, float)

if __name__ == '__main__':
    unittest.main()