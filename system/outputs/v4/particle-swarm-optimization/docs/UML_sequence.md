sequenceDiagram
    participant User
    participant PSO
    participant Particle
    participant CostFunction
    User->>PSO: Initialize PSO with parameters
    PSO->>CostFunction: Set cost function
    loop Optimization Iterations
        PSO->>Particle: Update velocity and position
        Particle->>CostFunction: Evaluate cost function
        Particle->>PSO: Return cost value
        PSO->>PSO: Update global best
    end
    PSO->>User: Return best solution and value