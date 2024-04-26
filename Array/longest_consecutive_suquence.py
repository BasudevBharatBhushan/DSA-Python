from typing import List


# Better Approach | This approach is not working because it is exceeding the time limit for some test cases

def longest_consecutive_sequence(nums:List[int])->int:
    n = len(nums)

    nums.sort()

    longest_streak = 0


    for i in range(n):

        temp_longest_streak = 1

        

        while i+1 < n:        
            # Skip the duplicates
            if nums[i+1] == nums[i]:
                i+=1
                continue

            elif nums[i+1] - nums[i] == 1:
                i+=1
                temp_longest_streak += 1

            else:
                break
     
        longest_streak = max(longest_streak, temp_longest_streak)


    return longest_streak


# Dry Run

"""
nums = [1,2,0,1]

sorted_nums = [0,1,1,2]



"""

# Better approach using Sort | TC - O(NlogN) + O(N) | SC - O(1)

def longest_consecutive_sequence_sort(nums:List[int])->int:
    n = len(nums)
    if n == 0:
        return 0
    

    nums.sort()

    last_smaller = float('-inf') # To keep track of the last smaller element
    temp_streak = 0
    longest_streak = 1

    for i in range(n):
        if nums[i] - 1 == last_smaller:
            temp_streak +=1
            last_smaller = nums[i]
        elif nums[i] != last_smaller:
            temp_streak = 1
            last_smaller = nums[i]

        longest_streak = max(longest_streak, temp_streak)

    return longest_streak







# Brute Force Approach 2 n| TC  O(N^2)
def longest_consecutive_sequence_bruteforce(nums:List[int])->int:
    n = len(nums)

    longest_streak = 0

    for i in range(n):
        current_num = nums[i]
        current_streak = 1

        while linearSearch(nums, current_num+1):
            current_num +=1
            current_streak +=1

        
        longest_streak = max(longest_streak, current_streak)
    
    return longest_streak




def linearSearch(nums:List[int], target:int)->bool:
    n = len(nums)
    for i in range(n):
        if nums[i]==target:
            return True
    return False



# Test Cases
# nums = [100, 4, 200, 1, 3, 2]
nums = [1,2,0,1]
print(longest_consecutive_sequence(nums)) # 4



# Oprimal Approach | Using Set Data Structure | TC - O(2*N) | Though we are using nested loops, the set will be traversed at most twice in the worst csae
# SC - O(N)

def longest_consecutive_sequence_optimal(nums:List[int])->int:
    n = len(nums)
    if n == 0:
        return 0
    

    longest_streak = 1
    temp_longest_streak = 0

    st = set(nums)


    for i in st:

        # We will only start the sequence from the smallest number
        if i-1 not in st:
            temp_longest_streak = 1

            x = i

            while x+1 in st:
                x +=1
                temp_longest_streak +=1
            
            longest_streak = max(longest_streak, temp_longest_streak)
    
    return longest_streak

