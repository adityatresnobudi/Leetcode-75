# base case -> if city already visited return 0
# regular case -> if city not visited, recursively calls function to visit city until
# forming a circle

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = set()

        def dfs(isConnected, visited, city):
            if city in visited:
                return 0
            visited.add(city)
            for path in range(len(isConnected[city])):
                if isConnected[city][path] == 1:
                    dfs(isConnected, visited, path)
            return 1

        provinces = 0
        for i in range(len(isConnected)):
            provinces += dfs(isConnected, visited, i)
        return provinces
