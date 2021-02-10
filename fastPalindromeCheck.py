# Check if the number is palindrome (faster way)

import math

"""

Algorithm:

A brute-force approach would be to convert the input to a string and then iterate through the string, 
pairwise comparing digits starting from the least significant digit and the most significant digit, and working 
inwards, stopping if there is a mismatch. The time and space complexity are O(n),where n is the number of digits in 
the input. We can avoid the O(n) space complexity used by the string representation by directly extracting the digits 
from the input. The number of digits, n, in the input's string representation is the log (base 10) of the input 
value, r. To be precise, n = math.floor(math.log10(x)) + 1. Therefore, the least significant digit is x mod 10, 
and the most significant digit is x/10^(n-1) .In the program below, we iteratively compare the most and least 
significant digits, and then remove them from the input. 

"""


def isPalindromeNumber(x):
    if x <= 0:
        return x == 0

    numDigits = math.floor(math.log10(x)) + 1
    msdMask = 10 ** (numDigits - 1)
    for i in range(numDigits // 2):
        if x // msdMask != x % 10:
            return False

        # Remove the most significant digit of x
        x %= msdMask

        # Remove the least significant digit of x.
        x //= 10

        msdMask //= 100
    return True


# driver code
n = 121
print(isPalindromeNumber(n))

# Time Complexity : O(n)
# Space Complexity : O(1)
