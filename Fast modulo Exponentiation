# Fast Modular Exponentiation

# Modulus is the most common operation while handling overflows, we modulo the
# large number so limit it to primitive data types range.
# So the problem is to find the nth power of a number and find its modulo,
# it can be calculated faster than you think so lets discuss it.

# Approach:
# A common approach to find the power is to iteratively square the number and take modulo at the end
# but easy approach comes with time complexity of O(n). We want better than this!
# We cannot do it in O(1) as we have n in the equation itself. So what about O(log(n))?

# Algorithm:
# Divide the problem into subproblems of size n/2
# If the number is even then simply multiply the subproblems
# else we get an extra factor which we will multiply at each point
# Repeat till we power is exhausted.


def fast_exponentiation(digit, n, p):

    # Initialise result
    result = 1

    # (ab) mod p = ( (a mod p) (b mod p) ) mod
    # calculate initial modulo
    digit = digit % p

    # while there is power left
    while n:

        # check if odd
        if int(n) & 1:
            result = (result * digit) % p

        # for even
        n /= 2
        digit = (digit ** 2) % p

    return result


# Driver Code
print(fast_exponentiation(6, 23, 13))


# Time Complexity : O(log(n))
# Space Complexity : O(1)
