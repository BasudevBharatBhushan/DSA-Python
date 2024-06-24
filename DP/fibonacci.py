"""
DYNAMIC PROGRAMMMING
--------------------------------------------------------


0 1 1 2 3 5 8


0. Overlapping Subproblems
------------------------


Recurance reln:  [Top Down Approach]
f(n) = f(n-1) + f(n-2)

---
f(n)
    if n <=1 
        reutn n;
    return f(n-1)  + f(n-2)

---- > Overlapping subproblems
--------------------------------------------


1. Memoization
------------------
f(n)

    if n<=1 
        return n;

    if dp[n] is not -1:
        return dp[n]
    else
        dp[n] = f(n-1) + f(n-2)

    
    return dp[n]
----------------------
TC -> O(N) Linear Pattern
SC -> O(N) Constant Array   
-------------------------------------------

2. Tabulation [Bottom Up--- BaseCase to required approach ]


------------------

dp = [0]*(n+1)

dp[0] = 0
dp[1] = 1

for i=2 ->  n:
    dp[i] = dp[i-1] + dp[i-2]

    
return dp[n]

---------------------
TC -> O(N)
SC -> O(N) Constant Array
Elimating the recursion stack space

-------------------------------------------

3. Optimized Tabluation [Eliminating the array O[n]]
------------------------------------------------------------
a = 0
b = 1

for i=2 -> n:
    c = a+b
    a = b
    b = c

return c


"""

# Memoization

def fibonacci_memoization(n, dp):

    if n<=1:
        return n
    
    if dp[n]!= -1:
        return dp[n]
    
    dp[n] = fibonacci_memoization(n-1, dp) + fibonacci_memoization(n-2, dp)


    return dp[n]

# Tabulation
def fibonacci_tabulation(n):

    dp = [-1] * (n+1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


# Tabulation [Removing Linear Space]
def fibonacci_tabulation_optimized(n):
    a = 0
    b = 1

    if n is 0 or n is 1:
        return n


    for i in range(2, n+1):
        c = a + b
        a = b
        b = c


    return c



## Test Cases
n = 6
dp = [-1]*(n+1)
print(fibonacci_memoization(n, dp))
print(fibonacci_tabulation(n))
print(fibonacci_tabulation_optimized(n))