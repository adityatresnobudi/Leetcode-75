# check count of letter in word
# sort the value, True -> same sorted count
# chech if both word has the same exact letter, True -> same letter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        hash_w1 = Counter(word1)
        hash_w2 = Counter(word2)

        count1 = sorted(hash_w1.values())
        count2 = sorted(hash_w2.values())
        
        set1 = set(word1)
        set2 = set(word2)

        if count1 == count2 and set1 == set2:
            return True
        else:
            pass
        return False
