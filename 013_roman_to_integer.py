"""
13. Roman ot Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

"""


class Solution(object):
    # https://github.com/zhouchong90/LeetCode-Python-Solution/blob/master/Solutions/13%20Roman%20to%20Integer.py
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        """
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        result = 0
        for i in range(len(s) - 1):
            # if current char smaller than next char, need substract it
            if roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
                print result
            else: # add current position char value
                result += roman[s[i]]
        else:
            result += roman[s[-1]]

        return result

if __name__ == '__main__':
    print Solution().romanToInt("CM")