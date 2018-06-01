# 361 Bomb Enemy

# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), 
# return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point 
# until it hits the wall since the wall is too strong to be destroyed.
# Note that you can only put the bomb at an empty cell.

# Example:
# For the given grid
# 0 E 0 0
# E 0 W E
# 0 E 0 0
# return 3. (Placing a bomb at (1,1) kills 3 enemies)

class Solution:
    # https://www.youtube.com/watch?v=X3WrZG08ns8
    # https://github.com/algorhythms/LeetCode/blob/master/361%20Bomb%20Enemy.py
    # 
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        rowKills: number of enemies killed in the current row at the current pos
        colKills[n]: number of enemies killed in column k (0 <= k < n) in the current row
        Time O(3mn) = O(mn)
        Space O(n)
        """
        m = len(grid)
        n = len(grid[0]) if m else 0
        if not m or not n:
            return 0

        res = 0
        colKills = [0] * n
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == 'W':
                    rowKills = 0
                    for k in range(j, n):
                        if grid[i][k] == 'E':
                            rowKills += 1
                        if grid[i][k] == 'W':
                            break
                if i == 0 or grid[i-1][j] == 'W':
                    colKills[j] = 0
                    # colKills = [0] * n
                    for k in range(i, m):
                        if grid[k][j] == 'E':
                            colKills[j] += 1
                        if grid[k][j] == 'W':
                            break
                if grid[i][j] == '0':
                    res = max(res, rowKills+colKills[j])
        return res

if __name__ == "__main__":
    print (Solution().maxKilledEnemies(["0E00", "E0WE", "0E00"]))
    #assert Solution().maxKilledEnemies(["0E00", "E0WE", "0E00"]) == 3
