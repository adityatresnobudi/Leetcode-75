#put pointer at the first and last height
#count volume
#iterate pointer if height is shorter (left to right, right to left)
#count volume and compare with last volume to search for max(volume)
#finish iterating after pointer left passed pointer right (vice versa)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        highestVol = -1
        pointL = 0
        pointR = len(height) - 1
        while pointL < pointR:
            vol = (pointR - pointL) * min(height[pointR], height[pointL])
            highestVol = max(highestVol, vol)
            if height[pointL] < height[pointR]:
                pointL += 1
            else:
                pointR -= 1
        return highestVol
