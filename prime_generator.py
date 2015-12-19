import sys

# produces sequence of prime numbers dependant on the user input
# e.g. if n = 5 generates 5 primes
def prime_sequence(n):
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


if __name__ == "__main__":

	num = int(sys.argv[1])
	print prime_sequence(num)
	#print is_prime(9)