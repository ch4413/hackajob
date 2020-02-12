import unittest
import main


class SolutionMethods(unittest.TestCase):
	##
	##
	def test_get_json(self):

		url = 'https://challenges.hackajob.co/swapi/api/people/'
		self.assertEqual(len(main.get_json(url)), 4)

	def test_clean_name(self):
		self.assertEqual(main.clean_name('a b'), 'a%20b')

	def test_run(self):
		sol = main.Solution()
		self.assertEqual(sol.run("The Force Awakens", "Walter White"), 'The Force Awakens: Ackbar, BB8, Captain Phasma, Chewbacca, Finn, Han Solo, Leia Organa, Luke Skywalker, Poe Dameron, R2-D2, Rey; Walter White: none')


if __name__ == "__main__":
	unittest.main()
