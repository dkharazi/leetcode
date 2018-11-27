# 323 Number of Connected Components in an Undirected Graph

# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to find the number of connected components in an undirected graph.
#
# Example 1:
#
#      0          3
#      |          |
#      1 --- 2    4
#
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.
#
# Example 2:
#
#      0           4
#      |           |
#      1 --- 2 --- 3
#
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.
#
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected,
# [0, 1] is the same as [1, 0] and thus will not appear together in edges.

class Solution:
    # https://all4win78.wordpress.com/2016/06/27/leetcode-323-number-of-connected-components-in-an-undirected-graph/
    def countComponents(self, n, edges):
        count = n
        idx = [i for i in range(n)]
        #for i in range(n):
        # idx[i] = i

        for edge in edges:
            a = edge[0]
            b = edge[1]
            fa = idx[a]
            fb = idx[b]
            if fa != fb:
                for i in range(n):
                    if idx[i] == fb:
                        idx[i] = fa
                count -= 1
        return count

print(Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]))
print(Solution().countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
