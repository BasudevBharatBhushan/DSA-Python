def cherry_pickup(grid):
    n = len(grid)
    
    def dp(r1, c1, r2, c2):
        c2 = r1 + c1 - r2  # Since r1 + c1 == r2 + c2
        # If out of bounds or hit a thorn
        if r1 >= n or c1 >= n or r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return -int(1e9)
        
        # If both persons reached the bottom-right corner
        if r1 == n - 1 and c1 == n - 1:
            return grid[r1][c1]
        
        # Collect cherries
        if r1 == r2 and c1 == c2:
            cherries = grid[r1][c1]
        else:
            cherries = grid[r1][c1] + grid[r2][c2]
        
        # Move to the next state
        cherries += max(dp(r1 + 1, c1, r2 + 1, c2),
                        dp(r1 + 1, c1, r2, c2 + 1),
                        dp(r1, c1 + 1, r2 + 1, c2),
                        dp(r1, c1 + 1, r2, c2 + 1))
        
        return cherries

    result = dp(0, 0, 0, 0)
    return max(result, 0)  # Ensure non-negative result

# Example usage
grid = [
    [0, 1, -1],
    [1, 0, -1],
    [1, 1, 1]
]
print(cherry_pickup(grid))  # Output: 5
