"""

eg. 1, 2, 3, 4

[1, 2] , [3, 4] = |7-3| = 4

[1, 3] , [2, 4] = |4-6| = 2

[1, 4] , [2, 3] = |5-5| = 0  --> min abs difference from the sum of two subsets


Tabulation approach in subset sum problem if n = 5 and target = 7

   0  1  2  3  4  5  6  7
0 [T, T, F, F, F, F, F, F]
1 [T, F, F, F, F, F, F, F]
2 [T, F, F, F, F, F, F, F]
3 [T, F, F, F, F, F, F, F]
4 [T, *, *, *, *, *, *, T]

So what did it signified.

dp [4][7] = ?

For array of n = 4, is subset sum of 7 possible?

similarly

dp [4][6] = ?
for array of n = 4, is subset sum of 6 possible?

dp [4][5] = ?
for array of n = 4, is subset sum of 5 possible?

dp [3][5] = ?
for array of n = 3, is subset sum of 5 possible?


Similarly, for arr = [3, 2, 7]

sum = 12 

we can find out what partions are possible

0   1   2   3   4   5   6   7   8   9   10  11  12
✅ ❌  ✅ ✅ ❌  ✅  ❌ ✅  ❌ ✅  ✅ ❌  ✅

so possibles s1 are 0, 2, 3, 5, 7 ,9, 10, 12
corresponding s2 are 12, 10, 9, 7, 5, 3, 2, 0

so all the abs diffs are

|0-12| = 12 , |2-10| = 8, |3-9| = 6, |5-7| = 2, |7-5| = 2, |9-3| = 6, |10-2| = 8, |12-0| = 12

so min abs diff is 2

"""
from typing import List
def subset_sum(nums:List[int])->List[int]:

    target = sum(nums)
    n = len(nums)

    dp = [[False for _ in range(target+1)] for _ in range (n)]

    # # Base Cases
    # for ever 0...n-1, if target = 0, then dp[i][0] = True

    for i in range(0, n):
        dp[i][0] = True

    # # Base Case 2

    if target >= nums[0]:
        dp[0][nums[0]] = True


    for i in range(1, n):
        for k in range(1, target+1):

            not_take = dp[i-1][k]

            take = False
            if k >= nums[i]:
                take = dp[i-1][k-nums[i]]

            dp[i][k] = take or not_take

    

    return dp[n-1]


def min_difference(nums:List)->int:

    n = len(nums)

    to_sum = sum(nums)

    mini = int(1e9)

    dp = subset_sum(nums)
    print(dp)

    for i in range(0, to_sum+1):
        if dp[i] == True:
            mini = min(mini, abs(i - (to_sum-i)))
            # print(i, "indexs")
            # print( abs(i - (i-to_sum)))
        
    
    return mini


if __name__ == '__main__':
    # nums:List[int] = [3, 2, 7]
    # nums:List[int] = [3, 9, 7,3]
    nums:List[int] = [-36,36]

    print(min_difference(nums))
    