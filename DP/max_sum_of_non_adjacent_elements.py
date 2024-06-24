"""

Maximum sum of non-adjacent elements || House Robber Problem
-------------------------------------------

It will follow the logic of recursion on subsequences (Pick and Non-Pick)

f(ind)

    if ind == 0 return a[ind]
    if ind < 0 return 0


    pick = a[ind] + f[ind-2]  //why because we cannot take the adjacent element

    not_pick = 0 + f[ind-1]

 

"""
from typing import List

# Recursive Solution

def max_sum(a:List[int], ind:int)->int:

    if ind == 0:
        return a[ind]
    
    if ind < 0:
        return 0

    pick = a[ind] + max_sum(a, ind-2)

    not_pick = 0 + max_sum(a, ind-1)

    return max(pick, not_pick)


# Memoization

def max_sum_memoization(a:List[int], ind:int, dp:List[int])->int:

    if ind == 0:
        return a[ind]
    
    if ind < 0:
        return 0
    
    if dp[ind] != -1:
        return dp[ind]
    
    pick = a[ind] + max_sum_memoization(a, ind-2, dp)

    not_pick = 0 + max_sum_memoization(a, ind-1, dp)

    dp[ind] = max(pick, not_pick)

    return dp[ind]



# Tabulation

def max_sum_tabulation(a:List[int] ) -> int:

    n = len(a)

    if n == 1:
        return a[0]
    
    if n == 0:
        return 0

    dp = [-1] * (n)

    dp[0] = a[0]
    neg = 0

    for i in range(1, n):

        pick = a[i]
        if i> 1:
            pick += dp[i-2]

        not_take = 0 + dp[i-1]

        dp[i] = max(pick, not_take)

    
    return dp[n-1]



# Tabulation - Optimized

def max_sum_tabulation_optimized(nums:List)->int:

    n = len(nums)

    if n == 1:
        return a[0]


    if n ==0:
        return 0
    
    b = nums[0]
    a = 0

    for i in range(1, n):

        pick = nums[i]
        if i > 1:
            pick += a

        not_pick = 0 + b

        curr = max(pick, not_pick)

        a = b
        b = curr

    return b

if __name__ == "__main__":
#Test Cases
    a = [2,7,9,3,1]
    print(max_sum(a,len(a)-1) ) # 12
    print(max_sum_tabulation(a)) # 12
    print(max_sum_memoization(a, len(a)-1, [-1]*len(a))) # 12
    print(max_sum_tabulation_optimized(a)) # 12






