"""
fixed 2 starting point

variable ending point

Alice(0,0)
Bob (0,c-1)


2 3 1 2
3 4 2 2 
5 6 3 5

Alice = 2 + 4  + 6
Bob = 2 + 2 + 5

paths down, left diagonal, right diagonal

all paths by Alice + all paths by Bob
[common cell should be counted once]


f(i, j1, j2)  f(0,0,m-1)

# BASE CASES

# Out of Boundary Case
if (j1< 0 or j1 > =m or j2< 0 or j2>=m)
    return -int('min')

# Destination Base Case
if (i==n-1)
    if j1 == j2:: return a[i][j1]
else:
    return a[i][j1] + a[i][j2]

    
# # Recursive Function

for every 3 movement of Alice there is simultaneously 3 movement of Bob = 9 combos

# # Explore all paths [Write a for loop to generate all the 9 combos]   which are col-1 col col +1 of row +1  //read it again to understand.

maxi = 0

for (dj1 -> -1 to +1) 
    for (dj2 -> -1 to +1)


       sum =  f(i+1, j1+dj1 , j2+dj2)
       

       if j1==j2: 
           sum += a[i][j1] 
        else:
            sum += (a[i][j1] + a[i][j2])

            
        maxi = max(maxi , sum)

        return maxi


    -----------------------------------------
    TC - 3^N * 3*N
    SC - O(n)

"""
from typing import List

# MEMOIZATION | TC - o(N*M*M) * 9 | SC = O(N*M*M) + O(N) (RECURSION STACK SPACE)

"""
n = rows
m = cols
"""

def max_cherry(i:int, j1:int, j2:int, n, m ,grid, dp )->int:

    # Base Case's

    # # Index out of bound
    if j1< 0 or j1>=m or j2<0 or j2>=m:
        return int(-1e9)
    
    # # Destination Base Case
    if i == n-1:
        if j1 == j2:
            return grid[i][j1]
        else:
            return grid[i][j1] + grid[i][j2]
        
    
    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2]
    
    # # Explore all the 9 combos

    maxi = int(-1e9)

    for di in range(-1, 2):
        for dj in range(-1, 2):
            
            sum = max_cherry(i+1, j1+di, j2+dj, n, m, grid, dp )


            if di == dj:
                sum += grid[i][j1]
            else:
                sum += (grid[i][j1] + grid[i][j2])

            maxi = max(maxi, sum)


    dp[i][j1][j2] = maxi

    
    return maxi


# TABULATION | Base Case to recursion

def max_cherry(grid:List[List[int]])->int:
    n = len(grid)
    m = len(grid[0])

    dp = [[[-1 for _ in range(m)]for _ in range(m)]for _ in range(n)]


    # Fill out values of DP for the destination index

    for i in range(m):
        for j in range(m):

            if i == j:
                dp[n-1][i][j] = grid[n-1][i]
            else:
                dp[n-1][i][j] = grid[n-1][i] + grid[n-1][j]



    for i in range(n-2, -1, -1):
        for j1 in range(m):
            for j2 in range(m):
                maxi = int(-1e9)

                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ans = 0

                        if j1 == j2:
                            ans = grid[i][j1]

                        else:
                            ans = grid[i][j1] + grid[i][j2]

                        
                        if (j1 + di < 0 or j1 + di >=m) or (j2 + dj < 0 or j2 + dj >=m):
                            ans += int(-1e9)
                        else:
                            ans += dp[i+1][j1+di][j2+dj]

                        maxi = max(ans, maxi)
                dp[i][j1][j2] = maxi

    return dp[0][0][m-1]


# SPACE OPTMIZATION

def max_cherry_space_optimization(grid:List[List[int]])->int:
    n = len(grid)
    m = len(grid[0])

    front = [[0 for _ in range(m)]for _ in range(m)]


    # Fill out values of DP for the destination index

    for i in range(m):

        for j in range(m):

            if i == j:
                front[i][j] = grid[n-1][i]
            else:
                front[i][j] = grid[n-1][i] + grid[n-1][j]

    
    for i in range(n-2, -1, -1):
        curr = [[0 for _ in range(m)]for _ in range(m)]

        for j1 in range(m):
            for j2 in range(m):
                maxi = int(-1e9)
                
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        
                        ans = 0

                        if j1 == j2:
                            ans = grid[i][j1]
                        
                        else:
                            ans = grid[i][j1] + grid[i][j2]


                        if (j1+di < 0 or j1+di >=m) or (j2+dj < 0 or j2+dj >=m):
                            ans += int(-1e9)
                        else:
                            ans += front[j1+di][j2+dj]

                        maxi = max(maxi, ans)
                
                curr[j1][j2] = maxi
        
        front = [row[:] for row in curr]

    return front[0][m-1]
            





    





def main():
    # Define the input matrix and its dimensions
    matrix = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
    n = len(matrix)
    m = len(matrix[0])

    dp = [[[-1 for _ in range(m)]for _ in range(m)]for _ in range(n)]
    
    # Call the maximumChocolates function and print the result
    # print(max_cherry(0,0,m-1,n,m,matrix,dp))
    print(max_cherry_space_optimization(matrix))

if __name__ == "__main__":
    main()
