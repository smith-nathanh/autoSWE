sequenceDiagram
    participant User
    participant PSO
    participant CostFunction
    participant OptimizationProcess
    User->>PSO: Initialize with parameters
    PSO->>CostFunction: Set cost function
    loop Optimization Iterations
        PSO->>OptimizationProcess: Update particles
        OptimizationProcess->>PSO: Return best solution
        PSO->>User: Display verbose output
    end
    PSO->>OptimizationProcess: Finalize optimization
    OptimizationProcess->>User: Display final output