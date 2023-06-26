#make empty array for vowel
#iteration for storing vowel from back to front
#iteration for changing vowel from front to back according to array

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
            if s_list[pointL] in vowels and s_list[pointR] in vowels:
                s_list[pointL], s_list[pointR] = s_list[pointR], s_list[pointL]
                pointL += 1
                pointR -= 1
            elif s_list[pointL] in vowels:
                pointR -= 1
            elif s_list[pointR] in vowels:
                pointL += 1
            else:
                pointL += 1
                pointR -= 1
        return "".join(s_list)
