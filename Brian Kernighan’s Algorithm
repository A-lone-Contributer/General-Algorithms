# Brian Kernighan’s Algorithm

# This algorithm is used to find the number of set bits in a binary number.

# Algorithm
# We try to flip each set bit(unset) in the binary number to 0 and count them.
# To unset the bits subtract the number by one and do bitwise AND with the number
# repeat this till the number becomes zero 


res=0
while n:
    n&=(n-1)
    res+=1
    

# Driver code
n=int(input())
print(res)

# Time Complexity : O(logn)
# Space Complexity : O(1)
