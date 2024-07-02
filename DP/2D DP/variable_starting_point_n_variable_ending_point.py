"""
Now, the case is 
Variable Starting point
Variable Ending Point

start from any row of starting point and end at any row of starting point
and minimise the sum


# RECURSION
1. Express in terms of i, j
2. Perform all possible paths, left, down, right
3. Find Min


Base Case 
    Destination
    Out of bound condition

f(i, j) //Max Path sum to reach (i, j) from any cell in the firest row

TC - 3^n
f(row, col)

   # # Base Case

   # Out of bound
   if row < 0 or j>= rows 
   return INT_MIN

   # Destination
   if row==0 return a[row][col]


   up = a[i][j] + f(row-1, col)
   left_diagonal = a[i][j] + f(row-1, col-1)
   right_diagonal = a[i][j] + f(row-1, col+1)

   return max(st, lt, rt)

"""

# MEMOIZATION
from typing import List
import sys
def min_path(row:int, col:int, matrix:List[List[int]], dp:List[List[int]])->int:

    # Base Cases

    # # Index out of bound
    if col < 0 or col >= len(matrix[0]):
        return int(1e9)
    
    # # Destination
    if row == 0:
        return matrix[row][col]
    

    if dp[row][col] != -1:
        return dp[row][col]
    

    up = matrix[row][col] + min_path(row-1, col, matrix, dp)
    left_diagonal = matrix[row][col] + min_path(row-1, col-1, matrix, dp)
    right_diagonal = matrix[row][col] + min_path(row-1, col+1, matrix, dp)

    dp[row][col] = min(up, left_diagonal, right_diagonal)

    return dp[row][col]

def get_min_path_sum(matrix:List[List[int]])->int:
    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[-1 for _ in range (cols)]for _ in range (rows)]

    mini = sys.maxsize

    for i in range(cols):
        mini = min(mini, min_path(rows-1, i, matrix, dp))


    return mini


# TABULATION | Base case to recursion
def min_path_tabulation(matrix:List[List[int]])->int:

    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0 for _ in range(cols)]for _ in range(rows)]

    # fill the 1st row of dp with the values of 1st row of matrix

    for i in range (cols):
        dp[0][i] = matrix[0][i]


    for row in range(1, rows):

        for col in range(0, cols):

            up = matrix[row][col] + dp[row-1][col]

            left_diagonal = matrix[row][col]
            if col-1>=0:
                left_diagonal += dp[row-1][col-1]
            else:
                left_diagonal += int(1e9)

            
            right_diagonal = matrix[row][col] 
            if col+1 < cols:
                right_diagonal += dp[row-1][col+1]
            else:
                right_diagonal += int(1e9)

    
            dp[row][col] = min(up, left_diagonal, right_diagonal)


    mini = int(1e9)
    for j in range(cols):
        mini = min(mini, dp[rows-1][j])

    
    return mini
    

# Space Optimization

def min_path_tabulation_optmized(matrix:List[List[int]])->int:

    rows = len(matrix)
    cols = len(matrix[0])

    prev = [0]* cols

    # fill the 1st row of dp with the values of 1st row of matrix

    for i in range (cols):
        prev[i] = matrix[0][i]


    for row in range(1, rows):
        curr = [0]* cols

        for col in range(0, cols):

            up = matrix[row][col] + prev[col]

            left_diagonal = matrix[row][col]
            if col-1>=0:
                left_diagonal += prev[col-1]
            else:
                left_diagonal += int(1e9)

            
            right_diagonal = matrix[row][col] 
            if col+1 < cols:
                right_diagonal += prev[col+1]
            else:
                right_diagonal += int(1e9)

    
            curr[col] = min(up, left_diagonal, right_diagonal)
        prev = curr


    mini = int(1e9)
    for j in range(cols):
        mini = min(mini, prev[j])

    
    return mini

# TestCases

if __name__ == "__main__":
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    matrix2 = [[17,82],[1,-44]]

    print(get_min_path_sum(matrix)) 
    print(min_path_tabulation(matrix)) 
    print(min_path_tabulation_optmized(matrix2)) 

