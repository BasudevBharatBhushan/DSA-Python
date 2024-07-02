"""

1
2 3
3 6 7
8 9 6 10
----------------------

GOAL: To reach any col of the last row and minimise the sum

Find the minimum Path Sum

Since here multiple ending points, we will start the recursion from start (0,0)


RECURSION
--------------

f(row, col)

# BASE CASE
if row == n-1:
    traingle[row][col]

we will never go outside of the boundary


---------------
diagonal = traingle[row][col] + f(row+1, col+1)
straight = traingle[row][col] + f(row+1, col)

return min(diagonal, straight)


"""

from typing import List

# MEMOIZATION

def min_total(row:int, col:int,triangle:List[List[int]], dp:List[List[int]])->int:

    # Base Case
    if row == len(triangle)-1:
        return triangle[row][col]
    

    if dp[row][col] != -1:
        return dp[row][col]
    
    diagonal = triangle[row][col]+ min_total(row+1, col+1, triangle, dp)
    straight = triangle[row][col] + min_total(row+1, col, triangle, dp)

    dp[row][col] = min(diagonal, straight)

    return dp[row][col]

# TABULATION | Bottom Up Approach | Base Case to Problem
def min_total_tabulation(triangle:List[List[int]])->int:
    rows = len(triangle)
    cols = len(triangle[-1])

    dp = [[0 for _ in range (rows)]for _ in range (rows)]


    # Initialzie the bottow row of the DP with the vlaues from the last row of the triangle
    for j in range (rows):
        dp[rows-1][j] = triangle[rows-1][j]
    

    for row in range (rows-2, -1,-1):
        for col in range(row, -1,-1):

            diagonal = triangle[row][col] + dp[row+1][col+1]
            straight = triangle[row][col] + dp[row+1][col]

            dp[row][col] = min(diagonal, straight)

    
    return dp[0][0]


## TABULATION | SPACE OPTIMIZED

def min_total_tabultaion_optimized(triangle:List[List[int]])->int:
    rows = len(triangle)
    cols = len(triangle[-1])

    prev = [0]* cols

    for j in range(cols):
        prev[j] = triangle[rows-1][j]


    for row in range(rows-2, -1,-1):
        curr = [0] * cols
        for col in range(row, -1,-1):

            diagonal = triangle[row][col] + prev[col+1]
            straight = triangle[row][col] + prev[col]

            curr[col] = min(diagonal, straight)
        
        prev = curr

    
    return prev[0]



# Test Cases
if __name__ == "__main__":
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    rows = len(triangle)
    cols = len(triangle[-1])
    dp = [[-1 for _ in range(cols)] for _ in range(rows)]
    # print(min_total(0, 0, triangle, dp)) # 11
    print(min_total_tabulation(triangle))
    print(min_total_tabultaion_optimized(triangle))