# Unique Paths of Robot
from typing import List
"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

"""

# Approach 1
# Brute Force Approach

# Recursive Approach

'''
With this approach, the timelimit exceeded for the case m = 23 and n = 12

TC - O(2^(m+n)) [Exponential], SC - O(m+n)
'''

def uniquePaths(m:int , n:int) -> int:
    def countPaths(i:int, j:int, n:int, m:int)->int:
        if i == n-1 and j == m-1:
            return 1
        if i>=n or j >= m:
            return 0
        
        else:
            return countPaths(i+1, j, n, m) + countPaths(i, j+1, n, m)
        
    return countPaths(0,0, n, m)



# Test Cases
m = 3
n = 7
print(uniquePaths(m, n)) # 28


# Approach 2
# Dynamic Programming  [Avoiding sub-overlapping problems]
# TC - O(m*n), SC - O(m*n)

def countPaths(i:int, j:int, n:int, m:int, dp:List[List[int]])->int:
    if i == n-1 and j == m-1:
        return 1
    
    if i>=n or j >= m:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    else:
        dp[i][j] = countPaths(i+1, j, n, m, dp) + countPaths(i, j+1, n, m, dp)

        return dp[i][j]
    

# Approach 3  | Combinatorics

"""
Total no of direction needed to be taken everytime is m-1 + n-1 = m+n-2

Out of these m-1 directions are right and n-1 directions are down

Combination Approach
m = 3, n = 2, m+n-2 = 3
_ _ _
B R R 
R R B
R B R    

= C(3,2)  = C (m+n-2, m-1) = (m+n-2)! / (m-1)!(n-1)!

TC - O(m-1) or O(n-1), SC - O(1)

eg. 
m+n-2 = 16
m-1 = 3

C (16,3) = 16!/3! 13! = 16*15*14/3*2*1

14/1 * 15/2 * 16/3 = 560

res = res * (total_directions - right_directions + i)//i

"""

def uniquePaths_combinatorics(m:int, n:int)->int:
    total_directions = m+n-2
    right_directions = m-1

    res = 1

    for i in range(1, right_directions+1):
        res *= res * (total_directions - right_directions + i)//i
    
    return int(res)
