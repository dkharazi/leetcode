# 241. Different Ways to Add Parentheses
#
# Given a string of numbers and operators, return all possible results
# from computing all the different possible ways to group numbers and operators.
# The valid operators are +, - and *.
#
# Example 1
# Input: "2-1-1".
#
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Output: [0, 2]
#
#
# Example 2
# Input: "2*3-4*5"
#
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Output: [-34, -14, -10, -10, 10]
#
# http://www.tangjikai.com/algorithms/leetcode-241-different-ways-to-add-parentheses
# Divide and Conque.
# For each sign, divide into two parts for before and after it.

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        ans = []
        for i in range(len(input)):
            c = input[i]
            if c in '+-*':
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i+1:])
                for m in l:
                    for n in r:
                        if c == '+':
                            ans.append(m + n)
                        elif c == '-':
                            ans.append(m - n)
                        elif c == '*':
                            ans.append(m * n)
        # edge condition to stop recursion
        # input is digit
        if not ans:
            ans.append(int(input))
        return ans

if __name__ == '__main__':
    print Solution().diffWaysToCompute("2-1-1")
