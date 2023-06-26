#rules 0 0 0 -> 0 1 0
#add extra 0 in front and behind flowerbed for iteration
#iterate for every flowerbed space
#if following the rules then place flower in the middle (between 0) and flower-1
#if all flower is placed correctly according to rules then True otherwise False

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        f = [0] + flowerbed + [0]

        for i in range (1, len(f) - 1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0
