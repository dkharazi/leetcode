"""
8. String to Integer (atoi)

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases.
If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated.
If you still see your function signature accepts a const char * argument,
please click the reload button  to reset your code definition.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary
until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign
followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace characters,
no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

author: https://github.com/gengwg
"""


class Solution(object):

    INT_MAX = 2147483647
    INT_MIN = -2147483648

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        #try:
        #    int(str)
        #except ValueError:
        #    return 0

        str = str.strip()

        if len(str) == 0:
            return 0

        answer = 0
        sign = 1
        digits = list(str)

        # remove leading sign.
        # note use elif, because otherwise first del could already modified the list
        if digits[0] == '+' and len(digits) > 1:
            del digits[0]
        elif digits[0] == '-' and len(digits) > 1:
            del digits[0]
            sign = -1

        """
        # this part for not allow any non digit characters in string.
        for digit in digits:
            if ord(digit) < ord('0') or ord(digit) > ord('9'):
                return 0

        for index, digit in enumerate(reversed(digits)):
            answer += (ord(digit) - ord('0')) * 10 ** index

        """

        for digit in digits:
            # ignore additional characters after any non-digit characters
            if ord(digit) < ord('0') or ord(digit) > ord('9'):
                break
            # shift by 10 the answer and add current digit
            answer = 10 * answer + ord(digit) - ord('0')
            # answer *= 10

        # multiplied answer by 1 time more in above loop, divide it here.
        # answer /= 10

        if sign * answer < self.INT_MIN:
            return self.INT_MIN
        if sign * answer > self.INT_MAX:
            return self.INT_MAX

        return sign * answer

    # http://blog.csdn.net/coder_orz/article/details/52053932
    # this one not need list
    def myAtoi2(self, str):

        if not str:
            return 0
        str = str.strip()
        number, flag = 0, 1
        if str[0] == '-':
            str = str[1:]
            flag = -1
        elif str[0] == '+':
            str = str[1:]
        for c in str:
            if '0' <= c <= '9':
                number = 10 * number + ord(c) - ord('0')
            else:
                break
        number *= flag
        number = number if number <= 2147483647 else 2147483647
        number = number if number >= -2147483648 else -2147483648
        return number

    # using regex
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re

        str = str.strip()
        try:
            res = re.search('(^[\+\-]?\d+)', str).group()
            res = int(res)
            res = res if res <= 2147483647 else 2147483647
            res = res if res >= -2147483648 else -2147483648
        except:
            res = 0
        return res

if __name__ == '__main__':
    print Solution().myAtoi("-12345")
    print Solution().myAtoi("  -0012a42")
    print Solution().myAtoi("+")
    print Solution().myAtoi("")
    print Solution().myAtoi("003")
    print Solution().myAtoi("+-3")
    print Solution().myAtoi("-+3")
    print Solution().myAtoi("123")
