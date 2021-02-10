# Kadane Algorithm

# This algorithm is used to find the maximum sum contiguous sub-array efficiently (Uses Dynamic Programming)

# A maximum sum contiguous sub-array is the one which has the maximum sum among all
# the sub-arrays and is contiguous.

# Algorithm:
# We keep two variables max_so_far (has the maximum sum so far) and max_ending here
# (look for all positive contiguous segments of the array).
# keep on adding elements of array to max_ending_here and compare with max_so_far
# and update the value of max_so_far is necessary

from sys import maxsize

def kadane(arr, n):

    # initialise variables as discussed in above algorithm
    # max_so_far is initialised with min value possible and max_ending_here with 0
    max_so_far, max_ending_here = -maxsize - 1, 0

    # variables to keep track of start and end of sub-array
    start, end = 0, 0

    # loop through all values
    for i in range(0, n):

        # keep adding elements of array to max_ending_here
        max_ending_here += arr[i]

        # compare max_ending_here and max_so_far and if max_ending_here exceeds max_so_far
        if max_ending_here > max_so_far:

            # update max_so_far
            max_so_far = max_ending_here

            # update the end index where we found new max_so_far
            end = i

        # if max_ending_here is negative
        if max_ending_here < 0:

            # update max_ending_here to 0
            max_ending_here = 0

            # keep on incrementing the start index
            start = i + 1

    # print the maximum sum and the range
    print(f"Maximum contiguous sum is {max_so_far} starting from index {start} to index {end}")


# Driver Code
arr = [-2, -3, 7, -3, -1, 4, 5, -3]
kadane(arr, len(arr))

# Time Complexity : O(n)
# Space Complexity : O(1)
