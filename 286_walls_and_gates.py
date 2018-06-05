# 286. WALLS AND GATES

# You are given a m x n 2D grid initialized with these three possible values.
#
# -1 – A wall or an obstacle.
# 0 – A gate.
# INF – Infinity means an empty room.
# We use the value 2^31 - 1 = 2147483647 to represent INF
# as you may assume that the distance to a gate is less than 2147483647.

# Fill each empty room with the distance to its nearest gate.
# If it is impossible to reach a gate, it should be filled with INF.
#
# For example, given the 2D grid:
#
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF

# After running your function, the 2D grid should be:
#
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4
#

class Solution:
    def wallsAndGates(self, rooms):
        """
        https://dyang2016.wordpress.com/2016/11/02/286-walls-and-gates/
        求矩阵中room到gate的最短距离这个题目用DFS 比较快。
        DFS: 找的时候如果当前点的值大于distance的值，就是符合条件的点。
        复杂度: 时间 MN4^K, 空间 4^N
        """
        if rooms is None or len(rooms) == 0 or rooms[0] is None or len(rooms[0]) == 0:
            return

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, 0)

    def dfs(self, rooms, x, y, distance):
        if x < 0 or x >= len(rooms) or y < 0 or y >= len(rooms[0]) or rooms[x][y] < distance:
            return

        rooms[x][y] = distance
        self.dfs(rooms, x + 1, y, distance + 1)
        self.dfs(rooms, x - 1, y, distance + 1)
        self.dfs(rooms, x, y + 1, distance + 1)
        self.dfs(rooms, x, y - 1, distance + 1)


if __name__ == '__main__':
    rooms = [
             [float("Inf"),  -1 , 0 , float("Inf")],
             [float("Inf"), float("Inf") ,float("Inf"),  -1],
             [float("Inf"),  -1 ,float("Inf"),  -1],
             [0,  -1, float("Inf"), float("Inf")]
             ]

    test = Solution()
    test.wallsAndGates(rooms)
    print(rooms)

