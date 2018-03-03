# 200. Number of Islands
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        http://www.tangjikai.com/algorithms/leetcode-200-number-of-islands

        We use a visited array to track whether the element is visited or not.
        When we find a  unvisited '1', DFS to mark all surrounding '1' to visited,
        then find other '1's.

        Complexity:
        O(mn) time
        O(mn) space
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(i, j, grid, visited)
                    res += 1
        return res

    def dfs(self, i, j, grid, visited):
        visited[i][j] = True

        if i + 1 < len(grid) and grid[i + 1][j] == '1' and not visited[i + 1][j]:
            self.dfs(i + 1, j, grid, visited)

        if j + 1 < len(grid[0]) and grid[i][j + 1] == '1' and not visited[i][j + 1]:
            self.dfs(i, j + 1, grid, visited)

        if i - 1 >= 0 and grid[i - 1][j] == '1' and not visited[i - 1][j]:
            self.dfs(i - 1, j, grid, visited)

        if j - 1 >= 0 and grid[i][j - 1] == '1' and not visited[i][j - 1]:
            self.dfs(i, j - 1, grid, visited)


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        http://zxi.mytechroad.com/blog/searching/leetcode-200-number-of-islands/
        for every land (1), visit its neighbor land using DFS,
        until there is no land,
        mark visited node as 0 (water).
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    self.dfs(grid, i, j, m, n)
        return ans

    def dfs(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j, m, n)
        self.dfs(grid, i - 1, j, m, n)
        self.dfs(grid, i, j + 1, m, n)
        self.dfs(grid, i, j - 1, m, n)

    # same as above solution, but put dfs func inside
    # this way no need for m, n
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, i, j):
            # reaches border or water
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    res += 1
        return res