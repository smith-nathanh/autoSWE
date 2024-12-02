class CostFunction:
    @staticmethod
    def sphere_function(position):
        return sum(x**2 for x in position)

    @staticmethod
    def custom_function(position):
        # Users can define their custom cost function here
        pass