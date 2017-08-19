"""
50. Pow(x, n)

Implement pow(x, n).

http://www.cnblogs.com/zuoyuan/p/3773182.html

if n is even:
n = 2 * n/2;
pow(x, n)
= x^n
= x^(2 * n/2)
= (x^2)^(n/2)
= pow(x*x, n/2);

if n is odd:
n = 2 * n/2 + 1;
pow(x, n)
= x^n
= x^(2 * n/2 + 1)
= (x^2)^(n/2) * x   [x^(a+b) = x^a * x^b]
= pow(x*x, n/2) * x
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return self.myPow(x*x, n/2) * x
        else:
            return self.myPow(x*x, n/2)

if __name__ == '__main__':
    print Solution().myPow(3., 2)