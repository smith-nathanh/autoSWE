import unittest
from src.cost_function import CostFunction

class TestCostFunction(unittest.TestCase):
    def test_evaluate(self):
        cost_function = CostFunction()
        position = [1, 2, 3]
        result = cost_function.evaluate(position)
        expected = 1**2 + 2**2 + 3**2
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()