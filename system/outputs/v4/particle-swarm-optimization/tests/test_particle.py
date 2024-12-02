import unittest
from src.particle import Particle

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

if __name__ == '__main__':
    unittest.main()