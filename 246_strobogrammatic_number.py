# 246 Strobogrammatic Number
# ======================

# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).

# Write a function to determine if a number is strobogrammatic. The number is
# represented as a string.

# For example, the numbers "69", "88", and "818" are all strobogrammatic.

class Solution:
    def isStrobogrammatic(self, num):
        table = {'0': '0', '1': '1', '6': '9', '8':'8', '9':'6'}
        n = len(num)
        for i in range((n>>1)+1):
            if num[i] not in table or num[n-i-1] != table[num[i]]:
                return False
        return True

s = Solution()
print(s.isStrobogrammatic('619'))
print(s.isStrobogrammatic('9'))
