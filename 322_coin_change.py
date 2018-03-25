# 322. Coin Change
#  You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)

# Example 2:
# coins = [2], amount = 3
# return -1.

# Note:
# You may assume that you have an infinite number of each kind of coin.

class Solution(object):
    # https://gengwg.blogspot.com/2018/03/leetcode-322-coin-change.html
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [-1] * amount
        for i in range(1, amount+1):
            # set min to a large impossible value
            # note it must be inside the loop
            mincoins = i + 1
            for j in [c for c in coins if c <= i]:  # only possible if coin value smaller than i
                if dp[i-j] != -1:   # if i-j is impossible, i is also impossible.
                    mincoins = min(mincoins, dp[i-j] + 1)
            # if min coints is impossible set it to -1
            dp[i] = -1 if mincoins == i + 1 else mincoins
        return dp[amount]

if __name__ == '__main__':
    s = Solution()
    print s.coinChange([1], 1)  # 1
    print s.coinChange([1, 2, 5], 11)   # 3
    print s.coinChange([1,5,10,25], 63)   # 6
    print s.coinChange([1,5,10,21,25], 63)   # 3


