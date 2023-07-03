class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        validDel = 1
        pointerL = 0
        
        for pointerR in range(len(nums)):
            if nums[pointerR] == 0:
                validDel -= 1
            
            while validDel < 0 and pointerL <= pointerR:
                if nums[pointerL] == 0:
                    validDel += 1
                pointerL += 1
            
            res = max(res, pointerR - pointerL)
            
        return res
