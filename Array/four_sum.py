# Optimal Approach [4 pointer approach]
# TC - O(n^3), SC - O(no of unique quadruplets)

from typing import List

def fourSum(nums:List[int], target:int)->List[List[int]]:

    n = len(nums)

    nums.sort()

    ans = []


    for i in range(n):
        
        # Avoid the duplicates while moving i
        if i > 0 and nums[i]==nums[i-1]:
            continue

        for j in range(i+1, n):

            # Avoid the duplicates while moving j  [ j > i+1 to exclude the conditiion for the first element]
            if j > i+1 and nums[j] == nums[j-1]:
                continue

            k = j + 1
            l = n-1

            while k<l:
                current_sum = nums[i] + nums[j] + nums[k] + nums[l]

                if current_sum == target:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])

                    k += 1
                    l -= 1

                    # Skip the duplicates
                    while k<l and nums[k] == nums[k-1]:
                        k += 1

                    while k<l and nums[l] == nums[l+1]:
                        l -=1

                elif current_sum < target:
                    k += 1

                else:
                    l -= 1

    return ans
    
# Test Cases
nums = [1, 0, -1, 0, -2, 2]
target = 0

print(fourSum(nums, target)) # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]