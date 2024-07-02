"""

Reucrsion 
(0,0) -> (m-1, n-1)
trying out all possible ways = Recursion

1. Express everything in terms in indexes (i, j)
2. Do all possible cases on the indexes according to the problem statement
3. Sum o fall ways / Max/Min of all ways depending on the question

----------------------

f(i, j) -> (m-1, n-1)

--------------------
REUCRSION | TC - O(2^(m*n)) | SC - O(m+n)
--------------------
f(i,j)

     Base Case
        if i == 0 and j == 0
            return 1
        if (i<0 or j<0)  //It got out of the boundary
            return 0

            
        up =  f(i-1, j) 
        left =  f(i, j-1)

        sum = up + left

        return sum


----------------------
f(3,3)

f(3,3)
  /             \
f(2,3)           f(3,2)
  /   \          /    \
f(1,3) f(2,2) f(2,2) f(3,1)   <- f(2,2) is overlapping
 /  \     /    \      /    \      /    \
f(0,3) f(1,2) f(1,2) f(2,1) f(1,2) f(2,1) f(2,1) f(3,0)   <- f(1,2) and f(2,1) are overlapping

----------------------

MEMOIZATION | Remove Overlapping subproblems

f(i,j)

     Base Case
        if i == 0 and j == 0
            return 1
        if (i<0 or j<0)  //It got out of the boundary
            return 0


        dp [i][j] != -1
            return dp[i][j]

            
        up =  f(i-1, j) 
        left =  f(i, j-1)

        sum = up + left

        dp[i][j] = sum

        return dp[i][j]

"""

# MEMOIZATION
from typing import List
def uniquePaths_memoization( m:int, n:int, dp:List[List[int]])->int:

    # # Base Case
    if m == 0 and n == 0:
        return 1
    
    if m<0 and n<0:
        return 0
    

    if dp[m][n] != -1:
        return dp[m][n]
    
    up = uniquePaths_memoization(m-1, n , dp)
    left = uniquePaths_memoization(m, n-1, dp)

    dp[up][left] = up + left

    return dp[up][left]


# Tabulation | TC - O(N*M) SC - (N*M)

def uniquePaths_tabulation(m:int, n:int)->int:
    dp = [[0 for _ in range(m)] for _ in range(n)]

    # Base Case
    # # Every cell has been initialized to zero above

    dp[0][0] = 1

    for row in range(0, m):
        for col in range(0, n):

            if row == 0 and col ==0:
                continue
            
            up = 0
            if row > 0:
                up = dp[row-1][col]

            left = 0
            if col > 0:
                left = dp[row][col-1]
            

            dp[row][col] = up + left

    
    return dp[m-1][n-1]



# Taabulation | Space optimized | Just store the previous ROW
def uniquePaths_tabulation_optimized(m:int, n:int)->int:
    
    # Base Case
    # # Every cell has been initialized to zero above

    prev = [0] * (n)

    for row in range(0, m):
        curr = [0] * (n)
        for col in range(0, n):

            if row == 0 and col ==0:
                curr[col] = 1
            else:
            
                up = 0
                if row > 0:
                    up = prev[col]

                left = 0
                if col > 0:
                    left = curr[col-1]

                curr[col] = up + left
            

        prev = curr

    
    return prev[n-1]


# Test Case
if __name__ == "__main__":

    m = 3
    n = 7

    dp = [[-1 for _ in range(m)] for _ in range(n)]
 
    print(uniquePaths_tabulation_optimized(m, n))