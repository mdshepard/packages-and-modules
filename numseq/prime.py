"""this here's a couple functions dealing with prime numbers
the first un' goes and prints out all the prime numbers leadin up to n
the second un' goes and finds out if the number you enter is prime or it'aint
"""

"""prints a list of prime numbers up to the argument"""
def primes(n):
    result = []
    for num in range(2, n):
        prime = True
        for x in range(2, num):
            if num % x == 0:
                prime = False
            else:
                pass
        if prime is True:
            result.append(num)
    return result


"""finds whether or not the number entered is prime or not"""


def is_prime(m):
    prime = True
    for num in range(2, m):
        if m % num == 0:
            prime = False
            break
    return prime
