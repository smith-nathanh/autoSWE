import random
from .particle import Particle
from .cost_function import CostFunction

class PSO:
    def __init__(self, num_particles, max_iterations, bounds, cost_function):
        self.num_particles = num_particles
        self.max_iterations = max_iterations
        self.bounds = bounds
        self.cost_function = cost_function
        self.particles = [Particle(bounds) for _ in range(num_particles)]
        self.global_best_position = None
        self.global_best_value = float('inf')

    def optimize(self):
        for iteration in range(self.max_iterations):
            for particle in self.particles:
                value = self.cost_function(particle.position)
                if value < particle.best_value:
                    particle.best_value = value
                    particle.best_position = particle.position

                if value < self.global_best_value:
                    self.global_best_value = value
                    self.global_best_position = particle.position

            for particle in self.particles:
                particle.update_velocity(self.global_best_position)
                particle.update_position(self.bounds)

            print(f"Iteration {iteration+1}/{self.max_iterations}, Best Value: {self.global_best_value}")

        return self.global_best_position, self.global_best_value