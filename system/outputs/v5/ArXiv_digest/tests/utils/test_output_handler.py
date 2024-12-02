import unittest
import os
from src.utils.output_handler import output_results
from src.paper import Paper

class TestOutputHandler(unittest.TestCase):
    def setUp(self):
        self.papers = [
            Paper('cs.CL', 'Title1', 'Author1', 'Abstract1', '2023-10-01T12:00:00Z', 'http://link1'),
            Paper('cs.CL', 'Title2', 'Author2', 'Abstract2', '2023-10-02T12:00:00Z', 'http://link2')
        ]
        self.test_file = 'test_output.csv'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_output_results_to_file(self):
        output_results(self.papers, self.test_file, False)
        self.assertTrue(os.path.exists(self.test_file))

    def test_output_results_verbose(self):
        # This test would ideally capture stdout and verify the output
        pass

if __name__ == '__main__':
    unittest.main()
