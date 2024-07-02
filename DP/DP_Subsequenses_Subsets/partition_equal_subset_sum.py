"""

So the catch is, 

We have to find one subset with total_sum/2.

if it is present, then we will definitely have a another subset with the equal sum

# RECURSION
--------------------

target will be initialized as sum/2

f(index, target, nums )

# # Base Case

if index == 0:
    return nums[0] == target

if target == 0:
    return True

----------------------------

not_take = f(index-1, target, nums)

target >= nums[index]
    take = f(index-1, target-nums[target], nums)

return not_take or take

"""

# MEMOIZATION
from typing import List

def can_patition(index:int, target:int, nums:List[int], dp:List[List[int]])->bool:

    # Base Cases
    if index == 0:
        return nums[0] == target
    
    if target == 0:
        return True
    

    if dp[index][target] != -1:
        return False
    
    not_take = can_patition(index, target, nums, dp)

    take = False

    if target >= nums[index]:
        take = can_patition(index , target-nums[index], dp)


    return take or not_take


# Tabulation
def can_patition_tabulation(nums:List[int])->bool:

    n = len(nums)
    sum = 0

    for i in range(n):
        sum+= nums[i]

    target = sum/2

    dp = [[0 for _ in range(target+1)]for _ in range(n)]

    # # Base Cases
    for i in range(n):
        dp[i][0] = True

    if target >= nums[0]:
        dp[0][nums[0]] = True

    for i in range(1, n):
        for k in range(1, target+1):

            not_take = dp[i-1][k]
            take = False

            if nums[i] <= target:
                take = dp[i-1][k-nums[i]]

            dp[i][target] = not_take or take

    return dp[n-1][k]


# Tabulation Space Optimization
def can_partition_tabulation_optimized(nums:List[int])->bool:
    n = len(nums)
    to_sum = 0
    to_sum = sum(nums)

    if to_sum % 2 != 0:
        return False

    target = to_sum//2


    prev =[False] * (target+1)

    # # Base Cases
    prev[0] = True

    if target >= nums[0]:
        prev[nums[0]] = True

    for i in range(1, n):
        curr =[False] * (target+1)
        curr[0] = True

        for k in range(1, target+1):

            not_take = prev[k]
            take = False

            if nums[i] <= target:
                take = prev[k-nums[i]]

            curr[k] = not_take or take
        
        prev = curr

    return prev[target]


# Test Cases
if __name__ == '__main__':
    nums = [1,5,11,5]
    n = len(nums)
    target = 0

    # dp = [[-1 for _ in range(target+1)]for _ in range(n)]

    # print(can_patition(n-1, target, nums, dp)) ## True

    # print(can_patition_tabulation(nums)) ## True

    print(can_partition_tabulation_optimized(nums)) ## True

    