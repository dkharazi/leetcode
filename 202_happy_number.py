# 202. Happy Number
#
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 1**2 + 9**2 = 82
# 8**2 + 2**2 = 68
# 6**2 + 8**2 = 100
# 1**2 + 0**2 + 0**2 = 1


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.helper([], n)

    # more efficient if using dict {}
    def helper(self, arr, n):
        sum = 0
        for d in str(n):
            sum += int(d) ** 2
        if sum == 1:
            return True

        if sum in arr:
            return False
        arr.append(sum)
        return self.helper(arr, sum)

    # http://blog.csdn.net/coder_orz/article/details/51315486
    def isHappy(self, n):
        dict = {}
        while True:
            dict[n] = True
            sum = 0
            # extract all digits from n
            while n:
                sum += (n % 10) * (n % 10)
                n /= 10
            if sum == 1:
                return True
            # if cycle starts return False
            if sum in dict:
                return False
            n = sum

    # Floyd Cycle Detection Algorithm
    def isHappy(self, n):
        slow = fast = n
        while True:
            slow = self.sumSquare(slow)
            fast = self.sumSquare(fast)
            fast = self.sumSquare(fast)
            if slow == fast:
                break
        return slow == 1

    def sumSquare(self, n):
        sum = 0
        while n:
            sum += (n%10) * (n%10)
            n /= 10
        return sum


if __name__ == '__main__':
    print Solution().isHappy(19)
