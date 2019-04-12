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


    # 一道难度适中的Union-Find题目。这类题目也有套路：首先为每个顶点初始化一个单独的集合；
    # 然后遍历，每次遇到一个边，就把边的两个顶点所属的集合进行合并，
    # 同时总的连通图数量减1。注意判断两个顶点是否属于同一个集合的经典代码，个人感觉应该背下来^_^。

    # 这道题目用BFS和DFS也可以求解，但代码要相对复杂一些。
    # --------------------- 
    # 原文：https://blog.csdn.net/magicbean2/article/details/76474678 
    def countComponents(self, n, edges):
        parents = [i for i in range(n)]
        ret = n
        for edge in edges:
            par1 = edge[0]
            par2 = edge[1]
            while par1 != parents[par1]: # due to connected nodes before
                par1 = parents[par1]
            while par2 != parents[par2]:
                par2 = parents[par2]
            if par1 != par2:
                # connect par2 with par1
                parents[par2] = par1
                ret -= 1
        return ret



if __name__ == '__main__':
    
    print(Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]))
    print(Solution().countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
