from typing import List
# Binary Search Approcah

def binarySearch(nums, target):
    n = len(nums)

    # if len == 1:
    #     return nums[0] == target

    low, high = 0, n-1

    while low<= high:
        mid = (low + high)//2

        if nums[mid] == target:
            return True
        
        elif target> nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


# Complexity - O(nlogm), since we are performing binary search on each row and SPACE - O(1)
def searchMatrix(matrix, target):
    n = len(matrix) # number of rows
    m = len(matrix[0])  # number of columns


    for i in range(n):
        
       
        # For every row, perform the binary search
        # print(matrix[i][0], matrix[i][m-1])
        if matrix[i][0] <= target <= matrix[i][m-1]:
            
            return binarySearch(matrix[i], target)

    return False
    

# # Flattening of the Matrix
"""
To get the 2D coordinate for the 1D flattened array, 
The formula is

row = index // m
col = index % m

TC  - O(log(m*n)), SC - O(1)
"""
def serachMatrix_optimal(matrix:List[List[int]], target:int)->bool:
    n = len(matrix)
    m = len(matrix[0])

    low = 0
    high = n*m -1

    while low <= high:

        mid = (low + high) // 2
        row  = mid // m
        col = mid % m

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1

        else:
            high = mid - 1
    
    return False










# Test Cases
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# matrix = [[1],[3]]
matrix = [[1,3,5]]
target = 1
print(serachMatrix_optimal(matrix, target)) # True




