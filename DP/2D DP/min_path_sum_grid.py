"""
MINIMUM PATH SUM IN GRID

---------
RECURRENCE RELATION

f(i, j , grid)

# # Base Case
if i == 0 and j == 0
    return grid[i][j]

if i<0 or j <0:
    return INT_MAX //so that it should not taken into the calculation


up = grid[i][j] + f(i-1, j)
left = grid[i][j] + f(i, j-1)


return min(up, left)


"""

# MEMOIZAION

from typing import List
def min_path_sum(rows:int, cols:int, grid:List[List[int]], dp:List[List[int]])->int:

    # # Base Cases

    if rows == 0 and cols == 0:
        return grid[rows][cols]
    
    if rows<0 or cols<0:
        return float('inf')
    

    # # Recursion
    
    if dp[rows][cols] != -1:
        return dp[rows][cols]

    up = grid[rows][cols] + min_path_sum(rows-1, cols, grid, dp)
    left = grid[rows][cols] + min_path_sum(rows, cols-1, grid, dp)

    return min(up, left)

# TABULATION
def min_path_sum_tabulation(grid:List[List[int]])->int:

    rows = len(grid)
    cols = len(grid[0])

    dp = [[0 for _ in range (cols)] for _ in range (rows)]

    for row in range(0, rows):
        for col in range(0, cols):

            if row == 0 and col == 0:
                dp[row][col] = grid[row][col]

            else:
                up = float('inf')
                left = float('inf')


                if row>0:
                    up = grid[row][col] + dp[row-1][col]

                if col>0:
                    left = grid[row][col] + dp[row][col-1]

                
                min_path = min(up, left)

                dp[row][col] = min_path
        

    return dp[rows-1][cols-1]


# Tabulation Optimized

def min_path_sum_tabulation_optimized(grid:List[List[int]])->int:
    rows = len(grid)
    cols = len(grid[0])

    prev = [0] * cols

    for row in range(0, rows):
        curr = [0] * cols
        for  col in range(0, cols):

            if row == 0 and col == 0:
                curr[col] = grid[row][col]

            else:

                up = float('inf')
                left = float('inf')

                if row > 0:
                    up = grid[row][col] + prev[col]

                if col > 0:
                    left = grid[row][col] + curr[col-1]

                min_sum = min(up, left)

                curr[col] = min_sum

        prev = curr


    return prev[cols-1]




# Test Cases
if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    rows = len(grid)
    cols = len(grid[0])
    dp = [[-1 for _ in range(cols)] for _ in range(rows)]
    print(min_path_sum(rows-1, cols-1, grid, dp)) # 7
    print(min_path_sum_tabulation( grid)) # 7
    print(min_path_sum_tabulation_optimized( grid)) # 7