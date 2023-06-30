#vowel array aiueo
#sliding windows with length k, max_vowel = how many vowel in windows
#iterate given array with popping the head and appending the array
#if popped elemnt is in vowel and new element is in vowel then max_vowel not change
#and other if else condition

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ["a","i","u","e","o"]
        countVowel = 0
        for i in range(k):
            if s[i] in vowels:
                countVowel += 1
        
        maxVowel = countVowel

        for i in range(k, len(s)):
            if s[i] in vowels:
                countVowel += 1
            else:
                pass
            if s[i-k] in vowels:
                countVowel -= 1
            else:
                pass
            maxVowel = max(maxVowel, countVowel)
        return maxVowel
