class OptimizationProcess:
    @staticmethod
    def show_progress(iteration, best_value):
        print(f"Iteration {iteration}: Best Value = {best_value}")

    @staticmethod
    def display_final_output(best_value):
        print(f"Optimization completed. Best Value = {best_value}")