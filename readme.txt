This project was created for the Prime tables coding exercise provided by FindmyPast.
Written using python 2.7.3

- How to run

1. To run the program navigate to this directory and run the following command;
'python prime_generator.py <num>'

Where num is the number of primes you wish to generate

2. To run the test suite for the program navigate to this directory and run the following command;
'python prime_tests.py'

Your output should include a summary of the tests run and the time taken to run the test suite. Any tests that fail will be displayed along with the reason for the failure (whether it was a logical error or a Fail condition of the test).

3. To run the performance tests, navigate to this directory and run the following command;
'python prime_times.py'

Your output should include a time in milliseconds for each of the examples,
these include running the sequence generator and then calculating a matrix for the same sequence (which is generated again).

- What I'm pleased with

I observed that each row in the matrix adds up to the prime factor of that row multiplied by 10, so made sure to include this as a test condition. I noticed later however that this only works for the first three primes.

The algorithm used was trial division as it was easier to interpret the problem and find logical breaks in the units of work in which to formulate unit tests and then iterate over the solution to build up each of the functions. In the worst case, trial division is a computationally-intensive algorithm.

The sieve of Eratosthenes is a much cheaper primality testing algorithm, one of a number of prime number sieves. It does so by iteratively marking as composite (non-prime) the multiples of each prime, starting with the multiples of two. If we wanted all primes up to the number 30 for example, we could use the sieve but if we wanted the first N primes we would need to be able to determine the number space beforehand. We could count to N number of primes and then terminate the function but in theory we could miss out the succeeding primes we need if the number space is too small e.g. if we sieve up to 10 but we need the first 5 primes. However we can use the prime number theorem (more accurately the prime counting function - https://primes.utm.edu/howmany.html#2) to determine the proximity of the next prime number.

- What I would like to improve on

The biggest bottleneck in the program is most certainly the prime number calculator. Albeit very fast for the most common use-cases (see 'prime_times.py'). It would be interesting to implement a few prime number sieves and possibly a more efficient algorithm and then time the different solutions. Each of these can be easily substituted for the initial sequence generator as the matrix calculator takes in any sequence as input.

I would have also liked to enhance the user experience by porting the program to the web, possibly having the table rendered on an HTML page with a number input and 'calculate' button. That way a user could explore different prime tables on the fly.

- Performance Tests

I used the 'timeit' python module to run these tests in the most imperative way.

The timeit module calls a function Timer which executes a specified function. The times posted are the accumulated times from each of the Timer executions. To get the true time of one execution divide each of these times by 100 again. For more info on how this works see 'prime_times.py' and the 'timeit' python docs.

The trial division process is exponential on paper but I was curious to see how rapidly this would take off in practice (at least when using my dev machine!). It was clear to see the curve shooting off 10 fold at the 50 mark from the initial 5 primes test and increasing almost ten fold again at the 200 mark.

It was interesting to see that calculating the matrix grid almost doubles the total execution time.  Which would imply that doing N^2 multiplications is about the same amount of work as generating the prime sequence (which is also N^2 operations).

After 100 executions per Timer call
First   5 primes (ms):  0.00139093399048
  and the matrix (ms):  0.00227403640747
First  20 primes (ms):  0.0145859718323
  and the matrix (ms):  0.0250849723816
First  50 primes (ms):  0.0770220756531
  and the matrix (ms):  0.126882076263
First 200 primes (ms):  1.6161429882
  and the matrix (ms):  2.35272288322