class PSO:
    def __init__(self, num_particles, max_iterations, bounds, cost_function):
        self.num_particles = num_particles
        self.max_iterations = max_iterations
        self.bounds = bounds
        self.cost_function = cost_function
        self.particles = [Particle(bounds) for _ in range(num_particles)]

    def run_optimization(self):
        for _ in range(self.max_iterations):
            self.update_particles()
            self.evaluate_particles()
        best_particle = min(self.particles, key=lambda p: p.best_value)
        return best_particle.best_position, best_particle.best_value

    def update_particles(self):
        for particle in self.particles:
            particle.update_velocity()
            particle.update_position()

    def evaluate_particles(self):
        for particle in self.particles:
            value = self.cost_function.evaluate(particle.position)
            if value < particle.best_value:
                particle.best_value = value
                particle.best_position = particle.position