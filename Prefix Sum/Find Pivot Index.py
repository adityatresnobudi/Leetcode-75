#left_sum = 0
#right_sum = sum(array) - (left_sum + pivot)
#iterate until find left_sum = right_sum
#if not found then -1

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum = 0

        for i in range (len(nums)):
            right_sum = sum(nums) - left_sum - nums[i] 
            if left_sum == right_sum:
                return i
            else:
                left_sum += + nums[i]
        return -1
