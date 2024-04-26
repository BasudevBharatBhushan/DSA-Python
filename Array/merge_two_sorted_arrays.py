# Merge two sorted arrays
from typing import List


# TC - O(n+m) + O(n+m)
# Brute Force Approach
# def merge(arr1, arr2, n, m):
#     arr3 = [0] * (n+m)

#     left = 0
#     right = 0
#     index = 0

#     while left< n and right < m:
#         if arr1[left] <=  arr2[right]:
#             arr3[index] = arr1[left]
#             left += 1
#             index +=1
#         else:
#             arr3[index] = arr2[right]
#             right +=1
#             index +=1

    
#     while left < n:
#         arr3[index] = arr1[left]
#         left +=1
#         index +=1

#     while right < m:
#         arr3[index] = arr2[right]
#         right +=1
#         index +=1

#     for i in range(n + m):
#         if i < n:
#             arr1[i] = arr3[i]
#         else:
#             arr2[i - n] = arr3[i]

    
    # Optimal Approach (Two pointer approach)

"""
    arr1 = [1, 3, 5, 7]  , arr2 = [0, 2, 6, 8, 9]

    1. letf = 7, right = 0, left > right, swap

    [1,3,5,0]  [7,2,6,8,9]

    2. left = 5, right = 2, left > right, swap
    
        [1,3,2,0]  [7,5,6,8,9]

    3. left = 3, right = 6, left < right, no swap

    break here and sort the two arrays individually
    

"""

    # TC - O(min(n,m)) + O(nlogn) + O(mlogm) becoz the count of smallest array will be the max no of comparasion done
    # SC - O(1)
def merge_optimal1(arr1, arr2, n, m):

    left = n-1
    right = 0


    while left >=0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left],arr2[right] = arr2[right],arr1[left]
            left -=1
            right +=1
        else:
            break

        
    arr1.sort()
    arr2.sort()

    print(arr1)
    print(arr2)

    for i in range(m):
        #arr1[n-i] = arr2[i]
        arr1.append(arr2[i])

    i = 0
    while i < len(arr1):
        if arr1[i]==0:
            
            del arr1[i]
        else:
            i+=1



# Optimal - 2
"""
Shell Sort, Gap Method

[1, 3, 5, 7]  [0, 2, 6, 8, 9]

gap = n+m/2 = 4+5/2 = 4.5 = 5

left = 1, right = 2, left < right, no swap

after right go out of the array, 

gap = gap/2 = 5/2 = 2.5 = 3

left = 1, right = 7

continue until the gap is 1

"""
# TC - O((n+m)*log(n+m)), SC - O(1)
# def swapIfGreater(arr1, arr2, i, j):
#     if arr1[i] > arr2[j]:
#         arr1[i],arr2[j] = arr2[j],arr1[i]

# def merge_optimal2(arr1, arr2, n, m):

#     len = n+m
#     gap = (len//2) + (len%2)

#     while gap > 0:

#         left = 0
#         right = left + gap

#         while right<len:

#             # left pointer in arr1 and right pointer in arr2
#             if left < n and right >=n:
#                 swapIfGreater(arr1,arr2,left,right-n)
            
#             # both pointers in arr2[]
#             elif left >=n:
#                 swapIfGreater(arr2,arr2,left-n,right-n)
            
#             else:
#                 swapIfGreater(arr1,arr1,left,right)

#             left +=1
#             right +=1

#             if gap ==1:
#                 break

#             gap = (gap//2) + (gap%2)


arr1 = [0,0,0,1,2,3]
arr2 = [2,5,6]

n = len(arr1)
m = len(arr2)
merge_optimal1(arr1, arr2, n, m)
print(arr1)