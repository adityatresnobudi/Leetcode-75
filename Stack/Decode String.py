# stack = []
# if element isnumber() then assign as current number
# then detect [, if detected get all char in after [ into one array until find ]
# decode with current number * char between []
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        currNum = 0
        currStr = ""
        for char in s:
            if char.isdigit():
                currNum = currNum * 10 + int(char)
            elif char == "[":
                stack.append(currNum)
                stack.append(currStr)
                currNum = 0
                currStr = ""
            elif char == "]":
                prevStr = stack.pop()
                prevNum = stack.pop()
                currStr = prevStr + currStr * prevNum
            else:
                currStr += char
        while stack:
            currStr = stack.pop() + currStr
        
        return currStr
