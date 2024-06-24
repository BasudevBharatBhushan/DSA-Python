"""
FROG JUMP


10 20 30 10

Recursion - All Possible ways

1. Breakdown in form of index
2. Do all possible case on the index
3. Take the min (all stuffs)

----------------

The energy required to jump from the ith stone to the jth stone is
abs(stones[i] - stones[j])

Recurance function 

left = [Recursion through i-1] + enrgy required to jump from i to i-1
right = [Recursion through i-2] + enrgy required to jump from i to i-2

f(ind)

    if ind == 0
        return 0

    left = f(ind-1) + abs(stones[ind] - stones[ind-1])

    if i>1
        right = f(ind-2) + abs(stones[ind] - stones[ind-2])

    return min(left,right)

    ----------------------------------

Recursion Tree

    f(3)
|
|-- f(2) + abs(stones[3] - stones[2])
|   |
|   |-- f(1) + abs(stones[2] - stones[1])
|   |   |
|   |   |-- f(0) + abs(stones[1] - stones[0])
|   |
|   |-- f(0) + abs(stones[2] - stones[0])
|
|-- f(1) + abs(stones[3] - stones[1])
    |
    |-- f(0) + abs(stones[1] - stones[0])


"""

# Recursion

def frogJump(stones, ind):

    if ind == 0:
        return 0
    
    left = frogJump(stones, ind-1) + abs(stones[ind] - stones[ind-1])

    right = float('inf')
    if ind > 1:
        right = frogJump(stones, ind-2) + abs(stones[ind] - stones[ind-2])

    return min(left, right)


# Memoization
def frogJump_memoization(stones, ind, dp):

    if ind == 0:
        return 0
    
    if dp[ind] != -1:
        return dp[ind]


    left = frogJump_memoization(stones, ind-1, dp) + abs(stones[ind] - stones[ind-1])

    right = float('inf')
    if ind > 1:
        right = frogJump_memoization(stones, ind-2, dp) + abs(stones[ind] - stones[ind-2])

    
    dp[ind] = min(left, right)

    return dp[ind]


# Tabulation

def frogJump_tabulation(stones):

    n = len(stones)

    dp = [float('inf')] * (n)

    dp[0] = 0

    for i in range(1, n):
       

        left = dp[i-1] +  abs(stones[i] - stones[i-1]) 

        right = float('inf')
        if i > 1:
            right = dp[i-2] +  abs(stones[i] - stones[i-2]) 

        dp[i] = min(left, right)

    return dp[n-1]


# Tabulation  | Optimized

def frogJump_tabulation_optimized(stones):
    n = len(stones)

    a = 0

    b = 0

    for i in range(1, n):
        a = a + abs(stones[i] - stones[i-1])

        if i > 1:
            b = b + abs(stones[i] - stones[i-2])

        c = min(a, b)

        a = b
        b = c

    return c


"""
Variation II

if frog can jump till i-1, i-2, i-3...i-k
--------------------------------------------------

f(ind)

    ind == 0 return 0

    minSteps = INT_MAX

    for(j - 1; j <=k ; j++)

        if ind-j >=0 
            jump = f(ind-j) + abs(a[ind] -a[ind-j])

        minSteps = min(minSteps, jump)

        TC - for every juction there is k steps o(N) * K

        






"""

# Variation II tablulation

def frogJump_variation_ii(stones, k:int):

    n  = len(stones)

    dp = [float('inf')] * (n)

    dp[0] = 0

    for i in range(1, n):
            
            minSteps = float('inf')
    
            for j in range(1, k+1):
    
                if i-j >= 0:
                    jump = dp[i-j] + abs(stones[i] - stones[i-j])
    
                    minSteps = min(minSteps, jump)
    
            dp[i] = minSteps

    return dp[n-1]

    







# Test Cases
stones = [10,20,30, 10]
n = len(stones)
ind = len(stones)-1
dp = [-1] * (n)

print(frogJump(stones, ind))
print(frogJump_memoization(stones, ind, dp))
print(frogJump_tabulation(stones))
print(frogJump_tabulation_optimized(stones))