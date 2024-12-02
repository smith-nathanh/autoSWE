classDiagram
    class PSO {
        +int num_particles
        +int max_iterations
        +list bounds
        +function cost_function
        +optimize()
    }
    class CostFunction {
        +function evaluate()
    }
    class SphereFunction {
        +function evaluate()
    }
    PSO --> CostFunction : uses
    SphereFunction --|> CostFunction