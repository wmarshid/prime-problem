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
	"""Tests for 'prime_sequence' unit."""

	def test_list_size_is_correct(self):
		num = 3
		seq = sut.prime_sequence(num)
		self.assertTrue(len(seq) is num)

	def test_last_num(self):
		# We know that 5 is the 3rd prime number
		self.assertTrue(sut.prime_sequence(3)[-1] is 5)

	#edge cases

	def test_list_size_for_input_zero(self):
		# List should be empty
		self.assertTrue(len(sut.prime_sequence(0)) is 0)

	def test_list_size_for_negative_input(self):
		# Returns an empty list
		self.assertTrue(len(sut.prime_sequence(-5)) is 0)

class PrimeNumMatrixTests(unittest.TestCase):
	"""Tests for 'matrix_calculator'."""

	def test_grid_size_is_correct(self):
		# grid should have N+1 rows and N+1 columns
		num = 3
		seq = sut.prime_sequence(num)
		matrix = sut.matrix_calculator(seq)
		self.assertTrue(len(matrix) is num+1) #checks rows
		self.assertTrue(len(matrix[0]) is num+1) #checks columns

	def test_row_headings_match_sequence(self):
		seq = sut.prime_sequence(3)
		row_headings = sut.matrix_calculator(seq)[0][1:]
		self.assertTrue(seq == row_headings)

	def test_calcs_are_correct(self):
		# each row should add up to its prime x 10
		seq = sut.prime_sequence(3)
		matrix = sut.matrix_calculator(seq)
		for row in matrix:
			self.assertTrue(sum(row[1:] is row[0] * 10))

if __name__ == "__main__":
	unittest.main()

