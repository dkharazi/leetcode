# 326. Power of Three

# Given an integer, write a function to determine if it is a power of three.
#
# Example 1:
#
# Input: 27
# Output: true
#
# Example 2:
#
# Input: 0
# Output: false
#
# Example 3:
#
# Input: 9
# Output: true
#
# Example 4:
#
# Input: 45
# Output: false
#
# Follow up:
# Could you do it without using any loop / recursion?
#

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False

        while n % 3 == 0:
            n = n // 3
        return n == 1

    def isPowerOfThree(self, n):
        # 1162261467 is 3^19,  3^20 is bigger than int
        return n > 0 and (1162261467 % n == 0)

print(Solution().isPowerOfThree(27))
print(Solution().isPowerOfThree(0))
print(Solution().isPowerOfThree(9))
print(Solution().isPowerOfThree(45))
