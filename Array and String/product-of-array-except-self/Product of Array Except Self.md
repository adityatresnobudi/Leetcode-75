# 238. Product of Array Except Self

Difficulty : `Medium`

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

 

Example 1:

> Input: nums = [1,2,3,4]\
Output: [24,12,8,6]

Example 2:

> Input: nums = [-1,1,0,-3,3]\
Output: [0,0,9,0,0]
 

Constraints:

>- 2 <= nums.length <= 105
>- -30 <= nums[i] <= 30
>- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


## Solution

### Go

```Go
// iterate forward using prefix and backward using postfix
// first iteration -> res = 1, 1, 2*1 , 3*2*1
// second iteration -> res = 2*3*4, 1*3*4, 2*1*4, 3*2*1*1

func productExceptSelf(nums []int) []int {
    res := make([]int, len(nums))

    prefix := 1
    for idx, num := range nums {
        res[idx] = prefix
        prefix *= num
    }

    postfix := 1
    for i := len(nums)-1; i >= 0; i-- {
        res[i] *= postfix
        postfix *= nums[i]
    }
    return res
}
```

### Python

```Python
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
```