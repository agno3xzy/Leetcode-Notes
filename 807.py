from typing import List, Any, Tuple, Union
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        maxTop = [0]*len(grid)
        maxLeft = [0]*len(grid)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[j][i] > maxTop[i]:
                    maxTop[i] = grid[j][i]
                if grid[i][j] > maxLeft[i]:
                    maxLeft[i] = grid[i][j]
        maxCount = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if min(maxLeft[i], maxTop[j]) > grid[i][j]:
                    maxCount = maxCount + min(maxLeft[i], maxTop[j]) - grid[i][j]
        return maxCount

    def maxIncreaseKeepingSkyline2(self, grid):
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]
        print(row_maxes)
        print(col_maxes)
        return sum(min(row_maxes[r], col_maxes[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))



grid = [[59,88,44],[3,18,38],[21,26,51]]
x = Solution()
x.maxIncreaseKeepingSkyline(grid)
print(x.maxIncreaseKeepingSkyline2(grid))

