"""
Nth Tribonacci Number

Tn = Tn-1 + Tn-2  + Tn-3

"""

# RECURSION - Top Down Approach

def tribonacci_recursion(n:int)->int:

    # # Base
    if n == 2 or n==1:
        return 1
    
    if n == 0:
        return 0
    
    # # Recursive Relation

    return tribonacci_recursion(n-1) + tribonacci_recursion(n-2) + tribonacci_recursion(n-3)


# # MEMOIZATION
from typing import List
def tribonacci_memoization(n:int, dp:List[int])->int:

    # # Base
    if n == 2 or n==1:
        return 1
    
    if n == 0:
        return 0
    
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = tribonacci_memoization(n-1, dp) + tribonacci_memoization(n-2, dp) + tribonacci_memoization(n-3, dp)

    return dp[n]
    
# # TABULATION  - Base Case to Recursive Approach - Bottom-UP

def tribonacci_tabulation(n:int)->int:

    dp = [-1] * (n+1)

    dp[0] = 0
    dp[1] = 1
    dp[2] = 1

    if n <=2:
        return dp[n]
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]


# # # Space Optimization
def tribonacci_tabulation_optimized(n:int)->int:

    a = 0
    b = 1
    c = 1

    for i in range(3, n + 1):
        temp = a + b + c
        a = b
        b = c
        c = temp

    return c


if __name__  == "__main__":
    # print(tribonacci_recursion(25))

    dp = [-1] * (25+1)

    print(tribonacci_memoization(25, dp))
    print(tribonacci_tabulation_optimized(25))

 