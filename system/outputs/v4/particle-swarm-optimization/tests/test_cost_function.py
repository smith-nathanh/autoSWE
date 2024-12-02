import unittest
from src.cost_function import CostFunction

class TestCostFunction(unittest.TestCase):
    def test_sphere_function(self):
        position = [0, 0]
        result = CostFunction.sphere_function(position)
        self.assertEqual(result, 0)

        position = [1, 1]
        result = CostFunction.sphere_function(position)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()