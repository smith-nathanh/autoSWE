import unittest
from src.particle import Particle

class TestParticle(unittest.TestCase):
    def test_particle_initialization(self):
        bounds = [(-5, 5), (-5, 5)]
        particle = Particle(bounds)
        self.assertEqual(len(particle.position), 2)
        self.assertEqual(len(particle.velocity), 2)

    def test_particle_update(self):
        bounds = [(-5, 5), (-5, 5)]
        particle = Particle(bounds)
        global_best_position = [0, 0]
        particle.update_velocity(global_best_position)
        particle.update_position(bounds)
        for i in range(len(particle.position)):
            self.assertGreaterEqual(particle.position[i], bounds[i][0])
            self.assertLessEqual(particle.position[i], bounds[i][1])

if __name__ == '__main__':
    unittest.main()