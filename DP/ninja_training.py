"""
 NINJA TRAINING

  f(day, last_activity)

    2  1  3  d0
    3  4  6  d1
    10 1  6  d2
    8  3  7  d3

    ----------------------

    f(day, last, task[][])

1. Recurrence Relation
-----------------
    
    ## BASE CASE
        if day == 0
            maxi = 0
            for (i = 0->2)
                if i != last
                    maxi = max(maxi, task[0][i])
            return maxi

        
        maxi = 0

        for (i = 0->2)
            if i != last
                points = task[day][i] + f(day-1, i , task)
                maxi = max(maxi, points)
        
        return maxi
    

"""
from typing import List

# Recursion
#--------------------------------------------------------------------------------------------
def ninja_training_recursion(day:int, last:int, task:List[List[int]])->int:

# Base Case
    if day == 0:
        maxi = 0
        for i in range(3):
            if i != last:
                maxi = max(maxi, task[0][i])
            return maxi
        

# Recursive Function

    maxi = 0

    for i in range(3):
        if i!= last:
            points = task[day][i] + ninja_training_recursion(day-1, i, task)

            maxi = max(maxi, points)

    
    return maxi

#--------------------------------------------------------------------------------------------
# Memoization | Removing Overlapping Subproblems | TC - O(N*4)*3  | SC- O(N) * O(N*4)

def ninja_training_memoization(day:int, last:int, task:List[List[int]] , dp:List[List[int]])->int:

# Base Case
    if day == 0:
        maxi = 0
        for i in range(3):
            if i != last:
                maxi = max(maxi, task[0][i])
            return maxi
        

    if dp[day][last] != -1:
        return dp[day][last]
    
    for i in range(3):
        points = task[day][i] + ninja_training_recursion(day-1, i, task)

        maxi = max(maxi, points)

    dp[day][last] = maxi
    return dp[day][last]


#-------------------------------------------------------
# TABLULATION | Remove the recursion stack space [base case to required approach]

def ninja_training_tabulation( points:List[List[int]])->int:

    days = len(points)

    # fill -1 in a 2D DP Array
    dp = [[0 for i in range(4)] for j in range(days)]

    # Base Case | Filling values for zeroth day
    dp[0][0] = max(points[0][1] , points[0][2])
    dp[0][1] = max(points[0][2] , points[0][0])
    dp[0][2] = max(points[0][0] , points[0][1])
    dp[0][3] = max(points[0][0] , points[0][1], points[0][2])
    

    for day in range(1, days):
        for last in range(0, days):
            dp[day][last] = 0

            for task in range(0, 3):

                if task != last:
                    point:int = points[day][task] + dp[day-1][task]
                    dp[day][last] = max(dp[day][last] , point)
    

    return dp[days - 1][3]


# Tabulation | Space Optmiized
def ninja_training_tabulation_optimized( points:List[List[int]])->int:

    days = len(points)

    dp = [0] * days


    # Base Case | Filling values for zeroth day
    dp[0] = max(points[0][1] , points[0][2])
    dp[1] = max(points[0][2] , points[0][0])
    dp[2] = max(points[0][0] , points[0][1])
    dp[3] = max(points[0][0] , points[0][1], points[0][2])
    

    for day in range(1, days):
        temp:List[int] = [0]* 4
        for last in range(0, 4):
            # dp[day][last] = 0

            for task in range(0, 3):

                if task != last:
                    point:int = points[day][task] + dp[task]
                    temp[last] = max(temp[last] , point)
                
        dp = temp
    

    return dp[days - 1]
        


# Test Cases
points = [[2,1,3], [3,4,6], [10,1,6], [8,3,7]]
day = len(points)
last = 3
dp = [[-1 for i in range(4)] for j in range(day)]
print(ninja_training_tabulation_optimized(points))
print(ninja_training_tabulation(points))

        