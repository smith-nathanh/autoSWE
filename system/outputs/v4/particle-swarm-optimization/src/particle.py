import random

class Particle:
    def __init__(self, bounds):
        self.position = [random.uniform(b[0], b[1]) for b in bounds]
        self.velocity = [0.0 for _ in bounds]
        self.best_position = self.position[:]
        self.best_value = float('inf')

    def update_velocity(self, global_best_position, inertia=0.5, cognitive=1.5, social=1.5):
        for i in range(len(self.position)):
            r1 = random.random()
            r2 = random.random()
            cognitive_velocity = cognitive * r1 * (self.best_position[i] - self.position[i])
            social_velocity = social * r2 * (global_best_position[i] - self.position[i])
            self.velocity[i] = inertia * self.velocity[i] + cognitive_velocity + social_velocity

    def update_position(self, bounds):
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]
            # Ensure the particle's position is within bounds
            if self.position[i] < bounds[i][0]:
                self.position[i] = bounds[i][0]
            elif self.position[i] > bounds[i][1]:
                self.position[i] = bounds[i][1]