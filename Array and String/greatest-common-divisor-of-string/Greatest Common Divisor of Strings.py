# check if str1+str2 == str2+str1
# if false then return "" (no gcd of string)
# if true find length gcd from both str
# return str1[:length]

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
