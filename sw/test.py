import unittest
import main


class SolutionMethods(unittest.TestCase):
    # First Example
    def test_run(self):
        """

        """
        sol = main.Solution()
        self.assertEqual(sol.run('maul'), 1)

    def test_get_json(self):
        """

        """
        url = 'https://challenges.hackajob.co/swapi/api/people/'
        self.assertEqual(len(main.get_json(url)), 4)

    def test_clean_name(self):
        """

        """
        self.assertEqual(main.clean_name('a b'), 'a%20b')


if __name__ == "__main__":
    unittest.main()

