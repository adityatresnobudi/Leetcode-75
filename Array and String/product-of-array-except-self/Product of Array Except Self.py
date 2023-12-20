#nums -> | 1 | 2 | 3 | 4 |
#prefix -> | 1 | 2 | 6 | 24 |
#postfix -> | 24 | 24 | 12 | 4 |
#output -> | 24 | 12 | 8 | 6 |

import numpy as np
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output
