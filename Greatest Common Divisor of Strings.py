#check gcd(len(str1),len(str2))
#check which str is longer
#store letter from shorter str as long as the gcd as output
#check if the shorter str is a substring of longer str
#check if output*len(str1)/gcd and output*len(str2)/gcd is equal to str1 and str2 respectively
#if all yes then print output if no then print ""

class Solution(object):
    def computeGCD(self, a, b):
        if a > b:
            small = b
        else:
            small = a
        for i in range(1, small + 1):
            if((a % i == 0) and (b % i == 0)):
                gcd = i
             
        return gcd

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        gcd = self.computeGCD(len(str1), len(str2))
        if len(str1) > len(str2):
            output = str2[:gcd]
        else:
            output = str1[:gcd]
        if ((output in str1) and (output in str2)):
            if ((output*(len(str1) / gcd)) == str1) and (output*(len(str2) / gcd) == str2):
                return output
            else:
                return ""
        else:
            return ""
