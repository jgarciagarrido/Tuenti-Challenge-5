import math


def primes_to(n):
    sieve = [True] * (n/2)
    for i in xrange(3, int(n**0.5)+1, 2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1, n/2) if sieve[i]]


def almost_prime_numbers_to(n):
    primes_b = primes_to(n/2 + 1)
    primes_a = primes_to(int(math.sqrt(n)) + 1)
    i = 0
    almost_primes = []
    for prime_a in primes_a:
        for prime_b in primes_b[i:]:
            almost_prime = prime_a*prime_b
            if almost_prime > n:
                break
            almost_primes.append(almost_prime)
        i += 1
    return almost_primes


def almost_prime_numbers_in_range(n_from, n_to, almost_primes):
    in_range = lambda x: x >= n_from and x <= n_to
    almost_primes_in = filter(in_range, almost_primes)
    return len(almost_primes_in)


almost_primes = almost_prime_numbers_to(100000000)
cases = int(input())
for i in xrange(cases):
    line_range = raw_input()
    n_from, n_to = map(lambda x: int(x), line_range.split())
    print almost_prime_numbers_in_range(n_from, n_to, almost_primes)
