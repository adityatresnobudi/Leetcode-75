# 1071. Greatest Common Divisor of Strings

Difficulty : `Easy`

For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + ... + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.

 

Example 1:

> Input: str1 = "ABCABC", str2 = "ABC"\
Output: "ABC"

Example 2:

> Input: str1 = "ABABAB", str2 = "ABAB"\
Output: "AB"

Example 3:

> Input: str1 = "LEET", str2 = "CODE"\
Output: ""
 

Constraints:

>- 1 <= str1.length, str2.length <= 1000
>- str1 and str2 consist of English uppercase letters.


## Solution

### Go

```Go
func gcd(num1, num2 int) int {
    for num2 != 0 {
        num1, num2 = num2, num1%num2
    }

    return num1
}
func gcdOfStrings(s1 string, s2 string) string {
    if s1+s2 != s2+s1 {
        return ""
    }

    length := gcd(len(s1), len(s2))
    return s1[:length]
}
```

### Python

```Python
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(a, b):
            while b != 0:
                a, b = b, a%b
            return a

        if str1+str2 != str2+str1:
            return ""
        
        length = gcd(len(str1), len(str2))
        return str1[:length]
```

In this code, we check first if `str1+str2` equals `str2+str1`, if false then immediately we can return `""` because it simply means there is no similarities between `str1` and `str2`, if true then we calculate the greatest common divisor from both string to get the maximum `length` and we can return `string[:length]`.