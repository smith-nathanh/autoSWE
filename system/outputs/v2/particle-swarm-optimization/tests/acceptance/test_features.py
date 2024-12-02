import unittest
from pso.pso import PSO
from pso.sphere_function import SphereFunction
from pso.cost_function import CostFunction

class CustomCostFunction(CostFunction):
    def evaluate(self, position):
        return sum(position)

class TestPSOFeatures(unittest.TestCase):
    def setUp(self):
        self.num_particles = 30
        self.max_iterations = 100
        self.bounds = [(-10, 10)] * 2

    def test_sphere_function_optimization(self):
        pso = PSO(self.num_particles, self.max_iterations, self.bounds, SphereFunction())
        pso.optimize()
        # Check if the best solution is within the expected range
        self.assertIsNotNone(pso.best_solution)
        self.assertTrue(all(self.bounds[i][0] <= x <= self.bounds[i][1] for i, x in enumerate(pso.best_solution)))

    def test_custom_cost_function_optimization(self):
        pso = PSO(self.num_particles, self.max_iterations, self.bounds, CustomCostFunction())
        pso.optimize()
        # Check if the best solution is within the expected range
        self.assertIsNotNone(pso.best_solution)
        self.assertTrue(all(self.bounds[i][0] <= x <= self.bounds[i][1] for i, x in enumerate(pso.best_solution)))

if __name__ == '__main__':
    unittest.main()
