import unittest
from src.pso import PSO
from src.particle import Particle
from src.cost_function import CostFunction

class TestPSO(unittest.TestCase):
    def setUp(self):
        self.cost_function = CostFunction()
        self.bounds = [(-5, 5) for _ in range(2)]

    def test_optimization(self):
        num_particles = 10
        max_iterations = 50
        pso = PSO(num_particles, max_iterations, self.bounds, self.cost_function)
        best_position, best_value = pso.run_optimization()
        self.assertIsInstance(best_position, list)
        self.assertIsInstance(best_value, float)

    def test_optimization_with_zero_iterations(self):
        num_particles = 10
        max_iterations = 0
        pso = PSO(num_particles, max_iterations, self.bounds, self.cost_function)
        best_position, best_value = pso.run_optimization()
        self.assertIsNone(pso.global_best_position)
        self.assertEqual(pso.global_best_value, float('inf'))

    def test_optimization_with_no_particles(self):
        num_particles = 0
        max_iterations = 50
        pso = PSO(num_particles, max_iterations, self.bounds, self.cost_function)
        best_position, best_value = pso.run_optimization()
        self.assertIsNone(pso.global_best_position)
        self.assertEqual(pso.global_best_value, float('inf'))

class TestParticle(unittest.TestCase):
    def setUp(self):
        self.bounds = [(-5, 5), (-5, 5)]

    def test_particle_initialization(self):
        particle = Particle(self.bounds)
        self.assertEqual(len(particle.position), 2)
        self.assertEqual(len(particle.velocity), 2)

    def test_particle_update(self):
        particle = Particle(self.bounds)
        global_best_position = [0, 0]
        particle.update_velocity(global_best_position)
        particle.update_position(self.bounds)
        for i in range(len(particle.position)):
            self.assertGreaterEqual(particle.position[i], self.bounds[i][0])
            self.assertLessEqual(particle.position[i], self.bounds[i][1])

    def test_particle_update_with_no_movement(self):
        particle = Particle(self.bounds)
        particle.velocity = [0, 0]
        particle.update_position(self.bounds)
        self.assertEqual(particle.position, particle.best_position)

class TestCostFunction(unittest.TestCase):
    def test_evaluate(self):
        cost_function = CostFunction()
        position = [1, 2, 3]
        result = cost_function.evaluate(position)
        expected = 1**2 + 2**2 + 3**2
        self.assertEqual(result, expected)

    def test_evaluate_with_empty_position(self):
        cost_function = CostFunction()
        position = []
        result = cost_function.evaluate(position)
        expected = 0
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
