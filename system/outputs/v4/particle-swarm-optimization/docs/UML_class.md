classDiagram
    class PSO {
        - int num_particles
        - int max_iterations
        - list bounds
        - function cost_function
        + optimize()
    }
    class Particle {
        - list position
        - list velocity
        - list best_position
        - float best_value
        + update_velocity()
        + update_position()
    }
    PSO --> Particle : uses
    class CostFunction {
        + sphere_function()
        + custom_function()
    }
    PSO --> CostFunction : uses