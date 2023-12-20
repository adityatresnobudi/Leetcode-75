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
