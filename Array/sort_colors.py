# Sort Arrays of 1s , 0s and 2s

class Solution(object):
    def sortColors(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(arr)
        i = 0
        zero_position = 0
        one_position = 0
        two_position = n-1

        while one_position <= two_position:

            if arr[one_position] == 0:
                arr[one_position], arr[zero_position] = arr[zero_position], arr[one_position]
                one_position+=1
                zero_position += 1

            elif arr[i] == 1:
               one_position += 1
            

            else:
                arr[one_position], arr[two_position] = arr[two_position], arr[one_position]
                two_position -= 1