import sys

# produces sequence of prime numbers dependant on the user input
# e.g. if n = 5 generates 5 primes
def prime(n):
	return n

# determines if the number entered is a prime based on explicit criteria
# a prime number is only divisable by itself and 1
def is_prime(n):
	if n < 2:
		return False
	else:
		return True


if __name__ == "__main__":

	num = sys.argv[1]
	print prime(num)