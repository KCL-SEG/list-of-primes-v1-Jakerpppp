"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    current = 1
    while len(list) < number_of_primes:
        if testIfPrime(current):
            list.append(current)
        current+=1
    return list

def testIfPrime(number):
    factors = 0
    for i in range(1,number+1):
        if number % i == 0:
            factors += 1
    return factors == 2
