"""
LEETCODE 1498. Number of Subsequences That Satisfy the Given Sum Condition

You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.


"""

from typing import List


## causing TLE
def print_subsequences(ind:int, n:int, nums:List[int],target:int, dp:List[int] )->int:
    if ind>=n:
        
        if dp:
            if dp[0] + dp[len(dp)-1] <= target:
                return 1
            return 
        return 0
    
    dp.append(nums[ind])

    take = print_subsequences(ind+1, n, nums,target, dp)  ## Take

    dp.pop()

    not_take = print_subsequences(ind+1, n, nums,target, dp)  ## Not Take

    return take+not_take


##Otimalaroach

from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        mod = 10**9 + 7
        result = 0
        
        # Pre-compute powers of 2 up to n
        powers = [1] * n
        for i in range(1, n):
            powers[i] = (powers[i - 1] * 2) % mod

        left, right = 0, n - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                result += powers[right - left]
                result %= mod
                left += 1
            else:
                right -= 1
        
        return result
    

    """
    EXLANATION

    Consider the array nums = [3, 5, 6] and target = 8.

Sort the Array: First, we sort the array: nums = [3, 5, 6].

Initialize Two Pointers: We start with left = 0 and right = 2 (pointing to the first and last elements).

Precompute Powers of 2:

For a list of length n, we precompute the powers of 2 up to n because each element in any subsequence can either be included or excluded.
powers = [1, 2, 4]
powers[0] = 2^0 = 1
powers[1] = 2^1 = 2
powers[2] = 2^2 = 4
Using Two-Pointer Technique
We use the two-pointer technique to find valid subsequences whose sum is less than or equal to the target:

Step-by-Step Process:
First Iteration:

left = 0, right = 2
Check if nums[left] + nums[right] (3 + 6 = 9) is less than or equal to the target (8). It’s not, so we move the right pointer to the left.
New right = 1
Second Iteration:

left = 0, right = 1
Check if nums[left] + nums[right] (3 + 5 = 8) is less than or equal to the target (8). It is, so:
All subsequences starting with nums[left] and ending at any element between left and right are valid.
There are 2^(right - left) such subsequences. Here, right - left = 1 - 0 = 1, so there are 2^1 = 2 subsequences: [3], [3, 5].
Add powers[1] (which is 2) to the result.
Move the left pointer to the right.
New left = 1
Third Iteration:

left = 1, right = 1
Check if nums[left] + nums[right] (5 + 5 = 10) is less than or equal to the target (8). It’s not, so we move the right pointer to the left.
New right = 0
Since left is now greater than right, we stop.
    """

# # Test case
# nums = [7, 10, 7, 3, 7, 5, 4]
# target = 12
# solution = Solution()
# print(solution.numSubseq(nums, target))  # Output should be 56


def main():
    nums:List[int] = [3,5,6,7]
    n:int = len(nums)
    nums.sort()
    dp:List[int] = []
    target:int = 9
    print(print_subsequences(0, n, nums, target, dp))
 

if __name__ == '__main__':
    main()