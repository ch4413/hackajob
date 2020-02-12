import unittest
import main


class SolutionMethods(unittest.TestCase):

    #
    def test_error(self):
        solution = main.Solution()
        self.assertEqual(solution.run('test'),
                         None)

    #
    def test_run(self):
        solution = main.Solution()
        self.assertEqual(solution.run(12), "XII")


if __name__ == "__main__":
    unittest.main()
