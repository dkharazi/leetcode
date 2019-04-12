# 787. Cheapest Flights Within K Stops

# There are n cities connected by m flights. 
# Each fight starts from city u and arrives at v with a price w.

# Now given all the cities and flights, together with starting city src and the destination dst, 
# your task is to find the cheapest price from src to dst with up to k stops. 
# If there is no such route, output -1.

# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation: 
# The graph looks like this:


# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation: 
# The graph looks like this:


# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

# Note:

#     The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
#     The size of flights will be in range [0, n * (n - 1) / 2].
#     The format of each flight will be (src, dst, price).
#     The price of each flight will be in the range [1, 10000].
#     k is in the range of [0, n - 1].
#     There will not be any duplicated flights or self cycles.


import collections
import heapq

class Solution:
    # https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115541/Easy-and-Concise-Solution-Using-Priority-Queue-JavaPython
    # It happen to be the same idea of Dijkstra's algorithm, but we need to keep the path.
    # https://en.wikipedia.org/wiki/Dijkstra's_algorithm
    def findCheapestPrice(self, n, flights, src, dst, k):
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k-1))
        return -1

    def findCheapestPrice(self, n, flights, src, dst, K):
        kInfCost = 1e9
        cost = [kInfCost for _ in range(n)]
        cost[src] = 0

        for i in range(K+1):
            tmp = list(cost)
            for p in flights:
                tmp[p[1]] = min(tmp[p[1]], cost[p[0]] + p[2])
            cost = tmp

        return -1 if cost[dst] >= kInfCost else cost[dst]

    # Bellman-Ford algorithm
    # dp[k][i]: min cost from src to i taken up to k flights (k-1 stops)
    # init: dp[0:k+2][src] = 0
    # transition: dp[k][i] = min(dp[k-1][j] + price[j][i])
    # ans: dp[K+1][dst]
    # Time complexity: O(k * |flights|) / O(k*n^2)
    # Space complexity: O(k*n) -> O(n)
    # w/o space compression O(k*n)
    def findCheapestPrice(self, n, flights, src, dst, K):
        kInfCost = 1e9
        dp = [[kInfCost for _ in range(n)] for __ in range(K+2)]
        dp[0][src] = 0
        for i in range(1, K+2):
            dp[i][src] = 0
            for p in flights:
                dp[i][p[1]] = min(dp[i][p[1]], dp[i-1][p[0]] + p[2])
        return -1 if dp[K+1][dst] >= kInfCost else dp[K+1][dst]



if __name__ == '__main__':
    print(Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 1))
