#1st pointer -> first element
#2ns pointer -> element after first element
#if pair found then pop at pointer and count pair + 1
#end iteration if 1st pointer at the end of array or array consist of 1 element

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        p1, p2 = 0, len(nums) - 1
        countPair = 0
        while p2 > p1:
            pair = nums[p1] + nums[p2]
            if pair < k:
                p1 += 1
            elif pair > k:
                p2 -= 1
            else:
                countPair += 1
                p1 += 1
                p2 -= 1
        return countPair
