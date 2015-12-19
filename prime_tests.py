import unittest
import prime_generator as sut #the system under test

class PrimeNumTests(unittest.TestCase):
	"""Tests for 'is_prime' unit."""

	def test_is_two_prime(self):
		self.assertTrue(sut.is_prime(2))

	def test_is_one_prime(self):
		self.assertFalse(sut.is_prime(1))

	def test_is_six_prime(self):
		self.assertFalse(sut.is_prime(6))

	#edge cases

	def test_is_zero_prime(self):
		self.assertFalse(sut.is_prime(0))

	def test_are_negatives_prime(self):
		self.assertFalse(sut.is_prime(-6))
		self.assertFalse(sut.is_prime(-5))

class PrimeNumGenTests(unittest.TestCase):
	"""Tests for 'prime' unit."""

	def test_last_num(self):
		# We know that 5 is the 3rd prime number
		self.assertTrue(sut.prime_sequence(3)[-1] is 5)

	#edge cases

	def test_list_size_for_input_zero(self):
		# List should be empty
		self.assertTrue(len(sut.prime_sequence(0)) is 0)

	def test_list_size_for_negative_input(self):
		self.assertTrue(len(sut.prime_sequence(-5)) is 0)

if __name__ == "__main__":
	unittest.main()

