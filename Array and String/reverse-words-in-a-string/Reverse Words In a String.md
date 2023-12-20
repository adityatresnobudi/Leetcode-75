# 151. Reverse Words in a String

Difficulty : `Medium`

Given an input string `s`, reverse the order of the **words**.

A **word** is defined as a sequence of non-space characters. The **words** in `s` will be separated by at least one space.

Return *a string of the words in reverse order concatenated by a single space*.

**Note** that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

> Input: s = "the sky is blue"\
Output: "blue is sky the"

Example 2:

> Input: s = "  hello world  "\
Output: "world hello"

Example 3:

> Input: s = "a good   example"\
Output: "example good a"
 

Constraints:

>- 1 <= s.length <= 104
>- s contains English letters (upper-case and lower-case), digits, and spaces ' '.
> -There is at least one word in s.


## Solution

### Go

```Go
// Using strings.Fields (assigned to words variable) to get word only from string given
// if length of the words is 0 then return "" (s is an empty string)
// print words backward using two pointer (l and r) and strings.Join to join words

func reverseWords(s string) string {
    words := strings.Fields(s)
    if len(words) == 0 {
        return ""
    }

    l, r := 0, len(words)-1
    for l < r {
        words[l], words[r] = words[r], words[l]
        l++
        r--
    }
    return strings.Join(words, " ")
}
```

### Python

```Python
#split sentencce into word
#print words backward

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])
```