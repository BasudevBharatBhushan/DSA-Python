# KADEN'S ALGORITHM

import sys

def max_subarray(arr):
    
    curr_sum =  0
    max_sum =  -sys.maxsize - 1
    n = len(arr)

    for i in range(n):
        curr_sum += arr[i]

        if curr_sum < 0:
            curr_sum = 0
        
        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum