# 1768. Merge Strings Alternately

Difficulty : `Easy`

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

> Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Example 2:

> Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"

Example 3:

> Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
 

Constraints:

>- 1 <= word1.length, word2.length <= 100
>- word1 and word2 consist of lowercase English letters.


## Solution

### Go

```Go
func mergeAlternately(word1 string, word2 string) string {
    res := ""
    if len(word1) >= len(word2) {
        for i := 0; i < len(word2); i++ {
            res += string(word1[i])
            res += string(word2[i])
        }
        res += word1[len(word2):len(word1)]
        return res
    }
    for i := 0; i < len(word1); i++ {
        res += string(word1[i])
        res += string(word2[i])
    }
    res += word2[len(word1):len(word2)]
    return res
}
```

### Python

```Python
#merge => empty array for final merging string
#len(word1) > len(word2)
#word1[:len(word2)] , word1[len(word2):]
#new array -> filled in using iteration
#every iteration will be adding letter from word1(short) and word2 simultaneously
#after iteration, appending the rest of the letter from word1 that has not appended yet

#vice versa

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        if len(word1) > len(word2):
            word1_a = word1[:len(word2)]
            word1_b = word1[len(word2):]
            
            for i in range(len(word2)):
                merged.append(word1_a[i])
                merged.append(word2[i])
            merged = merged + [word1_b]
        
        elif len(word1) < len(word2):
            word2_a = word2[:len(word1)]
            word2_b = word2[len(word1):]
            
            for i in range(len(word1)):
                merged.append(word1[i])
                merged.append(word2_a[i])
            merged = merged + [word2_b]
        
        else: #len(word1) == len(word2)
            for i in range(len(word1)):
                merged.append(word1[i])
                merged.append(word2[i])
        return "".join(merged)
```