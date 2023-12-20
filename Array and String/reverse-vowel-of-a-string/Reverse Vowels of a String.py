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
