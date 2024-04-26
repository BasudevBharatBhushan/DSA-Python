"""
A reverse pair is a pair (i, j) where:

0 <= i < j < nums.length and
nums[i] > 2 * nums[j].

"""
# Appproach 1 | Brute Force
# TC - O(n^2), SC - O(1)
from typing import List

def reversePairs(nums:List[int])->int:

    reverse_pairs = 0
    n = len(nums)

    for i in range(n):
        for j in range(i+1,n):
            if nums[i] > 2 * nums[j]:
                reverse_pairs += 1


    return reverse_pairs


# Test Cases
nums = [2,4,3,5,1]
# print(reversePairs(nums)) # 2

# Approach 2 | Merge Sort
"""
For instance below are the two sorted arrays of two half

[6, 13, 21, 25] and [1, 2, 3, 4, 4, 5, 9 , 11, 13]

Now, 

6 -> [1, 2]  (6 can form pair with 1 and 2)
13 -> [1, 2, 3, 4, 4, 5] = pair of 6 + [ 3, 4, 4, 5]
21 -> [1, 2, 3, 4, 4, 5, 9 ] = pair of 13 + [9]
25 -> [1, 2, 3, 4, 4, 5, 9 , 11] = pair of 21 + [11]

----------
We will be using this analogy to solve our problem, lets see how it will look in iteration

itr 1:  [6]  -------------- 

6 will form pair with 1, 2   --> pair_count = 2

itr 2: [13]  --------------

Now I will start from 3, since 13 will definitely form pair with pairs of 6

13 will form pair with 3, 4, 4, 5 --> pair_count = 4

Total Pairs of 13 = pair of 6 + 4 => 2 + 4 = 6

itr 3: [21]  -------------

Will start from 9, since 21 will definitely form pair with pairs of 13

21 will form pair with 9 --> pair_count = 1

Total Pairs of 21 = pair of 13 + 1 => 6 + 1 = 7

itr 4: [25]  ---------------

Will start from 11, since 25 will definitely form pair with pairs of 21

25 will form pair with 11 --> pair_count = 1

Total Pairs of 25 = pair of 21 + 1 => 7 + 1 = 8

------------------------------

Answer will be

pair of 6 + pair of 13 + pair of 21 + pair of 25 = 2 + 6 + 7 + 8 = 23

so this logic we will be implementing with the Merge sort to find the reverse pairs

"""

# Merging Function

def merge(arr:List[int], low:int, mid:int, high:int):
    temp = []

    left = low
    right = mid+1


    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left +=1
        else:
            temp.append(arr[right])
            right +=1

        
    # if elements on the left half are still left to be put on the merged array
    while left <= mid:
        temp.append(arr[left])
        left +=1

    
    # if elements on the right half are still left to be put on the merged array
    while right <= high:
        temp.append(arr[right])
        right +=1


    # Copying the elements from temp to original array

    for i in range(low, high+1):
        arr[i] = temp[i-low]

    

def count_pair(arr:List[int], low:int, mid:int, high:int):
    right = mid + 1
    pair_count = 0

    for i in range (low, mid+1):
        while right <= high and arr[i]> 2 * arr[right]:
            right +=1
        
        pair_count += right - (mid+1)


    return pair_count
    

def reveres_paris_merge_sort(arr:List[int], low:int, high:int)->int:
    if low>=high:
        return 0
    
    pair_count = 0
    mid = (low + high) // 2

    pair_count += reveres_paris_merge_sort(arr, low, mid) # Left Half
    pair_count += reveres_paris_merge_sort(arr, mid+1, high) # Right Half

    pair_count += count_pair(arr, low, mid, high) 

    merge(arr, low, mid, high)

    return pair_count
    

def reversePairs_merge_sort(nums:List[int])->int:
    return reveres_paris_merge_sort(nums, 0, len(nums)-1)




# Test Cases
nums = [1,3,2,3,1]  

print(reversePairs_merge_sort(nums)) # 3