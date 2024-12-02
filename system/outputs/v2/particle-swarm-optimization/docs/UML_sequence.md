sequenceDiagram
    participant User
    participant PSO
    participant CostFunction
    User->>PSO: Initialize with parameters
    loop for each iteration
        PSO->>CostFunction: Evaluate cost function
        CostFunction-->>PSO: Return cost
        PSO->>PSO: Update particles
        PSO->>User: Display iteration results
    end
    PSO->>User: Display final solution