# 334. Increasing Triplet Subsequence


Difficulty : `Medium`

Given an integer array `nums`, return `true` if there exists a triple of indices `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`. If no such indices exists, return `false`.

 

Example 1:

> Input: nums = [1,2,3,4,5]\
Output: true\
Explanation: Any triplet where i < j < k is valid.

Example 2:

> Input: nums = [5,4,3,2,1]\
Output: false\
Explanation: No triplet exists.

Example 3:

> Input: nums = [2,1,5,0,4,6]\
Output: true\
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

>- 1 <= nums.length <= 5 * 105
>- -231 <= nums[i] <= 231 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

## Solution

### Go

```Go
func increasingTriplet(nums []int) bool {
    first, second := math.MaxInt, math.MaxInt
    for _, num := range nums {
        if num <= first {
            first = num
        } else if num <= second {
            second = num
        } else {
            return true
        }
    }
    return false
```

### Python

```Python
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
```

The main idea behind this code logic is we only have to check if triplets exist or not in the `nums` array, that's why we start with two variable math(inf) for `first` and `second`. After that, we iterate `nums` array using for loop, and if we find the number at the index is lower than first then change first to number at that index and continue, and if the number after that is also lower than second (already higher than first) then change first to number at that index and continue, and else (for third number) we return true without checking anything because if we reach the last condition it means that there is always a triplet inside `nums` else `false`.