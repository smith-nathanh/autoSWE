from .cost_function import CostFunction

class SphereFunction(CostFunction):
    def evaluate(self, position):
        return sum(x**2 for x in position)