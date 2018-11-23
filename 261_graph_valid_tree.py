# 261 Graph Valid Tree

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to check whether these edges make up a valid tree.
#
# For example:
#
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
#
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
#
# Hint:
#
#     Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree? Show More Hint
#
# Note: you can assume that no duplicate edges will appear in edges.
# Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
#
# https://nb4799.neu.edu/wordpress/?p=1143
# We need to check two properties to determine whether a set of edges form a valid tree:
#
#     it has n-1 edges
#     it is acyclic

class Solution(object):
    # This algorithm uses an idea called union find. You first initialize each node so that each node itself forms a node set.
    # (We use union_arr to record which set a node belongs to).  As we traverse all edges, we will find connected components.
    # The union find algorithm makes sure that every node in a connected component will point to a same node set by using find_union function.
    # Therefore, if we see a new edge with two points in the same node set, we will return False because the edge makes a cycle in the graph.
    # If no cycle is found, we will finally check if there are exactly n-1 edges to form a tree rather than disjoint parts in the graph.
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype:
        """
        union_arr = range(n) # only works in py2
        def find_union(p):
            if union_arr[p] == p:
                return p
            return find_union(union_arr[p])

        for p1, p2 in edges:
            p1_set = find_union(p1)
            p2_set = find_union(p2)
            #print p1_set, p2_set
            if p1_set == p2_set:
                return False
            union_arr[p1_set] = p2_set

        return len(edges) == n - 1

    # DFS
    # We start to visit all nodes from node 0.
    # If we finish traversing all reachable nodes but there are still some adjacency matrix entry left
    # then we know the given edges actually form multiple separate graphs. Therefore we should return False.
    def validTree(self, n, edges):
        adj = {s:[] for s in range(n)}
        for p1, p2 in edges:
            adj[p1].append(p2)
            adj[p2].append(p1)
        stk = [0]
        while stk:
            cur = stk.pop()
            # stk.extend(xxx) equivalent to stk += xxx
            stk.extend(adj.pop(cur, [])) # if `cur` not in keys, pop [] instead of raising KeyError.
        return len(edges) == n - 1 and not adj

    # BFS
    # Similar idea as in code 2. But you implement the traversal of nodes using deque.
    def validTree(self, n, edges):
        from collections import deque
        adj = {s:[] for s in range(n)}
        for p1, p2 in edges:
            adj[p1].append(p2)
            adj[p2].append(p1)
        q = deque()
        q.append(0)
        while q:
            cur = q.popleft()
            q.extend(adj.pop(cur, []))
        return len(edges) == n - 1 and not adj

print(Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
