class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        result = []
        count = 1
        for i in range(1,len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                result.append([chars[i-1],count])
                count = 1
        result.append([chars[-1], count])
        i = 0
        for char, count in result:
            chars[i] = char
            i += 1
            if count > 1:
                for item in str(count):
                    chars[i] = str(item)
                    i += 1
        return i
