# Segmented Sieve of Eratosthenes

# Sieve of Eratosthenes is a great algorithm but consider a case where the
# size of n is very large so in that case it is difficult to construct sieve.
# Also the Simple sieve has a bad locality of reference.

# If the n value is large or we want to compute prime numbers within a specified
# range then Segmented Sieve comes to the rescue. We have not implemented Segmented 
# sieve for "Specified range" but it can be easily done. Try to do it yourself.

# Algorithm:
# Compute all the prime numbers up-to root(n) using sieve and store it in an array.
# We need primes up-to n so we divide this range into segments of root(n)
# Now for each segment Create an array is-prime[high-low+1].We need only O(K) space where K is
# number of elements in given range.
# Iterate through all primes found in first step and for every prime, mark its multiples in given range.

# Unlike Simple sieve where we need O(n) space , here we need only o(root(n)) space plus
# a better locality of reference.


from math import sqrt, ceil, floor

# for storing pre-computed value of prime
primes = []

# Simple Sieve
def sieve_of_eratosthenes(limit):
    
    # Initialising a list of size limit to keep track of prime numbers
    is_prime = [1] * limit

    # We want to find prime till limit but going up to the square root of limit would suffice.
    # Why? Because if limit is not prime then it can be de-composed into at least two factors,
    # and one of those factors must be smaller than or equal to the square of limit.
    # If this was not true (i.e., both factors were larger than the square of limit) the
    # resulting number would be larger the limit itself.
    for i in range(2, int(sqrt(limit)) + 1):

        # if the number is prime
        if is_prime[i]:

            # store the prime number
            primes.append(i)

            # print the number
            print(i, end=" ")

            # mark all multiples of i , starting from square, lesser or equal than n (k * i ≤ n, k ≥ i)
            # as 0 indicating non-prime
            for k in range(i * i, limit, i):
                is_prime[k] = 0

    # check the numbers in range root(limit) to limit
    for j in range(int(sqrt(limit)) + 1, limit):

        # if unmarked i.e 1 thus they are prime numbers
        if is_prime[j]:
            
            # append them to the list of primes
            primes.append(j)
            
            # print them
            print(j, end=" ")


# segmented sieve function
def segmented_sieve(n):

    # size of segment (root(n))
    segment = int(floor(sqrt(n)) + 1)

    # compute all primes smaller than or equal to segment
    sieve_of_eratosthenes(segment)

    # Divide the range into different segments
    low = segment
    high = segment * 2

    # while all the segments are not processed, process one segment at a time
    while low < n:
        if high >= n:
            high = n

        # Initialising a list of size n to keep track of marked and unmarked numbers
        is_prime = [1] * segment

        # for all primes in primes[]
        for i in range(len(primes)):

            # find the base i.e minimum number in [low..high] that is
            # divisible by primes[i]
            # for example if low is 31 and primes[i] is 3 then base will be 33
            base = ceil(low / primes[i]) * primes[i]

            # loop from base to high taking steps of primes[i]
            for j in range(base, high, primes[i]):
            
                # and mark all the non-primes as 0
                is_prime[j - low] = 0

        # from low to high
        for i in range(low, high):

            # check for the numbers marked as true (those will be primes)
            if is_prime[i - low]:
            
                # print them
                print(i, end=" ")

        # keep incrementing low and high by segment to calculate sieves for each segment
        low += segment
        high += segment


# Driver Code
n = int(input())
print(f"The Prime numbers equal to or less than {n} are :")
segmented_sieve(n)


# Time Complexity : O(n*log(log(n)))
# Space Complexity : O(root(n))
