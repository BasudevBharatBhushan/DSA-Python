#rotate_matrix.py

"""
Inputs: N*N matrix

"""
# Brute Force Approach | TC - O (n*n) , SC - O(n*n)

from typing import List
def rotate (matrix: List[List[int]])-> List[List[int]]:
    n = len(matrix)
    rotated = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = matrix[i][j]
    return rotated

# Optimal Approach [Transpose of Matrix]

def rotate_transpose(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)

    # transposing the matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reversing the matrix
    for i in range(n):
        matrix[i].reverse()

