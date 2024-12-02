class PSO:
    def __init__(self, num_particles, max_iterations, bounds, cost_function):
        self.num_particles = num_particles
        self.max_iterations = max_iterations
        self.bounds = bounds
        self.cost_function = cost_function
        self.best_solution = None

    def optimize(self):
        # Initialize particles
        particles = self._initialize_particles()
        best_global_position = None
        best_global_value = float('inf')

        for iteration in range(self.max_iterations):
            for particle in particles:
                # Evaluate cost function
                value = self.cost_function(particle['position'])
                if value < particle['best_value']:
                    particle['best_value'] = value
                    particle['best_position'] = particle['position']

                if value < best_global_value:
                    best_global_value = value
                    best_global_position = particle['position']

            # Update particles
            self._update_particles(particles, best_global_position)

            # Verbose output
            self.verbose_output(iteration, best_global_value)

        self.best_solution = best_global_position
        self.display_final_output(best_global_value)

    def _initialize_particles(self):
        import random
        particles = []
        for _ in range(self.num_particles):
            position = [random.uniform(b[0], b[1]) for b in self.bounds]
            particles.append({'position': position, 'best_position': position, 'best_value': float('inf')})
        return particles

    def _update_particles(self, particles, best_global_position):
        import random
        for particle in particles:
            new_position = []
            for i, (pos, best_pos, global_best) in enumerate(zip(particle['position'], particle['best_position'], best_global_position)):
                new_pos = pos + random.uniform(0, 1) * (best_pos - pos) + random.uniform(0, 1) * (global_best - pos)
                new_pos = max(self.bounds[i][0], min(new_pos, self.bounds[i][1]))
                new_position.append(new_pos)
            particle['position'] = new_position

    def verbose_output(self, iteration, best_value):
        print(f"Iteration {iteration}: Best Value = {best_value}")

    def display_final_output(self, best_value):
        print(f"Optimization completed. Best Value = {best_value}")