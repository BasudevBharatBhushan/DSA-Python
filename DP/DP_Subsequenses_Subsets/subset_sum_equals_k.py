"""
In the entire array, till the index n-1, does there exist a target
f(n-1, target)

# # RECURSION
f(index, target)

# # # Base Case
if target == 0: return 0

if index == 0: return a[0]==target

-------------------

 # # # I will not take the selected index  [so nothing will be subtracted from the target]
 bool not_take = f(index-1, target) 

 # # # I will take the selected index
 bool take = false

 if target >= a[index]:
    take = f(index-1, target-a[index])


return take or not_take

TC - O(2*n)



"""
from typing import List

# Memoization  | TC 
def subset_sum(index:int, target:int, nums:List[int], dp:List[List[int]])->bool:
    # Base Cases
    if target == 0:
        return True
    
    if index == 0:
        return nums[0]==target
    
    if dp[index][target] != -1:
        return dp[index][target]
    
    not_take:bool = subset_sum(index-1, target, nums, dp)

    take:bool = False

    if(target >= nums[index]):
        take = subset_sum(index-1, target-nums[index], nums , dp)

    
    dp[index][target] = take or not_take

    return dp[index][target]


def subset_sum_count(index:int, target:int, nums:List[int], dp:List[List[int]])->int:
    # Base Cases
    if target == 0:
        return 1
    
    if index == 0:
        return 1 if nums[0] == target else 0

    
    if dp[index][target] != -1:
        return dp[index][target]
    
    not_take:int = subset_sum_count(index-1, target, nums, dp)

    take:int = 0

    if(target >= nums[index]):
        take = subset_sum_count(index-1, target-nums[index], nums, dp)

    dp[index][target] =  take + not_take


    return dp[index][target]

# TABULATION
def subset_sum_tabulation(nums:List[int], k:int)->int:
    n:int = len(nums)
    dp = [[0 for _ in range(k+1)]for _ in range (n)]


    """
    1st base case
    Just look into the recursion first base case
    if target == 0:
        return True

    we can say, for target == 0, any row value can be possible, 0, 1...n-1

    so every dp[i][0] will be stored as True, 
    in case of count it will be dp[i][0] = 1


    2nd base case
    if index == 0:
        return nums[0]==target


    possibility:
    dp[0][nums[0]] = true


    """

    for i in range(n):
        dp[i][0] = 1

    if k >= nums[0]:
        dp[0][nums[0]]= 1


    
    for i in range(1,n):
        for target in range(1, k+1):

            not_take = dp[i-1][target]

            take = 0
            if nums[i] <= target:
                take = dp[i-1][target-nums[i]]
            
            dp[i][target] = not_take + take

    
    return dp[n-1][k]


# TABULATION |SPACE OPTMIZATION
def subset_sum_tabulation_optmized(nums:List[int], k:int)->int:
    n:int = len(nums)
    

    prev = [0]*(k+1)


    prev[0] = 1

    if k >= nums[0]:
        prev[nums[0]]= 1


    
    for i in range(1,n):

        curr = [0]*(k+1)
        
        curr[0]  = 1

        for target in range(1, k+1):

            not_take = prev[target]

            take = 0
            if nums[i] <= target:
                take = prev[target-nums[i]]
            
            curr[target] = not_take + take
        
        prev = curr

    
    return prev[k]
    




if __name__ == '__main__':

    nums = [1,5,11,5]
    # nums =[3,5,6,7]
    n = len(nums)
    k = 11
    dp = [[-1 for _ in range(k+1)]for _ in range(n)]

    # print(subset_sum(n-1, k , nums,dp ))
    print(subset_sum_count(n-1, k , nums,dp ))
    print(subset_sum_tabulation(nums, k ))
    print(subset_sum_tabulation_optmized(nums, k ))



    


    

