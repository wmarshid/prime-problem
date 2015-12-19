import unittest
import prime_generator as sut #the system under test

class PrimeGenTests(unittest.TestCase):
	"""Tests for 'prime_generator.py'."""

	def test_is_two_prime(self):
		self.assertTrue(sut.is_prime(2))

	def test_is_one_prime(self):
		self.assertFalse(sut.is_prime(1))


if __name__ == "__main__":
	unittest.main()

