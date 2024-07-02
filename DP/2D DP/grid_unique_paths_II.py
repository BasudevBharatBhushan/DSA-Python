"""
here is a bloackage/dead shell with value -1


fn(i, j)

    //Base Case

    if i>=0 and j>=0 and a[i][j] ==-1   # # Check for deadend
        return 0

    
    if i == 0 and j == 0
        return 1

    if i<0 or j<0 return 0

    
    //Recurance relation




"""
from typing import List

# Tabulation | TC - O(N*M) SC - (N*M)

def uniquePaths_tabulation(m:int, n:int, grid:List[List[int]])->int:
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # Base Case
    # # Every cell has been initialized to zero above


    dp[0][0] = 1

    for row in range(0, m):
        for col in range(0, n):

            if grid[row][col] == -1:
                dp[row][col] = 0

            elif row == 0 and col == 0:
                dp[row][col] = 1
            
            else:
            
                up = 0
                if row > 0:
                    up = dp[row-1][col]

                left = 0
                if col > 0:
                    left = dp[row][col-1]
                

                dp[row][col] = up + left
                # print(row, col)

    
    return dp[m-1][n-1]



# Taabulation | Space optimized | Just store the previous ROW
def uniquePaths_tabulation_optimized(m:int, n:int, grid:List[List[int]])->int:
    
    # Base Case
    # # Every cell has been initialized to zero above

    prev = [0] * (n)

    for row in range(0, m):
        curr = [0] * (n)
        for col in range(0, n):
            
            if grid[row][col] == -1:
                curr[col] = 0

            elif row == 0 and col ==0:
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

    # # Test Case 1
    # m = 3
    # n = 3
    # grid = [[0,0,0],[0,-1,0],[0,0,0]]
    # # Output: 28
    # print(uniquePaths_tabulation(m, n, grid))
    # print(uniquePaths_tabulation_optimized(m, n, grid))

    # # Test Case 2
    m = 3
    n = 2
    grid = [[0,0],[0,0],[0,0]]
    # Output: 3
    print(uniquePaths_tabulation(m, n, grid))
    # print(uniquePaths_tabulation_optimized(m, n, grid))

   