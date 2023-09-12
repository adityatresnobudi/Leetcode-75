# 605. Can Place Flowers

Difficulty : `Easy`

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, return `true` if `n` new flowers can be planted in the `flowerbed` without violating the no-adjacent-flowers rule and `false` otherwise.

 

Example 1:

> Input: flowerbed = [1,0,0,0,1], n = 1\
Output: true

Example 2:

> Input: flowerbed = [1,0,0,0,1], n = 2\
Output: false
 

Constraints:

>- 1 <= flowerbed.length <= 2 * 104
>- flowerbed[i] is 0 or 1.
>- There are no two adjacent flowers in flowerbed.
>- 0 <= n <= flowerbed.length


## Solution

The function canPlaceFlowers will take array of integers flowerbed and n as the number of flowers we have as an arguments, the function will return true if we can successfully put in all flowers and return false otherwise.

### Go

```Go
func canPlaceFlowers(flowerbed []int, n int) bool {
    length := len(flowerbed)

    for idx, flower := range flowerbed {
        if length == 1 {
            if flower == 0 {
                flower = 1
                n--
                continue
            }
            break
        }
        
        switch idx {
        case 0:
            if flowerbed[idx+1] == 0 && flowerbed[idx] == 0 {
                flowerbed[idx] = 1
                n--
            }
        case length-1:
            if flowerbed[idx-1] == 0 && flowerbed[idx] == 0 {
                flowerbed[idx] = 1
                n--
            }
        default:
            if flowerbed[idx-1] == 0 && flowerbed[idx+1] == 0 && flowerbed[idx] == 0 {
                flowerbed[idx] = 1
                n--
            }
        }
    }

    return n <= 0
}
```

In this code, we will take the length of the flowerbed and store it in length variable, and then we iterate through flowerbed, if we have a flowerbed with only one space in it, then we check if there is a flower or not, if there are more than one, then check if the space available has flower planted adjacent to it, for every flower we successfully put, we subtract the number of total flower.

### Python

```Python
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        f = [0] + flowerbed + [0]

        for i in range (1, len(f) - 1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0
```

In this code, we will append the flowerbed array with 0 in the front and at the back, and then we iterate through flowerbed from after the front 0 until the last number before the last 0, every iteration we check the adjacent space if there is a flower planted, if not then we place the flower and subtract the number of total flower.