import unittest
from pso.pso import PSO
from pso.sphere_function import SphereFunction
from pso.cost_function import CostFunction

class TestPSO(unittest.TestCase):
    def setUp(self):
        self.num_particles = 30
        self.max_iterations = 100
        self.bounds = [(-10, 10)] * 2  # 2D problem

    def test_pso_initialization(self):
        pso = PSO(self.num_particles, self.max_iterations, self.bounds, SphereFunction())
        self.assertEqual(pso.num_particles, self.num_particles)
        self.assertEqual(pso.max_iterations, self.max_iterations)
        self.assertEqual(pso.bounds, self.bounds)
        self.assertIsInstance(pso.cost_function, SphereFunction)

    def test_sphere_function_evaluation(self):
        sphere_function = SphereFunction()
        position = [1, 2]
        expected_cost = 1**2 + 2**2
        self.assertEqual(sphere_function.evaluate(position), expected_cost)

    def test_custom_cost_function(self):
        class CustomCostFunction(CostFunction):
            def evaluate(self, position):
                return sum(position)

        custom_cost_function = CustomCostFunction()
        position = [1, 2, 3]
        expected_cost = 1 + 2 + 3
        self.assertEqual(custom_cost_function.evaluate(position), expected_cost)

    def test_pso_optimization_process(self):
        pso = PSO(self.num_particles, self.max_iterations, self.bounds, SphereFunction())
        pso.optimize()
        # Since the optimization process is stochastic, we can't predict the exact best solution
        # But we can check if the best_solution is not None after optimization
        self.assertIsNotNone(pso.best_solution)

if __name__ == '__main__':
    unittest.main()
