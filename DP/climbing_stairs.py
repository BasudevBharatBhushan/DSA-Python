"""
CLIMBING STAIRS

- How to understand that this is the DP Problem?
  - count the total no of ways
  - min/max output out of all possible ways

Try all possible ways - Recursion

1. Breakdown in form of index
2. Do all possible case on the index ac to the problem statement
3. 
Sum of the all the stuffs - Count all ways
min/max of all the stuffs - Min/Max output

###################

Recursive Reln

f(ind){

    if ind == 0
        return 1

    l = f(ind-1)

    r = 0
    if ind>1
        r = f(ind-2)

    return l+r

}


------
Memoization

f(ind)

    if ind == 0
        return 1

    if dp[ind] is not -1
        return dp[ind]

    l = f(ind-1)
    
    if ind>1
        r = f(ind-2)

    dp[ind] = l+r

    return dp[ind]


"""

# Tabulation

def climb_stairs(n:int)->int:

    dp = [-1] * (n+1)

    dp[0] = 1

    for i in range(1, n+1):
        dp[i] = dp[i-1]
        if i > 1:
            dp[i] += dp[i-2]

    return dp[n]

# Tabulation - Space Optimized
def climb_stairs_optimized(n:int)->int:

    if n == 0:
        return 1
    
    if n == 1:
        return 1

    a = 1
    b = 1
    
    for i in range(2, n+1):
        
        curr = a + b
        a = b
        b = curr

    return b

# Test Cases
n = 3
print(climb_stairs(n)) # 3
