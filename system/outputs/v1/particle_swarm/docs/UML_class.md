classDiagram
    class PSO {
        - int num_particles
        - int max_iterations
        - tuple bounds
        - list particles
        - function cost_function
        + run_optimization()
        + update_particles()
        + evaluate_particles()
    }
    class Particle {
        - tuple position
        - tuple velocity
        - float best_position
        - float best_value
        + update_velocity()
        + update_position()
    }
    PSO --> Particle : manages
    PSO --> "1" CostFunction : uses
    class CostFunction {
        + evaluate(position)
    }