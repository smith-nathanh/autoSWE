import unittest
from src.pso import PSO
from src.particle import Particle
from src.cost_function import CostFunction

class TestPSO(unittest.TestCase):
    def test_optimization(self):
        cost_function = CostFunction.sphere_function
        bounds = [(-10, 10) for _ in range(2)]
        pso = PSO(num_particles=10, max_iterations=10, bounds=bounds, cost_function=cost_function)
        best_position, best_value = pso.optimize()
        self.assertIsInstance(best_position, list)
        self.assertIsInstance(best_value, float)
        self.assertTrue(all(bounds[i][0] <= best_position[i] <= bounds[i][1] for i in range(2)))

    def test_invalid_bounds(self):
        cost_function = CostFunction.sphere_function
        bounds = [(10, -10) for _ in range(2)]  # Invalid bounds
        with self.assertRaises(ValueError):
            PSO(num_particles=10, max_iterations=10, bounds=bounds, cost_function=cost_function)

class TestParticle(unittest.TestCase):
    def test_particle_initialization(self):
        bounds = [(-10, 10) for _ in range(2)]
        particle = Particle(bounds)
        self.assertEqual(len(particle.position), 2)
        self.assertEqual(len(particle.velocity), 2)

    def test_particle_update(self):
        bounds = [(-10, 10) for _ in range(2)]
        particle = Particle(bounds)
        global_best_position = [0, 0]
        particle.update_velocity(global_best_position)
        particle.update_position(bounds)
        self.assertTrue(all(bounds[i][0] <= particle.position[i] <= bounds[i][1] for i in range(2)))

    def test_particle_out_of_bounds(self):
        bounds = [(-10, 10) for _ in range(2)]
        particle = Particle(bounds)
        particle.position = [20, -20]  # Out of bounds
        particle.update_position(bounds)
        self.assertTrue(all(bounds[i][0] <= particle.position[i] <= bounds[i][1] for i in range(2)))

class TestCostFunction(unittest.TestCase):
    def test_sphere_function(self):
        position = [0, 0]
        result = CostFunction.sphere_function(position)
        self.assertEqual(result, 0)

        position = [1, 1]
        result = CostFunction.sphere_function(position)
        self.assertEqual(result, 2)

    def test_custom_function(self):
        # Assuming a custom function is defined
        def custom_function(position):
            return sum(x**3 for x in position)

        position = [1, 1]
        result = custom_function(position)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
