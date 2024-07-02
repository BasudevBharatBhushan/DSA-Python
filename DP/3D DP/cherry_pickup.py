"""
You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through,
1 means the cell contains a cherry that you can pick up and pass through, or
-1 means the cell contains a thorn that blocks your way.


Return the maximum number of cherries you can collect by following the rules below:

fixed starting and fixed destination
n*n

f(i , j) === f(n-1, n-1)

# Base Cases

# # Out of Bound
if i < 0 or j < 0:
    return int(-1e9)

# # Blocked Cell
if grid[i][j] == -1:
    return int(-1e9)

# # Destination
if i == 0 and j == 0:
    return grid[0][0]


# # Recursion

sum = grid[i][j]

up = sum + f(i-1, j)
left = sum + f(i, j-1)

return max(up, left)


2 round trips required
above soltion only handle for 1 trip


---------------

what if I consider two person

"""

def cherry_pickup(i1, j1, i2,j2, grid):
    n = len(grid)
    # Base Cases

    if i1 >= n or j1 >= n or i2 >= n or j2 >= n or grid[i1][j1] == -1 or grid[i2][j2] == -1:
        return -int(1e9)
    
    
    if i1 == n-1 and j1 == n-1:
        return grid[i1][j1]
    

    # Recursion

    if i1 == i2 and j1 == j2:
        cherries = grid[i1][j1]
    else:
        cherries = grid[i1][j1] + grid[i2][j2]

    # maxi = int(-1e9)
    # for di in range(0, 2):
    #     for dj in range(0,2):

    #         sum = cherry_pickup(i1+di, j1+dj, i2+di, j2+dj, grid)
    #         maxi = max(maxi, sum)

    
    # cherries += maxi
    # Move to the next state
    cherries += max(cherry_pickup(i1 + 1, j1, i2 + 1, j2, grid),
                    cherry_pickup(i1 + 1, j1, i2, j2 + 1, grid),
                    cherry_pickup(i1, j1 + 1, i2 + 1, j2, grid),
                    cherry_pickup(i1, j1 + 1, i2, j2 + 1, grid))

    return cherries



# MEMOIZAATION
def cherry_pickup(i1, j1, i2,j2, grid, dp):
    n = len(grid)
    # Base Cases

    if i1 >= n or j1 >= n or i2 >= n or j2 >= n or grid[i1][j1] == -1 or grid[i2][j2] == -1:
        return -int(1e9)
    
    
    if i1 == n-1 and j1 == n-1:
        return grid[i1][j1]
    

    # Recursion

    if i1 == i2 and j1 == j2:
        cherries = grid[i1][j1]
    else:
        cherries = grid[i1][j1] + grid[i2][j2]

    if dp[i1][j1][i2][j2]!= -1:
        return dp[i1][j1][i2][j2]

    cherries += max(cherry_pickup(i1 + 1, j1, i2 + 1, j2, grid, dp),
                    cherry_pickup(i1 + 1, j1, i2, j2 + 1, grid, dp),
                    cherry_pickup(i1, j1 + 1, i2 + 1, j2, grid, dp),
                    cherry_pickup(i1, j1 + 1, i2, j2 + 1, grid, dp))

    dp[i1][j1][i2][j2] =  cherries

    return dp[i1][j1][i2][j2]


# TABULATION



if __name__ == '__main__':
    grid = [[0,1,-1],[1,0,-1],[1,1,1]]
    n = len(grid)

    dp = [[[[ -1 for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
    
    print(cherry_pickup(0,0,0,0, grid, dp))
    

