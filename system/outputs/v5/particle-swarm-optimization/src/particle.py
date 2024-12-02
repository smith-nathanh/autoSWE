import random

class Particle:
    def __init__(self, bounds):
        self.position = [random.uniform(bound[0], bound[1]) for bound in bounds]
        self.velocity = [0.0 for _ in bounds]
        self.best_position = self.position
        self.best_value = float('inf')

    def update_velocity(self, global_best_position):
        inertia_weight = 0.5
        cognitive_constant = 1.5
        social_constant = 1.5
        for i in range(len(self.velocity)):
            cognitive_velocity = cognitive_constant * random.random() * (self.best_position[i] - self.position[i])
            social_velocity = social_constant * random.random() * (global_best_position[i] - self.position[i])
            self.velocity[i] = inertia_weight * self.velocity[i] + cognitive_velocity + social_velocity

    def update_position(self, bounds):
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]
            # Ensure the particle's position is within bounds
            if self.position[i] < bounds[i][0]:
                self.position[i] = bounds[i][0]
            elif self.position[i] > bounds[i][1]:
                self.position[i] = bounds[i][1]