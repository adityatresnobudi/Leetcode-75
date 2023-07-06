# using stack
# iterate through the string
# if char is not * then append to stack
# else pop the last char in stack

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if char != '*': 
                stack.append(char)
            else: 
                stack.pop()
        return ''.join(stack)
