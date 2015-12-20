import sys

# produces a 2D array (list of lists) of the multiples of a sequence of primes
# n - input list which contains the list of primes
def matrix_calculator(nums):
	#populate grid headings
	grid = list()
	grid.append([-1] + nums)
	for n in nums:
		row = list()
		row.append(n)
		for m in nums:
			row.append(m * n)
		grid.append(row)

	return grid


# produces sequence of prime numbers dependant on the user input
# e.g. if n = 5 generates 5 primes
# if input is not a positive number, return empty list
def prime_sequence(n):
	if n < 1:
		return []

	primes = list()
	count = 2

	while len(primes) is not n:
		if is_prime(count):
			primes.append(count)
		count = count + 1
	return primes

# determines if the number entered is a prime based on explicit criteria
# a prime number is only divisable by itself and 1
def is_prime(n):
	if n < 2:
		return False
	for div in range(2, n):
		if n % div == 0:
			return False
	return True

def pretty_print(mtx):
	for row in mtx:
		for num in row:
			out = '%4s' % (str(num),)
			print "| " + out,
		print "|"

if __name__ == "__main__":

	num = int(sys.argv[1])
	seq = prime_sequence(num)
	pretty_print(matrix_calculator(seq))