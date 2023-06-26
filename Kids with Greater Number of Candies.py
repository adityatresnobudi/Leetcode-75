#make empty array for result
#iterate for each kid to find maximum value after getting extraCandies
#if higher than max(candies) then true otherwise false

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        for kid in candies:
            if max(candies) <= kid + extraCandies:
                result.append(True)
            else:
                result.append(False)
        return result
