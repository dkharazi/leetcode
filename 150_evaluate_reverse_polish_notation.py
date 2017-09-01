# -*- coding: utf-8 -*-
# 150. Evaluate Reverse Polish Notation
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


class Solution(object):
    def evalRPN(self, tokens):
        """
        https://shenjie1993.gitbooks.io/leetcode-python/150%20Evaluate%20Reverse%20Polish%20Notation.html
        后缀表达式的形式为操作数1，操作数2，操作符，
        也就是操作符要进行计算操作的两个数（或者表达式）在它的前方，
        所以在遍历列表的时候，我们要将前面的操作符压入栈中，
        当遇到操作符的时候，我们将它对应的操作数弹出并进行计算，
        计算结果可能是其他操作符的操作数，
        它原来是一个表达式，我们将该表达式的值计算出来了，所以应该把那个值继续压栈，
        遍历完整个列表的时候，计算结束。
        这里特别要注意的是除法操作，
        因为给的表达式都是合法的，所以不用考虑除数为零的情况，
        但这里的除法操作是针对整数的，会对结果进行去尾操作。
        对负数与整数的除法操作也与Python自带的计算方式不同，
        Python计算-1//2结果为-1，而在这里应该为0，所以要进行特殊的处理。

        http://www.cnblogs.com/zuoyuan/p/3760530.html
        解题思路：这道题是经典的逆波兰式求值。
        具体思路是：开辟一个空栈，遇到数字压栈，遇到运算符弹出栈中的两个数进行运算，并将运算结果压栈，
        最后栈中只剩下一个数时，就是所求结果。
        这里需要注意的一点是python中的'/'除法和c语言不太一样。
        在python中，(-1)/2=-1，而在c语言中，(-1)/2=0。
        也就是c语言中，除法是向零取整，即舍弃小数点后的数。
        而在python中，是向下取整的。
        而这道题的oj是默认的c语言中的语法，所以需要在遇到'/'的时候注意一下。

        :param tokens: List[str]
        :return: int
        """
        stack = []
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == '+':
                    stack.append(first + second)
                elif token == '-':
                    stack.append(first - second)
                elif token == '*':
                    stack.append(first * second)
                else:
                    if first * second < 0:
                        # / first, then -
                        stack.append(-(abs(first) // abs(second)))
                    else:
                        stack.append(first // second)

        return stack.pop()


if __name__ == "__main__":
    assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    print Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
