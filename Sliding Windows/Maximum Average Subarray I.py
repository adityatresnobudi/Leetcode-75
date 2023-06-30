#sliding windows consist of k elements
#compare new avg with old average, take max

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        winL, winR = 0, k
        max_jml = jml = float(sum(nums[:winR]))
        while winR < len(nums):
            jml += nums[winR] - nums[winL]
            max_jml = max(jml, max_jml)
            winL += 1
            winR += 1
        return max_jml / k
