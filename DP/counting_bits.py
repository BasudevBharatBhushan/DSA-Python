"""
COUNTING BITS


RECURSIVE SOLUTION

f(n) = str(n%2) +  f(n/2)

"""
from typing import list

def countOnes(n:int):

    # # Base Case
    if n == 0:
        return 0
    
    return (n%2) + countOnes(n//2)

def countOnes_memo(n, memo):
    if n == 0:
        return 0
    
    if n in memo:
        return memo[n]
    
    memo[n] = (n%2) + countOnes_memo(n//2)
    return memo[n]
 

def counting_bits_recursion(n:int)->str:

    memo = {}
    ans = []

    for i in range(n+1):
        ans.append(countOnes_memo(i, memo))
    
    return ans
    

def counting_bits_tabulation(n:int)->list[int]:
    dp  = [0] * (n+1)

    for i in range(1, n+1):
        dp[i] = dp[i//2] + (i%2)

    return dp
    


## Test Case

n = 8
print(countOnes(n))