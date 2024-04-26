"""
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

indexes

[0,0], [0,1]     1, 3
[1,0], [1,1]     2, 6
[2,0], [2,1]  =  8, 10
[3,0], [3,1]     15,18


dry run

start - 1, end - 3

then it will compare if

2 <= 3 (i.e end)
...

and so on
"""


"""
Approach:

I will assume that these are already present in sorted order

compare:

y of 1st > x of 2nd
[x1, y2]



"""
# BRUTE FORCE APPROACH | TC - O(NlogN) + O(N*2)
"""
we are using 2 loops i and j. But while using loop i, we skip all the intervals that are merged with loop j.
so we can conclude that every interval is rougly visited twice [once for checking or skipping and once for merging]

so the time complexity of loop is 2*N insted of N*N

Space Complexity - O(N)

"""
from typing import List
def merge(intervals: List[List[int]])-> List[List[int]]:

    merged = []

    n = len(intervals)

    intervals.sort()


    for i in range(n):

        start, end = intervals[i][0], intervals[i][1]


        if merged and end <= merged[-1][1]:
            continue


        for j in range(i+1, n):
            if intervals[j][0] <= end:
                end = max(end, intervals[j][1])
            else:
                break
        
        merged.append([start, end])

        return merged



# Optimal Approach, Using a single loop | TC - O (nlogn) + o(n) , SC - O(n)

def merge_ii(intervals: List[List[int]])->List[List[int]]:
    n = len(intervals)

    intervals.sort()

    merged = []

    for i in range(n):

        if not merged or intervals[i][0] > merged[-1][1]:
            merged.append(intervals[i])

        else:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
    
    return merged


"""
DRY RUN - 
[0,0], [0,1]     1, 3
[1,0], [1,1]     2, 6
[2,0], [2,1]  =  8, 10
[3,0], [3,1]     15,18


i = 0 , 

if merged is empty or
intervals[0][0] > merged[-1][1] (which is empty)

merged - [[1,3]]

i = 1

intervals[1][0] > merged[-1][1] -> 2 > 3 ? No

else

merged[-1][1] = max(3, 6) = 6... and so on...



"""
