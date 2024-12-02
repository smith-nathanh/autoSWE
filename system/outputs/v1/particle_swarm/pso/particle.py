import random

class Particle:
    def __init__(self, bounds):
        self.position = tuple(random.uniform(b[0], b[1]) for b in bounds)
        self.velocity = tuple(random.uniform(-1, 1) for _ in bounds)
        self.best_position = self.position
        self.best_value = float('inf')

    def update_velocity(self):
        # Simplified velocity update for demonstration purposes
        self.velocity = tuple(v + random.uniform(-0.1, 0.1) for v in self.velocity)

    def update_position(self):
        self.position = tuple(p + v for p, v in zip(self.position, self.velocity))