# solution not using hash set
# take array col to store column element from grid
# iterate through row grid, if col == row.grid then resule + 1

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col = []
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                col.append(grid[j][i])
            for k in range(len(grid)):
                if col == grid[k]:
                    res += 1
                else:
                    pass
            col = []
        return res
