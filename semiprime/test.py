import main
import unittest


class SolutionMethods(unittest.TestCase):

    def test_example(self):
        self.assertEqual("this is an example", "this is an example")

    #
    # Second Example
    #
    def test_run(self):
        sol = main.Solution()
        self.assertEqual(sol.run(90), False)


if __name__ == "__main__":
    unittest.main()
