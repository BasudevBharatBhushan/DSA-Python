# Element that appears more than n/2 times in an array

# Approach 1, Using Hash Map

from collections import Counter
from typing import List

arr = [2, 2, 1, 1, 1, 2, 2]

n = len(arr)

counter = Counter(arr)

print(counter)  




def majorityElement(arr):
    n = len(arr)

    counter = Counter(arr)

    for num,count in counter.items():
        print(num, count)
        if count > n//2:
            return num
        
    return -1



print(majorityElement(arr)) # 2



# Optimal Approach
# Boyer Moore Voting Algorithm

def majorityElement_optimal(arr:List[int])->int:
    count = 0
    element = 0

    for num in arr:
        if count == 0:
            element = num
            count = 1
        elif element == num:
            count +=1
        else:
            count -=1

    
    return element


print(majorityElement_optimal(arr)) # 2