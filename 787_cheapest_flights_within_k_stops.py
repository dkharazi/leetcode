# 787. Cheapest Flights Within K Stops


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
