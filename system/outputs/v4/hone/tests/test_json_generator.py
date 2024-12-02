import unittest
import json
from src.json_generator import JSONGenerator

class TestJSONGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = JSONGenerator()
        self.data = [['name', 'age'], ['Tommy', '5'], ['Clara', '2']]
        self.schema = {'name': 'name', 'age': 'age'}

    def test_convert_to_json_without_schema(self):
        expected = [{'name': 'Tommy', 'age': '5'}, {'name': 'Clara', 'age': '2'}]
        result = self.generator.convert_to_json(self.data)
        self.assertEqual(result, expected)

    def test_convert_to_json_with_schema(self):
        expected = [{'name': 'Tommy', 'age': '5'}, {'name': 'Clara', 'age': '2'}]
        result = self.generator.convert_to_json(self.data, self.schema)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
