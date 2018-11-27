# 357. Count Numbers with Unique Digits

# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.
#
# Example:
#
# Input: 2
# Output: 91
# Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
#              excluding 11,22,33,44,55,66,77,88,99
#

# For the first (most left) digit, we have 9 options (no zero);
# for the second digit we used one but we can use 0 now, so 9 options;
# and we have 1 less option for each following digits.
# Number can not be longer than 10 digits.

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        product = 1
        ans = 1
        for i in range(min(n, 10)):
            product *= choices[i]
            ans += product
        return ans

