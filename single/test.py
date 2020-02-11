import main
import unittest


class SolutionMethods(unittest.TestCase):
	# First Example
	#
	def test_example(self):
		self.assertEqual("this is an example", "this is an example")

	##
	# Second Example
	##
	def test_run(self):
		solution = main.Solution()
		self.assertEqual(solution.run([1, 2, 1]), 2)


if __name__ == "__main__":
	unittest.main()
