# 773. Sliding Puzzle

# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
# and an empty square represented by 0.
#
# A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
#
# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
#
# Given a puzzle board, return the least number of moves required so that
# the state of the board is solved. If it is impossible for the state of the board
# to be solved, return -1.
#
# Examples:
#
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
#
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
#
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
#
# Input: board = [[3,2,4],[1,5,0]]
# Output: 14
#
# Note:
#
#     board will be a 2 x 3 array as described above.
#     board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
#

import collections

class Solution(object):

    # https://blog.csdn.net/fuxuemingzhu/article/details/82919580
    # 每次移动都相当于得到了一个新的状态，同时记录得到这个状态需要的步数，
    # 并把这个状态保存到已经出现过的set里。
    # 本题的难点在于使用如果把二维数组和字符串进行转化的问题，代码写的很清楚了。

    # 需要注意的是，通过二维坐标得到字符串索引的方式是x * cols + y

    # python的字符画不支持直接指定某个位置的字符，因此迫不得已用了几次string和list互转的过程。

    # 最坏情况下的时间复杂度是O((MN)!)，空间复杂度是O(MN)。M,N代表行列数，这个题分别为2，3.
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        goal = "123450"
        start = self.board2str(board)

        bfs = collections.deque()
        bfs.append((start, 0))  # (path, step)
        visited = set()
        visited.add(start)

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while bfs:
            path, step = bfs.popleft()
            if path == goal:
                return step
            p = path.index("0")
            x, y = p//3, p%3
            path = list(path)
            for dir in dirs:
                tx = x + dir[0]
                ty = y + dir[1]
                if tx < 0 or tx >= 2 or ty < 0 or ty >= 3:
                    continue
                path[tx * 3 + ty], path[x * 3 + y] = path[x * 3 + y], path[tx * 3 + ty]
                pathStr = "".join(path)
                if pathStr not in visited:
                    bfs.append((pathStr, step + 1))
                    visited.add(pathStr)
                path[tx * 3 + ty], path[x * 3 + y] = path[x * 3 + y], path[tx * 3 + ty]
        return -1

    def board2str(self, board):
        bstr = ""
        for i in range(2):      # rows
            for j in range(3):  # cols
                bstr += str(board[i][j])
        return bstr

print(Solution().board2str([[1,2,3],[4,0,5]]))
print(Solution().slidingPuzzle([[1,2,3],[4,0,5]]))
print(Solution().slidingPuzzle([[1,2,3],[5,4,0]]))
print(Solution().slidingPuzzle([[4,1,2],[5,0,3]]))
