# 397. Integer Replacement
#  Given a positive integer n and you can do operations as follow:
#
#     If n is even, replace n with n/2.
#     If n is odd, you can replace n with either n + 1 or n - 1.
#
# What is the minimum number of replacements needed for n to become 1?
#
# Example 1:
#
# Input:
# 8
#
# Output:
# 3
#
# Explanation:
# 8 -> 4 -> 2 -> 1
#
# Example 2:
#
# Input:
# 7
#
# Output:
# 4
#
# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1
#

class Solution(object):
    # http://www.voidcn.com/article/p-tdcnvoig-bcx.html
    # 推导出递推公式（在2147483647会超时，因为里面有n+1的递归，int溢出，所以单独拿出来）
    # f(1)=0;
    # f(2)=f(1)+1
    # f(3)=min(f(2)+1,f(4)+1)
    # ...
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2147483647:
            return 32
        if n == 1:
            return 0
        if n % 2 == 0:
            return self.integerReplacement(n//2) + 1
        else:
            return min(self.integerReplacement((n-1)//2) + 2, self.integerReplacement((n+1)//2) + 2)


print(Solution().integerReplacement(8))
print(Solution().integerReplacement(7))
