# 1431. Kids With the Greatest Number of Candy

Difficulty : `Easy`

There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `i^th` kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return a boolean array `result` of length `n`, where `result[i]` is `true` if, after giving the `i^th` kid all the `extraCandies`, they will have the **greatest** number of candies among all the kids, or `false` otherwise.

Note that **multiple** kids can have the **greatest** number of candies.

 

Example 1:

> Input: candies = [2,3,5,1,3], extraCandies = 3\
Output: [true,true,true,false,true]

Example 2:

> Input: candies = [4,2,1,1,2], extraCandies = 1\
Output: [true,false,false,false,false]
 

Constraints:

>- n == candies.length
>- 2 <= n <= 100
>- 1 <= candies[i] <= 100
>- 1 <= extraCandies <= 50


## Solution

### Go

```Go
func maxCandies(candies []int) int {
    max := 0
    for _, v := range candies {
        if max < v {
            v = max
        }
    }
    return max
}

func kidsWithCandies(candies []int, extraCandies int) []bool {
    condition := make([]bool, len(candies))
    for i := 0; i < len(candies); i++ {
        if candies[i] + extraCandies >= maxCandies(candies) {
            condition[i] = true
            continue
        }
        condition[i] = false
    }
    
    return condition
}
```

### Python

```Python
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        for kid in candies:
            if max(candies) <= kid + extraCandies:
                result.append(True)
            else:
                result.append(False)
        return result
```

In this code, we will find the maximum number of candies in the candies array, and then iterate through the candies array, in every element of array we try to add extraCandies to the element and check if it will be greater than maximum number of candies, if true then append true in the condition/result index, if false otherwise.