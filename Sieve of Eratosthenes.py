# SIEVE OF ERATOSTHENES

# Given a number n, print all primes smaller than or equal to n.

# NOTE : Prime numbers are those which have 1 and itself has divisors.

# Algorithm:
# Create a list of all the integers up-to n that is up-to the number.
# Now mark all the elements which are divisible by 2,3,5,7.. and so on as they can't be prime numbers.
# Repeat till there are no more such numbers. The unmarked ones are prime numbers.

from math import sqrt

def sieve_of_eratosthenes(n):
    
    # Initialising a list of size n with 1 to keep track of prime numbers
    is_prime = [1] * n

    # We want to find prime till n but going up to the square root of n would suffice.
    # Why? Because if n is not prime then it can be de-composed into at least two factors,
    # and one of those factors must be smaller than or equal to the square of n.
    # If this was not true (i.e., both factors were larger than the square of n) the
    # resulting number would be larger the n itself.
    for i in range(2, int(sqrt(n)) + 1):

        # if the number is prime
        if is_prime[i]:

            # print the number
            print(i)

            # mark all multiples of i , starting from square, lesser or equal than n (k * i ≤ n, k ≥ i) 
            # as 0 indicating non-prime
            for k in range(i * i, n, i):
                is_prime[k] = 0

    # check the numbers in range root(n) to n
    for j in range(int(sqrt(n)) + 1, n):

        # if unmarked i.e 1 thus they are prime numbers
        if is_prime[j]:
            
            # print them
            print(j)


# Driver Code
sieve_of_eratosthenes(30)

# Time Complexity : O(n*log(log(n)))
# Space Complexity : O(n)
