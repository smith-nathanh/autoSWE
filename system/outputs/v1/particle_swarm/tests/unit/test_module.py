import unittest
from pso.pso import PSO
from pso.particle import Particle
from pso.cost_function import CostFunction

class TestPSO(unittest.TestCase):
    def setUp(self):
        self.num_particles = 30
        self.max_iterations = 100
        self.bounds = [(-10, 10)] * 2
        self.cost_function = CostFunction()
        self.pso = PSO(self.num_particles, self.max_iterations, self.bounds, self.cost_function)

    def test_initialization(self):
        self.assertEqual(len(self.pso.particles), self.num_particles)
        for particle in self.pso.particles:
            self.assertTrue(all(self.bounds[i][0] <= particle.position[i] <= self.bounds[i][1] for i in range(len(self.bounds))))

    def test_run_optimization(self):
        best_position, best_value = self.pso.run_optimization()
        self.assertIsInstance(best_position, tuple)
        self.assertIsInstance(best_value, float)

    def test_particle_update_velocity(self):
        particle = self.pso.particles[0]
        old_velocity = particle.velocity
        particle.update_velocity()
        self.assertNotEqual(old_velocity, particle.velocity)

    def test_particle_update_position(self):
        particle = self.pso.particles[0]
        old_position = particle.position
        particle.update_position()
        self.assertNotEqual(old_position, particle.position)

class TestCostFunction(unittest.TestCase):
    def test_evaluate(self):
        cost_function = CostFunction()
        position = (1, 2)
        expected_value = 1**2 + 2**2
        self.assertEqual(cost_function.evaluate(position), expected_value)

if __name__ == '__main__':
    unittest.main()
