# 443. String Compression

Difficulty : `Medium`

Given an array of characters `chars`, compress it using the following algorithm:

Begin with an empty string `s`. For each group of **consecutive repeating characters** in `chars`:

- If the group's length is `1`, append the character to `s`.
- Otherwise, append the character followed by the group's length.

The compressed string `s` **should not be returned separately**, but instead, be stored **in the input character array** `chars`. Note that group lengths that are `10` or longer will be split into multiple characters in `chars`.

After you are done **modifying the input array**, return *the new length of the array*.

You must write an algorithm that uses only constant extra space.
 

Example 1:

> Input: chars = ["a","a","b","b","c","c","c"]\
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Example 2:

> Input: chars = ["a"]\
Output: Return 1, and the first character of the input array should be: ["a"]

Example 3:

> Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
 

Constraints:

>- 1 <= chars.length <= 2000
>- chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.


## Solution

### Go

```Go
func compress(chars []byte) int {
    count, index := 1, 0
    for i := 1; i <= len(chars); i++ {
        if i < len(chars) && chars[i] == chars[i - 1] {
            count++
            continue
        }

        chars[index] = chars[i - 1]
        index++
        if count > 1 {
            for _, num := range strconv.Itoa(count) {
                chars[index] = byte(num)
                index++
            }
        }
        count = 1
    }

    return index
}
```

### Python

```Python
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        result = []
        count = 1
        for i in range(1,len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                result.append([chars[i-1],count])
                count = 1
        result.append([chars[-1], count])
        i = 0
        for char, count in result:
            chars[i] = char
            i += 1
            if count > 1:
                for item in str(count):
                    chars[i] = str(item)
                    i += 1
        return i
```