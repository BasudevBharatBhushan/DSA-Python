def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    n = len(nums)

    adj = []* n

    bit_adj = 0
        
    for i in range(1,n):
        print(i)
        bit_adj ^= i

        
    for i in range(n):
        bit_adj ^= nums[i]
        
    print(bit_adj)

    return bit_adj


# Test Cases
nums = [1,3,4,2,2]
findDuplicate(nums)