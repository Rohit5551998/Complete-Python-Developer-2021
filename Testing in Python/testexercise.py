import unittest
import script


class TestGame(unittest.TestCase):

	def test_input(self):
		guess = 5
		answer = 5
		result = script.run_guess(guess, answer)
		self.assertTrue(result)

	def test_input_wrong_guess(self):
		guess = 5
		answer = 1
		result = script.run_guess(guess, answer)
		self.assertFalse(result)

	def test_input_wrong_number(self):
		guess = 11
		answer = 1
		result = script.run_guess(guess, answer)
		self.assertFalse(result)

	def test_input_wrong_type(self):
		guess = "hello"
		answer = 1
		result = script.run_guess(guess, answer)
		self.assertFalse(result)

if __name__ == "__main__":
	unittest.main()