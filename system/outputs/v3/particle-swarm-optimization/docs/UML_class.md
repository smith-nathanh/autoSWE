classDiagram
    class PSO {
        +int num_particles
        +int max_iterations
        +list bounds
        +function cost_function
        +optimize()
        +verbose_output()
    }
    class CostFunction {
        +function sphere_function
        +function custom_function
    }
    PSO --> CostFunction : uses
    class OptimizationProcess {
        +function show_progress()
        +function display_final_output()
    }
    PSO --> OptimizationProcess : manages