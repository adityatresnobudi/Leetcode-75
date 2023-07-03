#iterate and adding every elemennt
#saving max element

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        currAlt = 0
        maxAlt = 0
        for i in gain:
            currAlt += i
            maxAlt = max(maxAlt, currAlt)
        return maxAlt
