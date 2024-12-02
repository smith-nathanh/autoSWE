sequenceDiagram
    participant User
    participant PSO
    participant Particle
    participant CostFunction
    User->>PSO: Initialize PSO with parameters
    loop Optimization Process
        PSO->>Particle: Update velocity and position
        Particle-->>PSO: Return updated state
        PSO->>CostFunction: Evaluate cost function
        CostFunction-->>PSO: Return cost value
        PSO->>PSO: Update best solution
    end
    PSO-->>User: Return best solution found