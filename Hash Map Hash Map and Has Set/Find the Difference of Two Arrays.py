#change to set -> no duplicate
#iterate through nums1
#if element exist in both set then remove else pass
#return list of list

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        n1 = set(nums1)
        n2 = set(nums2)
        for num in list(n1):
            if num in n1 and num in n2:
                n1.remove(num)
                n2.remove(num)
            else:
                pass
        return [list(n1),list(n2)]
