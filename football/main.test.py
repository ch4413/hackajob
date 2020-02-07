import unittest
import main


class SolutionMethods(unittest.TestCase):
    # Set of unit tests with unittest package

    # test get_json
    def test_get_json(self):
        'Retrieves data from URL and checks length'
        data = main.get_json("https://raw.githubusercontent.com/openfootball/football.json/master/2014-15/en.1.json")
        self.assertEqual(len(data), 2)

    # test run
    def test_run(self):
        """
        Runs pipeline on test case
        """
        solution = main.Solution()
        self.assertEqual(solution.run('arsenal'), 71)

    def test_run_bad_key(self):
        """
        Runs pipeline on fail case
        """
        solution = main.Solution()
        self.assertEqual(solution.run('a'),
                         'Key "a" not found')


if __name__ == "__main__":
    unittest.main()
