# 345. Reverse Vowels of a String

Difficulty : `Easy`

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

 

Example 1:

> Input: s = "hello"\
Output: "holle"

Example 2:

> Input: s = "leetcode"\
Output: "leotcede"
 

Constraints:

>- 1 <= s.length <= 3 * 105
>- s consist of printable ASCII characters.


## Solution

### Go

```Go
func isVowel(c rune) bool {
    vowel := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for _, v := range vowel {
        if c == v {
            return true
        }
    }
    return false
}

func reverseVowels(s string) string {
    l, r := 0, len(s)-1
    runes := make([]rune, len(s))
    for idx, r := range s {
        runes[idx] = r
    }

    for l < r {
        if !isVowel(runes[r]) {
            r--
            continue
        }

        if !isVowel(runes[l]) {
            l++
            continue
        }

        runes[l], runes[r] = runes[r], runes[l]
        l++
        r--
    }

    return string(runes)
}
```

### Python

```Python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a","i","u","e","o","A","I","U","E","O"]
        s_list = list(s)
        pointL, pointR = 0, len(s_list) - 1
        while pointL < pointR:
            if s_list[pointL] not in vowels:
                pointL += 1
                continue

            if s_list[pointR] not in vowels:
                pointR -= 1
                continue

            s_list[pointL], s_list[pointR] = s_list[pointR], s_list[pointL]
            pointL += 1
            pointR -= 1

        return "".join(s_list)
```

In this code, we will copy the string s into runes array, and check every element if it is vowel or not, if both of them is a vowel then we switch the position, the main idea here is using two-pointer method to iterate through the word given.