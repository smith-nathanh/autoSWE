class CostFunction:
    def evaluate(self, position):
        # Example: Sphere function
        return sum(x**2 for x in position)