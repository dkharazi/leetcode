# 400 Nth Digit

# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
#
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).
#
# Example 1:
#
# Input:
# 3
#
# Output:
# 3
#
# Example 2:
#
# Input:
# 11
#
# Output:
# 0
#
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

class Solution(object):
    # https://www.hrwhisper.me/leetcode-contest-5-solution/
    # 主要是求出该数字需要的位数，因为一位数有9*1，两位数有90*2，三位数有900*3以此类推。
    # 剩下的直接看看是否整除啥的即可。
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 9
        cnt = 1
        while n > num * cnt:
            n -= (num * cnt)
            num *= 10
            cnt += 1
        t = n // cnt
        base = 10 ** (cnt - 1) + t
        if t * cnt == n:
            return (base - 1) % 10
        n -= t * cnt
        return int(str(base)[::-1][-n])

print(Solution().findNthDigit(11))
