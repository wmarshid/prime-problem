import timeit

# Executes the 'prime_generator' sequence function (which utilities trial division) for different lengths.
# Then executes the 'prime_generator' matrix function which multiplies these prime factors together to a multiplication table of prime numbers. 
if __name__ == "__main__":

    # runs timeit 'reps' amount of times to limit system overhead per call
    # each timeit call runs an 'execs' number of times
    # The time produced is the accumulated time of all the execs.
    # The overall time takes the minimum from all the times produced.
    # (it can be assumed that larger times include system overhead as the minimum time comprises of the least amount of work needed to generate a result)
    
    reps = 5 # calls the Timer 'reps' number of times
    execs = 100 # executes the code under test 'execs' number of times per Timer call

    print('First   5 primes (ms): '),
    print min(timeit.Timer('sut.prime_sequence(5)', setup='import prime_generator as sut').repeat(reps, execs))
    print('  and the matrix (ms): '),
    print min(timeit.Timer('sut.matrix_calculator(sut.prime_sequence(5))', setup='import prime_generator as sut').repeat(reps, execs))

    print('First  20 primes (ms): '),
    print min(timeit.Timer('sut.prime_sequence(20)', setup='import prime_generator as sut').repeat(reps, execs))
    print('  and the matrix (ms): '),
    print min(timeit.Timer('sut.matrix_calculator(sut.prime_sequence(20))', setup='import prime_generator as sut').repeat(reps, execs))

    print('First  50 primes (ms): '),
    print min(timeit.Timer('sut.prime_sequence(50)', setup='import prime_generator as sut').repeat(reps, execs))
    print('  and the matrix (ms): '),
    print min(timeit.Timer('sut.matrix_calculator(sut.prime_sequence(50))', setup='import prime_generator as sut').repeat(reps, execs))

    print('First 200 primes (ms): '),
    print min(timeit.Timer('sut.prime_sequence(200)', setup='import prime_generator as sut').repeat(reps, execs))
    print('  and the matrix (ms): '),
    print min(timeit.Timer('sut.matrix_calculator(sut.prime_sequence(200))', setup='import prime_generator as sut').repeat(reps, execs))