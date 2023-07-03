"""
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

class Solution(object):
    def longestOnes(self, nums, k):
        maxOne, zero, pointer = 0, 0, 0
        for index, value in enumerate(nums):
            if value == 0: zero += 1
            while zero > k:
                if nums[pointer] == 0: zero -= 1
                pointer += 1
            maxOne = max(maxOne, (index - pointer) + 1)
        return maxOne
