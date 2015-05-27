import operator
primes = [97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]


def read_numbers_file():
    numbers_file = open('numbers.txt')
    line = numbers_file.readline()
    numbers = []
    while line:
        numbers.append(long(line))
        line = numbers_file.readline()
    numbers_file.close()
    return numbers


def times_divisible(number, divisor):
    i = 0
    division = number / divisor
    while division * divisor == number:
        number = division
        i += 1
        division = number / divisor
    return (i, number)


def prime_factors(number, primes):
    factors = []
    for divisor in primes:
        times, number = times_divisible(number, divisor)
        factors.append(times)
    return factors


def prime_favorites_in_range(numbers, primes):
    result = 25*[0]
    for number in numbers:
        factors = prime_factors(number, primes)
        result = map(operator.add, result, factors)
    return result


def print_favorites(result, primes):
    primes_result = zip(primes, result)
    favorite_times = max(result)
    favorites_primes_result = filter(lambda x: x[1] == favorite_times, primes_result)
    print favorite_times,
    for x in favorites_primes_result[::-1]:
        print x[0],
    print

numbers = read_numbers_file()

cases = int(input())
for i in xrange(cases):
    line_range = raw_input()
    n_from, n_to = map(lambda x: int(x), line_range.split())
    favorites = prime_favorites_in_range(numbers[n_from:n_to], primes)
    print_favorites(favorites, primes)
