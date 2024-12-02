sequenceDiagram
    participant User
    participant PSO
    participant Particle
    participant CostFunction
    User->>PSO: initialize(num_particles, max_iterations, bounds, cost_function)
    loop for each iteration
        PSO->>Particle: update_velocity()
        PSO->>Particle: update_position()
        Particle->>CostFunction: evaluate(position)
        CostFunction-->>Particle: return value
        Particle-->>PSO: update best position and value
    end
    PSO-->>User: return best solution and value