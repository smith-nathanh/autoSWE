import unittest
from pso.pso import PSO
from pso.cost_function import CostFunction

class TestPSO(unittest.TestCase):
    def setUp(self):
        self.num_particles = 30
        self.max_iterations = 100
        self.bounds = [(-10, 10)] * 2
        self.cost_function = CostFunction.sphere_function

    def test_initialization(self):
        pso = PSO(self.num_particles, self.max_iterations, self.bounds, self.cost_function)
        self.assertEqual(pso.num_particles, self.num_particles)
        self.assertEqual(pso.max_iterations, self.max_iterations)
        self.assertEqual(pso.bounds, self.bounds)
        self.assertEqual(pso.cost_function, self.cost_function)

    def test_optimize(self):
        pso = PSO(self.num_particles, self.max_iterations, self.bounds, self.cost_function)
        pso.optimize()
        self.assertIsNotNone(pso.best_solution)

    def test_sphere_function(self):
        position = [0, 0]
        result = self.cost_function(position)
        self.assertEqual(result, 0)

        position = [1, 1]
        result = self.cost_function(position)
        self.assertEqual(result, 2)

    def test_custom_cost_function(self):
        def custom_cost_function(position):
            return sum(x**2 for x in position) + 10

        pso = PSO(self.num_particles, self.max_iterations, self.bounds, custom_cost_function)
        pso.optimize()
        self.assertIsNotNone(pso.best_solution)

if __name__ == '__main__':
    unittest.main()
