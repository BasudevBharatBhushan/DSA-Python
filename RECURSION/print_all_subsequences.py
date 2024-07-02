"""


"""
from typing import List

def print_subsequences(ind:int, n:int, nums:List[int], dp:List[int], subsequences:List[List[int]]):
    if ind>=n:
        # print(dp)
        # Store the dp in the subsequences
        subsequences.append(dp[:])
        return
    
    dp.append(nums[ind])

    print_subsequences(ind+1, n, nums, dp, subsequences)  ## Take

    dp.pop()

    print_subsequences(ind+1, n, nums, dp, subsequences)  ## Not Take



def main():
    nums:List[int] = [3,1,2]
    n:int = len(nums)
    dp:List[int] = []
    subsequences: List[List[int]] = []
    print_subsequences(0, n, nums, dp, subsequences)
    print(subsequences)

if __name__ == '__main__':
    main()
